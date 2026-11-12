"""Tahap 1 (Ekstraksi): pembaca berkas mentah WDI (World Bank), kasus 17.

Prinsip: pembaca hanya mengubah JSON mentah menjadi tabel panjang.
Tidak ada nilai yang dibuang, dibetulkan, atau ditafsirkan, kecuali
penyaringan ke seri kasus lewat `indicator.id` (sesuai tugas).
Baris bernilai null TETAP dibawa; keputusan membuangnya ada di tahap Silver.

"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.common.manifest import sha256_raw

RAW = Path(__file__).resolve().parents[2] / "data" / "raw"
SNAPSHOT = "wdi/2026-10-20"
SERI_KASUS = {"SH.H2O.SMDW.ZS", "SH.H2O.BASW.ZS"}


# util
def _muat(berkas: str):
    """Baca JSON mentah. Kembalikan (metadata_halaman | None, daftar_isi)."""
    with open(RAW / berkas, encoding="utf-8") as f:
        isi = json.load(f)
    # Bentuk WDI API: [ {page, pages, per_page, total, ...}, [ ...rekaman... ] ]
    if (
        isinstance(isi, list)
        and len(isi) == 2
        and isinstance(isi[0], dict)
        and isinstance(isi[1], list)
    ):
        return isi[0], isi[1]
    if isinstance(isi, list):
        return None, isi
    raise ValueError(f"{berkas}: bentuk JSON tak dikenali ({type(isi).__name__})")


def _ambil(d: dict, *kunci):
    """Ambil d[k1][k2]... ; None bila ada yang hilang."""
    for k in kunci:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def _lineage(df: pd.DataFrame, berkas: str) -> pd.DataFrame:
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)  # jangan ditulis tangan
    return df


# pembaca
def baca_data_wdi(berkas: str, seri=SERI_KASUS):
    """Pengamatan WDI -> tabel panjang. Kembalikan (df, baris_mentah)."""
    _, rekaman = _muat(berkas)
    baris_mentah = len(rekaman)
    baris = []
    for r in rekaman:
        kode = _ambil(r, "indicator", "id")
        if seri is not None and kode not in seri:
            continue
        baris.append(
            {
                "indikator_id": kode,
                "indikator_nama": _ambil(r, "indicator", "value"),
                "negara_id": _ambil(r, "country", "id"),
                "negara_nama": _ambil(r, "country", "value"),
                "negara_iso3": r.get("countryiso3code"),
                "tahun_mentah": r.get("date"),  # apa adanya (teks)
                "nilai_mentah": r.get("value"),  # None = tak ada pengamatan
                "unit_mentah": r.get("unit"),
                "scale_mentah": r.get("scale"),  # tidak ada di semua rekaman
                "obs_status": r.get("obs_status"),
                "decimal": r.get("decimal"),
            }
        )
    df = pd.DataFrame(baris)
    if df.empty:
        raise ValueError(f"{berkas}: tidak ada baris untuk seri {sorted(seri)}")
    return _lineage(df, berkas), baris_mentah


def baca_indikator_wdi(berkas: str, seri=SERI_KASUS):
    """Metadata indikator (disaring menurut `id`). Kembalikan (df, baris_mentah)."""
    _, rekaman = _muat(berkas)
    baris_mentah = len(rekaman)
    baris = []
    for r in rekaman:
        if seri is not None and r.get("id") not in seri:
            continue
        baris.append(
            {
                "indikator_id": r.get("id"),
                "indikator_nama": r.get("name"),
                "unit": r.get("unit"),
                "sumber_id": _ambil(r, "source", "id"),
                "sumber_nama": _ambil(r, "source", "value"),
                "sumber_catatan": r.get("sourceNote"),
                "sumber_organisasi": r.get("sourceOrganization"),
                "topik": json.dumps(r.get("topics"), ensure_ascii=False),
            }
        )
    return _lineage(pd.DataFrame(baris), berkas), baris_mentah


def baca_sumber_wdi(berkas: str):
    """Katalog sumber WDI, tanpa penyaringan. Kembalikan (df, baris_mentah)."""
    _, rekaman = _muat(berkas)
    df = pd.json_normalize(rekaman)
    return _lineage(df, berkas), len(rekaman)


#  semua
def baca_semua_wdi():
    """Baca seluruh berkas WDI kasus 17.

    Kembalikan (hasil, catatan):
      hasil   : {"data": df, "indikator": df, "sumber": df}
      catatan : daftar dict {berkas, baris_mentah, baris_terbaca}
                -> salin ke komentar tugas dan ke metrics.json
    """
    berkas_json = sorted(
        p.relative_to(RAW).as_posix() for p in (RAW / SNAPSHOT).rglob("*.json")
    )
    kumpulan = {"data": [], "indikator": [], "sumber": []}
    catatan = []

    for b in berkas_json:
        nama = Path(b).name
        if "/data/" in b:
            df, mentah = baca_data_wdi(b)
            jenis = "data"
        elif nama.endswith("_indikator.json"):
            df, mentah = baca_indikator_wdi(b)
            jenis = "indikator"
        elif nama == "sumber.json":
            df, mentah = baca_sumber_wdi(b)
            jenis = "sumber"
        else:
            raise ValueError(f"Berkas WDI tak dikenali pembaca: {b}")
        kumpulan[jenis].append(df)
        catatan.append({"berkas": b, "baris_mentah": mentah, "baris_terbaca": len(df)})

    hasil = {k: pd.concat(v, ignore_index=True) for k, v in kumpulan.items() if v}
    return hasil, catatan


if __name__ == "__main__":
    hasil, catatan = baca_semua_wdi()
    print(f"{'berkas':70} {'mentah':>8} {'terbaca':>8}")
    for c in catatan:
        print(f"{c['berkas']:70} {c['baris_mentah']:>8} {c['baris_terbaca']:>8}")
    print()
    print("berkas_dibaca =", len(catatan))
    print("baris_mentah  =", sum(c["baris_mentah"] for c in catatan))
    d = hasil["data"]
    print("\nPengamatan per indikator (termasuk nilai null):")
    print(d.groupby("indikator_id").agg(
        baris=("nilai_mentah", "size"),
        null=("nilai_mentah", lambda s: s.isna().sum()),
        tahun_min=("tahun_mentah", "min"),
        tahun_maks=("tahun_mentah", "max"),
    ))
    assert d["_berkas_raw"].notna().all() and d["_sha256_raw"].notna().all()
    print("\nLineage lengkap di semua baris data: OK")