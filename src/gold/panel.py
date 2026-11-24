"""Tahap 4 — Pembentukan panel Gold provinsi x tahun dan aturan pemilihan seri kanonik.

Menerapkan aturan penyeleksian tepat satu nilai per provinsi x periode x konsep:
1. Pemilihan seri kanonik per konsep di tingkat provinsi:
   - air_layak: var845
   - air_aman: var2741
   - sanitasi_layak: var847
   - cuci_tangan: var1273
   - sanitasi_aman: var2179 (var2749 tidak terpilih karena nilainya identik dengan var2179 rincian gabungan,
     namun var2749 tidak memuat rincian perkotaan/perdesaan serta bolong di Papua Pegunungan).
2. Penanganan snapshot ganda:
   - Apabila terdapat perbedaan nilai antar-snapshot, snapshot terbaru yang dipilih (sudah konsisten di Silver).
3. Penanganan periode:
   - Data tahunan dipakai langsung; periode semesteran/bulanan tidak dirata-ratakan sembarangan (di Kasus 17
     seluruh data BPS berjenis tahunan).
4. Pemisahan rincian:
   - Panel total (lebar) untuk rekonsiliasi dan analisis umum.
   - Panel berincian (panjang) tetap mempertahankan rincian perkotaan (daerah=URBAN) dan perdesaan (daerah=RURAL).
5. Membawa penanda anomali (outlier, patahan seri, patahan wilayah, cakupan parsial, perbedaan struktural)
   dari Sprint 1 tanpa menghapus nilai aslinya.
"""
from pathlib import Path
import pandas as pd

from src.laporan import ROOT, catat
from src.silver import deret

PANEL_GOLD_LEBAR = ROOT / "data" / "gold" / "panel_provinsi_tahunan.parquet"
PANEL_GOLD_PANJANG = ROOT / "data" / "gold" / "gold_provinsi.parquet"

# Pemetaan seri kanonik ke nama konsep baku
KONSEP_KANONIK = {
    "var845": "air_layak",
    "var2741": "air_aman",
    "var847": "sanitasi_layak",
    "var2179": "sanitasi_aman",
    "var1273": "cuci_tangan",
}


def muat_anomali():
    """Membaca berkas anomali hasil Sprint 1 untuk ditempelkan sebagai penanda."""
    jalur_anomali = ROOT / "reports" / "anomali.csv"
    if not jalur_anomali.exists():
        return pd.DataFrame(columns=["seri_kode", "wilayah_kode", "periode", "kategori"])
    df = pd.read_csv(jalur_anomali)
    df["periode"] = df["periode"].astype(str)
    return df[["seri_kode", "wilayah_kode", "periode", "kategori"]].drop_duplicates()


def seleksi_kanonik(silver):
    """Memilih tepat satu nilai per provinsi x periode x indikator/konsep.
    Mengembalikan: (df_terpilih, df_tidak_terpilih)
    """
    prov = silver[silver["wilayah_kode"] != 9999].copy()
    prov["periode"] = prov["periode"].astype(str)

    # Filter seri kanonik
    mask_kanonik = prov["seri_kode"].isin(KONSEP_KANONIK)
    terpilih = prov[mask_kanonik].copy()
    tidak_terpilih = prov[~mask_kanonik].copy()

    terpilih["konsep"] = terpilih["seri_kode"].map(KONSEP_KANONIK)

    # Tempelkan label penanda anomali/patahan dari Sprint 1
    terpilih["deret"] = [deret.label(s, r) for s, r in zip(terpilih["seri_kode"], terpilih["rincian"])]
    anomali = muat_anomali()
    if not anomali.empty:
        terpilih = terpilih.merge(
            anomali.rename(columns={"seri_kode": "deret", "kategori": "flag_anomali"}),
            on=["deret", "wilayah_kode", "periode"], validate="many_to_one",
            how="left",
        )
        terpilih["flag_anomali"] = terpilih["flag_anomali"].fillna("normal")
    else:
        terpilih["flag_anomali"] = "normal"

    diprofilkan = {label for label, _, _ in deret.daftar()}
    terpilih.loc[~terpilih["deret"].isin(diprofilkan), "flag_anomali"] = "tidak_diprofilkan"
    return terpilih.drop(columns="deret"), tidak_terpilih


def bentuk_panel(silver):
    """Membentuk panel Gold provinsi x tahun per konsep."""
    terpilih, tidak_terpilih = seleksi_kanonik(silver)

    # 1. Panel panjang lengkap dengan rincian dan flag anomali
    PANEL_GOLD_PANJANG.parent.mkdir(parents=True, exist_ok=True)
    kolom_panjang = [
        "konsep", "seri_kode", "wilayah_kode", "nama_wilayah",
        "periode", "jenis_periode", "rincian", "nilai", "satuan",
        "flag_anomali", "_berkas_raw", "_sha256_raw"
    ]
    df_panjang = terpilih[kolom_panjang].sort_values(
        ["konsep", "wilayah_kode", "periode", "rincian"]
    ).reset_index(drop=True)
    df_panjang.to_parquet(PANEL_GOLD_PANJANG, index=False)

    # 2. Panel lebar (tingkat total per konsep)
    df_total = terpilih[terpilih["rincian"] == "total"].copy()
    df_lebar = df_total.pivot(
        index=["wilayah_kode", "nama_wilayah", "periode"],
        columns="konsep",
        values="nilai"
    ).reset_index()

    # Rujuk seri asal per konsep
    df_lebar.columns.name = None
    df_lebar.to_parquet(PANEL_GOLD_LEBAR, index=False)

    # Catat metrik
    catat(
        baris_gold_provinsi=len(df_panjang),
        baris_gold_panel_lebar=len(df_lebar),
        baris_silver_tidak_terpilih=len(tidak_terpilih)
    )

    print(f"           Gold: {len(df_panjang):,} baris terpilih ({len(tidak_terpilih)} tidak terpilih) -> {PANEL_GOLD_PANJANG.relative_to(ROOT)}")
    print(f"           Gold Panel Lebar: {len(df_lebar):,} baris (provinsi x tahun) -> {PANEL_GOLD_LEBAR.relative_to(ROOT)}")

    return {
        "gold_panjang": df_panjang,
        "gold_lebar": df_lebar,
        "tidak_terpilih": tidak_terpilih
    }
