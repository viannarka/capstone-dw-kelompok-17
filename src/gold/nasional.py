"""Persiapan tahap 6 — tabel nasional semua seri dan daftar pasangan rekonsiliasi.

Sprint 1: tabel periode x seri (tampilan lebar) untuk baris Indonesia dan daftar pasangan rekonsiliasi.
Sprint 2: tabel Gold nasional dalam format panjang (satu baris per periode x seri), memuat 6 seri utama BPS
(`var845`, `var2741`, `var847`, `var1273`, `var2179`, `var2749`) dan 5 seri pembanding (`WSH_WATER_SAFELY_MANAGED`,
`WSH_HYGIENE_BASIC`, `SDGODAWS`, `SH.H2O.SMDW.ZS`, `SH.H2O.BASW.ZS`).

Aturan Asal Angka Nasional:
- Kolom 'asal' / 'asal_angka':
  * 'baris Indonesia': Angka resmi nasional (wilayah_kode 9999) yang diterbitkan langsung oleh BPS dalam data mentah.
    Keenam seri BPS menerbitkan baris 9999 untuk 100% tahun survei, sehingga agregasi sintetik dari tingkat provinsi
    tidak diperlukan (menjaga integritas angka publikasi resmi BPS).
  * 'pembanding': Angka nasional dari publikasi lembaga internasional (WHO GHO dan World Bank WDI).
  * 'agregat': Untuk seri yang tidak menerbitkan baris nasional resmi (di Kasus 17 bernilai 0 karena seluruh seri BPS memiliki baris Indonesia).
- Setiap baris tetap membawa `_berkas_raw` dan `_sha256_raw` untuk penelusuran lineage.
- Tersimpan di `data/gold/tabel_nasional.parquet`, `data/gold/gold_nasional.parquet`, dan `data/gold/tabel_nasional.csv`.
"""
import pandas as pd

from src import konfigurasi as K
from src import wilayah as W
from src.laporan import ROOT, catat, tabel_md, tulis

TABEL_NASIONAL_PARQUET = ROOT / "data" / "gold" / "tabel_nasional.parquet"
GOLD_NASIONAL_PARQUET = ROOT / "data" / "gold" / "gold_nasional.parquet"
REKONSILIASI = ROOT / "data" / "gold" / "rekonsiliasi.parquet"
TABEL_NASIONAL_CSV = ROOT / "data" / "gold" / "tabel_nasional.csv"

SERI_UTAMA = [
    "var845",   # Air Minum Layak (BPS)
    "var2741",  # Air Minum Aman (BPS)
    "var847",   # Sanitasi Layak (BPS)
    "var1273",  # Cuci Tangan (BPS)
    "var2179",  # Sanitasi Aman (BPS)
    "var2749",  # Sanitasi Aman 2024-2025 (BPS)
]

SERI_PEMBANDING = [
    "WSH_WATER_SAFELY_MANAGED",  # WHO GHO
    "WSH_HYGIENE_BASIC",         # WHO GHO
    "SDGODAWS",                  # WHO GHO
    "SH.H2O.SMDW.ZS",            # WDI
    "SH.H2O.BASW.ZS",            # WDI
]

KONSEP_NASIONAL = {
    "var845": "air_layak",
    "var2741": "air_aman",
    "var847": "sanitasi_layak",
    "var1273": "cuci_tangan",
    "var2179": "sanitasi_aman",
    "var2749": "sanitasi_aman",
    "WSH_WATER_SAFELY_MANAGED": "air_aman",
    "WSH_HYGIENE_BASIC": "cuci_tangan_basic",
    "SDGODAWS": "bantuan_air_sanitasi",
    "SH.H2O.SMDW.ZS": "air_aman",
    "SH.H2O.BASW.ZS": "air_layak_basic",
}


