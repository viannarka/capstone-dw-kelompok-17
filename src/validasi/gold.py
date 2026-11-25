"""Aturan validasi Gold dan rekonsiliasi (Sprint 2).

Setiap fungsi menerima (silver, gold) dan mengembalikan DataFrame baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src.gold.nasional import REKONSILIASI

KATEGORI_SAH = {
    "definisi berbeda",
    "metode berbeda",
    "vintage berbeda",
    "cakupan berbeda",
    "belum terjelaskan",
}


def _muat_tabel_gold(gold):
    panel = gold.get("panel", {}) if isinstance(gold, dict) else {}
    gp = panel.get("gold_panjang")
    gl = panel.get("gold_lebar")
    gn = gold.get("nasional_gold") if isinstance(gold, dict) else None
    rek = gold.get("rekonsiliasi") if isinstance(gold, dict) else None
    if rek is None and REKONSILIASI.exists():
        rek = pd.read_parquet(REKONSILIASI)
    return gp, gl, gn, rek


def kunci_panel_unik(silver, gold):
    """Kunci panel Gold (provinsi panjang, provinsi lebar, nasional, rekonsiliasi) tidak kembar."""
    gp, gl, gn, rek = _muat_tabel_gold(gold)
    cek = [
        ("gold_provinsi", gp, ["wilayah_kode", "periode", "konsep", "rincian"]),
        ("panel_provinsi_tahunan", gl, ["wilayah_kode", "periode"]),
        ("gold_nasional", gn, ["seri_kode", "periode"]),
        ("rekonsiliasi", rek, ["id_perbandingan", "periode"]),
    ]
    buruk = []
    for nama, df, kunci in cek:
        if df is None or df.empty:
            continue
        dup = df[df.duplicated(kunci, keep=False)]
        if not dup.empty:
            bagian = dup[kunci].copy()
            bagian.insert(0, "tabel", nama)
            buruk.append(bagian)
    return pd.concat(buruk, ignore_index=True) if buruk else pd.DataFrame()


def satu_satuan_per_indikator(silver, gold):
    """Setiap indikator/konsep di Gold hanya memiliki satu satuan baku."""
    gp, _, gn, _ = _muat_tabel_gold(gold)
    buruk = []
    if gp is not None and not gp.empty:
        for kolom in ("konsep", "seri_kode"):
            n = gp.groupby(kolom)["satuan"].nunique()
            ganda = n[n > 1]
            if not ganda.empty:
                buruk.append(pd.DataFrame({"tabel": "gold_provinsi", "kolom": kolom, "nilai": ganda.index, "jumlah_satuan": ganda.values}))
    if gn is not None and not gn.empty:
        n = gn.groupby("seri_kode")["satuan"].nunique()
        ganda = n[n > 1]
        if not ganda.empty:
            buruk.append(pd.DataFrame({"tabel": "gold_nasional", "kolom": "seri_kode", "nilai": ganda.index, "jumlah_satuan": ganda.values}))
    return pd.concat(buruk, ignore_index=True) if buruk else pd.DataFrame()


def sel_gold_punya_pasangan_silver(silver, gold):
    """Setiap sel pada Gold (provinsi dan nasional) memiliki pasangan identik di Silver."""
    gp, _, gn, _ = _muat_tabel_gold(gold)
    kunci = ["seri_kode", "wilayah_kode", "periode", "rincian", "_berkas_raw"]
    s_ref = silver[kunci + ["nilai"]].copy()
    s_ref["periode"] = s_ref["periode"].astype(str)
    s_ref = s_ref.rename(columns={"nilai": "nilai_silver"})

    buruk = []
    for nama, df in [("gold_provinsi", gp), ("gold_nasional", gn)]:
        if df is None or df.empty:
            continue
        g = df[kunci + ["nilai"]].copy()
        g["periode"] = g["periode"].astype(str)
        gabung = g.merge(s_ref, on=kunci, how="left")
        hilang = gabung["nilai_silver"].isna() | ((gabung["nilai"] - gabung["nilai_silver"]).abs() > 1e-9)
        if hilang.any():
            b = gabung.loc[hilang, kunci + ["nilai", "nilai_silver"]].copy()
            b.insert(0, "tabel", nama)
            buruk.append(b)
    return pd.concat(buruk, ignore_index=True) if buruk else pd.DataFrame()


def rekonsiliasi_berpasangan_berkategori(silver, gold):
    """Setiap baris rekonsiliasi berstatus 'berpasangan' memiliki kategori penjelasan yang sah."""
    _, _, _, rek = _muat_tabel_gold(gold)
    if rek is None or rek.empty:
        return pd.DataFrame()
    berpasangan = rek[rek["status"] == "berpasangan"].copy()
    if berpasangan.empty:
        return pd.DataFrame()
    kat = berpasangan["kategori"].fillna("").astype(str).str.strip()
    melanggar = ~kat.isin(KATEGORI_SAH)
    return berpasangan.loc[melanggar, ["id_perbandingan", "periode", "status", "kategori"]]


ATURAN = [
    ("gold_kunci_panel_unik", "kunci panel Gold dan rekonsiliasi tidak kembar", True, kunci_panel_unik),
    ("gold_satu_satuan_per_indikator", "satu indikator/konsep di Gold hanya punya satu satuan", True, satu_satuan_per_indikator),
    ("gold_sel_punya_pasangan_silver", "setiap sel Gold (provinsi dan nasional) punya pasangan di Silver", True, sel_gold_punya_pasangan_silver),
    ("rekonsiliasi_berpasangan_berkategori", "setiap baris rekonsiliasi berpasangan punya kategori sah", True, rekonsiliasi_berpasangan_berkategori),
]
