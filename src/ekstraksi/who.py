"""Tahap 1 (Ekstraksi): pembaca berkas mentah WHO GHO, kasus 17.

Prinsip: pembaca hanya mengubah berkas mentah menjadi tabel panjang.
Tidak ada baris dibuang atau nilai dibetulkan. Satu-satunya penyaringan ada
pada metadata (Indicator.json dan ddiindicators), yang memuat ribuan
indikator, disaring ke tiga indikator kasus.

"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.common.manifest import sha256_raw

RAW = Path(__file__).resolve().parents[2] / "data" / "raw"
SNAPSHOT = "who_gho/2026-10-20"
KODE_KASUS = {"WSH_WATER_SAFELY_MANAGED", "WSH_HYGIENE_BASIC", "SDGODAWS"}
# UrlName di ddiindicators = IND_UUID di CSV (diambil dari CSV, tidak ditulis tangan)


# util
def _lineage(df: pd.DataFrame, berkas: str) -> pd.DataFrame:
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)  # jangan ditulis tangan
    return df


def _muat_json(berkas: str):
    with open(RAW / berkas, encoding="utf-8") as f:
        isi = json.load(f)
    if isinstance(isi, dict) and isinstance(isi.get("value"), list):
        return isi["value"]  # bentuk OData: {"@odata.context":..., "value":[...]}
    if isinstance(isi, list):
        return isi
    raise ValueError(f"{berkas}: bentuk JSON tak dikenali")


def _skalar(v):
    """Nilai bersarang (list/dict) disimpan sebagai teks JSON, tidak dibuang."""
    return json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v


# pembaca
def baca_data_who(berkas: str):
    """CSV datadot -> tabel panjang. Kembalikan (df, baris_mentah).

    Semua kolom asli dipertahankan apa adanya (teks). Kolom nilai berakhiran
    _N (batas bawah _NL, batas atas _NU bila ada) diseragamkan menjadi
    `nilai_mentah` / `batas_bawah` / `batas_atas`; nama kolom aslinya
    disimpan di `kolom_nilai` supaya skala dan satuannya tidak hilang.
    """
    mentah = pd.read_csv(
        RAW / berkas, dtype=str, keep_default_na=False, encoding="utf-8-sig"
    )
    baris_mentah = len(mentah)

    kol_n = [c for c in mentah.columns if c.endswith("_N")]
    if len(kol_n) != 1:
        raise ValueError(f"{berkas}: kolom nilai _N ditemukan {kol_n}, harus tepat satu")
    kol = kol_n[0]
    dasar = kol[: -len("_N")]

    def angka(nama):
        if nama not in mentah.columns:
            return pd.Series([None] * len(mentah), dtype="float64")
        return pd.to_numeric(mentah[nama].replace("", None), errors="raise")

    df = mentah.drop(columns=[c for c in (kol, dasar + "_NL", dasar + "_NU") if c in mentah.columns])
    df["kolom_nilai"] = kol
    df["nilai_mentah"] = angka(kol).to_numpy()
    df["batas_bawah"] = angka(dasar + "_NL").to_numpy()
    df["batas_atas"] = angka(dasar + "_NU").to_numpy()
    return _lineage(df, berkas), baris_mentah


def baca_indikator_who(berkas: str, kode=KODE_KASUS):
    """odata/Indicator.json (kode + nama), disaring ke kode kasus."""
    rekaman = _muat_json(berkas)
    baris = [
        {
            "IndicatorCode": r.get("IndicatorCode"),
            "IndicatorName": r.get("IndicatorName"),
            "Language": r.get("Language"),
        }
        for r in rekaman
        if r.get("IndicatorCode") in kode
    ]
    return _lineage(pd.DataFrame(baris), berkas), len(rekaman)


def baca_ddi_who(berkas: str, uuid):
    """ddiindicators_*.json (definisi dan metodologi), disaring menurut UrlName.

    Semua field dibawa; field bersarang disimpan sebagai teks JSON.
    """
    rekaman = _muat_json(berkas)
    baris = [
        {k: _skalar(v) for k, v in r.items()}
        for r in rekaman
        if r.get("UrlName") in uuid
    ]
    return _lineage(pd.DataFrame(baris), berkas), len(rekaman)


# semua
def baca_semua_who():
    """Baca seluruh berkas WHO GHO kasus 17.

    Kembalikan (hasil, catatan):
      hasil   : {"data": df, "indikator": df, "ddi": df}
      catatan : daftar dict {berkas, baris_mentah, baris_terbaca}
    """
    dasar = RAW / SNAPSHOT
    berkas = sorted(p.relative_to(RAW).as_posix() for p in dasar.rglob("*") if p.is_file())
    kumpulan = {"data": [], "indikator": [], "ddi": []}
    catatan = []

    # CSV dulu: UUID indikator diambil dari data, dipakai menyaring ddiindicators
    csv_ = [b for b in berkas if b.endswith(".csv")]
    json_ = [b for b in berkas if b.endswith(".json")]
    dikenal = set(csv_) | set(json_)
    if dikenal != set(berkas):
        raise ValueError(f"Berkas WHO tak dikenali: {sorted(set(berkas) - dikenal)}")

    for b in csv_:
        df, mentah = baca_data_who(b)
        kumpulan["data"].append(df)
        catatan.append({"berkas": b, "baris_mentah": mentah, "baris_terbaca": len(df)})
    uuid = set(pd.concat(kumpulan["data"])["IND_UUID"])

    for b in json_:
        nama = Path(b).name
        if nama == "Indicator.json":
            df, mentah = baca_indikator_who(b)
            kumpulan["indikator"].append(df)
        elif nama.startswith("ddiindicators"):
            df, mentah = baca_ddi_who(b, uuid)
            kumpulan["ddi"].append(df)
        else:
            raise ValueError(f"Berkas JSON WHO tak dikenali pembaca: {b}")
        catatan.append({"berkas": b, "baris_mentah": mentah, "baris_terbaca": len(df)})

    hasil = {k: pd.concat(v, ignore_index=True) for k, v in kumpulan.items() if v}
    return hasil, catatan


if __name__ == "__main__":
    hasil, catatan = baca_semua_who()
    print(f"{'berkas':72} {'mentah':>8} {'terbaca':>8}")
    for c in catatan:
        print(f"{c['berkas']:72} {c['baris_mentah']:>8} {c['baris_terbaca']:>8}")
    print()
    print("berkas_dibaca =", len(catatan))
    print("baris_mentah  =", sum(c["baris_mentah"] for c in catatan))
    d = hasil["data"]
    print("\nPengamatan per indikator:")
    print(d.groupby(["IND_CODE", "kolom_nilai"]).agg(
        baris=("nilai_mentah", "size"),
        null=("nilai_mentah", lambda s: s.isna().sum()),
        tahun_min=("DIM_TIME", "min"),
        tahun_maks=("DIM_TIME", "max"),
    ))
    assert d["_berkas_raw"].notna().all() and d["_sha256_raw"].notna().all()
    print("\nLineage lengkap di semua baris data: OK")