def bentuk_tabel_nasional_gold(silver):
    """Membentuk tabel Gold nasional satu baris per periode x seri.

    Menyaring baris nasional (wilayah_kode 9999), rincian 'total', untuk keenam seri utama BPS
    dan kelima seri pembanding WDI/WHO GHO.
    """
    semua_seri = SERI_UTAMA + SERI_PEMBANDING
    mask = (
        (silver["wilayah_kode"] == W.INDONESIA)
        & (silver["seri_kode"].isin(semua_seri))
        & (silver["rincian"] == "total")
    )
    df_nas = silver[mask].copy()

    # Pastikan periode berupa string
    df_nas["periode"] = df_nas["periode"].astype(str)

    # Menentukan kolom asal angka nasional
    def tentukan_asal(row):
        seri = row["seri_kode"]
        sumber = str(row.get("sumber", "")).lower()
        if seri in SERI_UTAMA or sumber == "bps":
            return "baris Indonesia"
        elif seri in SERI_PEMBANDING or sumber in ["who_gho", "wdi"]:
            return "pembanding"
        else:
            return "agregat"

    df_nas["asal"] = df_nas.apply(tentukan_asal, axis=1)
    df_nas["asal_angka"] = df_nas["asal"]

    # Petakan konsep baku
    df_nas["konsep"] = df_nas["seri_kode"].map(KONSEP_NASIONAL).fillna("lainnya")

    # Kolom rapi dan terurut
    kolom_urut = [
        "seri_kode",
        "konsep",
        "wilayah_kode",
        "nama_wilayah",
        "periode",
        "jenis_periode",
        "rincian",
        "nilai",
        "satuan",
        "sdg_kode",
        "sumber",
        "asal",
        "asal_angka",
        "_berkas_raw",
        "_sha256_raw",
    ]
    for col in ["batas_bawah", "batas_atas", "rujukan_tahun"]:
        if col in df_nas.columns and col not in kolom_urut:
            kolom_urut.append(col)

    df_nas = df_nas[[c for c in kolom_urut if c in df_nas.columns]]
    df_nas = df_nas.sort_values(["seri_kode", "periode"]).reset_index(drop=True)

    # Simpan ke data/gold/
    TABEL_NASIONAL_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    df_nas.to_parquet(TABEL_NASIONAL_PARQUET, index=False)
    df_nas.to_parquet(GOLD_NASIONAL_PARQUET, index=False)
    df_nas.to_csv(TABEL_NASIONAL_CSV, index=False)

    print(f"           Gold Nasional: {len(df_nas):,} baris (periode x seri) -> {TABEL_NASIONAL_PARQUET.relative_to(ROOT)}")
    return df_nas


def tabel_nasional(silver):
    nas = silver[silver["wilayah_kode"] == W.INDONESIA].copy()
    nas["kolom"] = nas["seri_kode"] + nas["rincian"].map(lambda r: "" if r == "total" else f" [{r}]")
    total = nas[nas["rincian"] == "total"]
    lebar = total.pivot_table(index="periode", columns="kolom", values="nilai").sort_index()
    return nas, lebar


def irisan(silver, utama, rinci_utama, pembanding, semester=None):
    def per(seri, rinci):
        s = silver[(silver["seri_kode"] == seri) & (silver["rincian"] == rinci) & (silver["wilayah_kode"] == W.INDONESIA)]
        # tahun proyeksi (bukan estimasi atas data) tidak ikut tabel rekonsiliasi
        return set(s["periode"]) - set(getattr(K, "PROYEKSI", {}).get(seri, set()))
    a = per(utama, rinci_utama)
    if semester:
        # seri semesteran dibandingkan dengan seri tahunan lewat satu semester yang ditetapkan (misalnya S1 = Maret)
        a = {p[:4] for p in a if len(p) == 4 or p.endswith(f"-{semester}")}
    return sorted(set.intersection(a, *[per(s, r) for s, r in pembanding])) if pembanding else []


def bentuk_rekonsiliasi(nasional):
    """Satu baris per perbandingan dan periode yang tersedia pada salah satu sisi."""
    bagian = []

    def deret(seri, rincian):
        mask = (nasional["seri_kode"] == seri) & (nasional["rincian"] == rincian)
        return nasional.loc[mask].set_index("periode", verify_integrity=True)["nilai"]

    for p in K.PASANGAN:
        utama = deret(p["utama"], p["rincian_utama"]).rename("nilai_utama")
        for kode, rincian in p["pembanding"] or [(None, None)]:
            pembanding = deret(kode, rincian).rename("nilai_pembanding")
            d = pd.concat([utama, pembanding], axis=1).sort_index()
            d["id_perbandingan"] = f"{p['id']}/{kode}" if kode else p["id"]
            d["pasangan"] = p["id"]
            d["seri_utama"] = p["utama"]
            d["seri_pembanding"] = kode
            d["satuan"] = K.SERI[p["utama"]]["satuan"]
            d["selisih_poin_persen"] = d["nilai_utama"] - d["nilai_pembanding"]
            lengkap = d["selisih_poin_persen"].notna()
            d["status"] = "tanpa pasangan" if kode else "konteks"
            d.loc[lengkap, "status"] = "berpasangan"
            d.loc[lengkap, "kategori"] = p["kategori"]
            d["bukti"] = p["bukti"]
            bagian.append(d.reset_index())
    return pd.concat(bagian, ignore_index=True)


def jalankan(silver):
    nas, lebar = tabel_nasional(silver)
    (ROOT / "reports").mkdir(exist_ok=True)
    lebar.to_csv(ROOT / "reports" / "tabel-nasional.csv")

    # Bentuk tabel Gold Nasional
    df_gold_nas = bentuk_tabel_nasional_gold(silver)

    baris, bagian = [], []
    for p in K.PASANGAN:
        utama = p["utama"].split(",")[0].strip()
        rinci_utama = p.get("rincian_utama", "total")
        bersama = irisan(silver, utama, rinci_utama, p["pembanding"], p.get("semester_utama"))
        baris.append({"id": p["id"], "seri_utama": p["utama"], "pembanding": ", ".join(f"{s} [{r}]" for s, r in p["pembanding"]) or "—",
                      "jenis": p["jenis"], "periode_beririsan": len(bersama), "tahun": ", ".join(bersama) or "—",
                      "dugaan_kategori": p["kategori"]})
        teks = [f"### {p['id']}: {p['judul']}", f"- Seri utama: `{p['utama']}` (rincian `{rinci_utama}`)",
                "- Pembanding: " + (", ".join(f"`{s}` (rincian `{r}`)" for s, r in p["pembanding"]) or "tidak ada di paket"),
                f"- Jenis: **{p['jenis']}**; tahun beririsan: {', '.join(bersama) or '—'}",
                f"- Penjelasan: {p['kategori']}", "", "Pertanyaan keterbandingan dan jawabannya:", ""]
        teks += [f"{i}. **{q}** {a}" for i, (q, a) in enumerate(p["pertanyaan"], 1)]
        teks.append(p["bukti"])
        bagian.append("\n".join(teks))
    rekonsiliasi = bentuk_rekonsiliasi(df_gold_nas)
    rekonsiliasi.to_parquet(REKONSILIASI, index=False)
    daftar = pd.DataFrame(baris)
    n_selisih = int((daftar["jenis"] == "selisih").sum())
    median = float(rekonsiliasi["selisih_poin_persen"].median())
    catat(selisih_median=median, pasangan_rekonsiliasi=n_selisih, pasangan_konteks=int((daftar["jenis"] != "selisih").sum()),
          periode_beririsan=int(daftar.loc[daftar["jenis"] == "selisih", "periode_beririsan"].sum()),
          baris_gold_nasional=len(df_gold_nas),
          seri_gold_nasional=df_gold_nas["seri_kode"].nunique(),
          **{f"irisan_{r.id.lower()}": r.periode_beririsan for r in daftar.itertuples()})
    tulis("pasangan-rekonsiliasi.md", "\n\n".join([
        "# Tabel nasional dan pasangan rekonsiliasi",
        "Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih per pembanding "
        "tersimpan di `data/gold/rekonsiliasi.parquet` (nilai utama dikurangi pembanding, dalam poin persentase).",
        "Tabel nasional Gold (satu baris per periode x seri, dengan kolom asal angka dan _berkas_raw): "
        "`data/gold/tabel_nasional.parquet` dan `data/gold/gold_nasional.parquet`.",
        "Tabel nasional lebar (periode x seri, rincian total): `reports/tabel-nasional.csv`. "
        "Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.",
        f"Seluruh periode pada salah satu sisi dipertahankan. Dari {len(rekonsiliasi)} baris, "
        f"{rekonsiliasi['selisih_poin_persen'].count()} memiliki kedua nilai. Median selisih bertanda "
        f"adalah {median:.4f} poin persentase. Periode tanpa pasangan dan P5 memiliki selisih kosong.",
        "## Ringkasan pasangan", tabel_md(daftar),
        "## Rincian per pasangan", *bagian,
    ]))
    return {"nasional": nas, "nasional_gold": df_gold_nas, "pasangan": daftar}

