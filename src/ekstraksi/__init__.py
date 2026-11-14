"""Tahap 1 — Ekstraksi (pertemuan X). Milik tim.

Nilai asli tidak dibersihkan. Lineage setiap baris tetap dipertahankan.
"""
import json

import pandas as pd

from src.common.manifest import RAW, baca, periksa, sha256_raw
from src.ekstraksi.bps import baca_semua_bps
from src.ekstraksi.who import baca_semua_who
from src.ekstraksi.wdi import baca_semua_wdi


# membaca metadata BPS
def baca_metadata_bps():
    berkas = "bps/2026-10-17/manifest_asal.json"

    with open(RAW / berkas, encoding="utf-8-sig") as f:
        isi = json.load(f)

    if not isinstance(isi, dict) or not isinstance(isi.get("tabel"), dict):
        raise ValueError("Format metadata BPS tidak dikenali")

    baris = []

    for nama, rincian in isi["tabel"].items():
        baris.append({
            "nama_tabel": nama,
            "detail_tabel": json.dumps(rincian, ensure_ascii=False),
            "sumber": isi.get("sumber"),
            "domain": isi.get("domain"),
            "diunduh": isi.get("diunduh"),
            "skrip": isi.get("skrip"),
        })

    if not baris:
        raise ValueError("Metadata BPS kosong")

    df = pd.DataFrame(baris)
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)

    return df


# menggabungkan semua pembaca
def jalankan():
    """Kembalikan {nama_sumber: DataFrame mentah}."""

    jumlah, salah = periksa()

    if salah:
        raise ValueError(
            f"Ada {len(salah)} berkas yang tidak cocok dengan manifest"
        )

    hasil_bps, catatan_bps = baca_semua_bps()
    hasil_who, catatan_who = baca_semua_who()
    hasil_wdi, catatan_wdi = baca_semua_wdi()

    kumpulan = []

    for sumber, hasil in (
        ("bps", hasil_bps),
        ("who", hasil_who),
        ("wdi", hasil_wdi),
    ):
        for jenis, df in hasil.items():

            if not isinstance(df, pd.DataFrame):
                raise TypeError(f"{sumber}/{jenis}: bukan DataFrame")

            if not {"_berkas_raw", "_sha256_raw"}.issubset(df.columns):
                raise ValueError(f"{sumber}/{jenis}: lineage belum lengkap")

            bagian = df.copy()
            bagian["_sumber_data"] = sumber
            bagian["_jenis_data"] = jenis

            kumpulan.append(bagian)

    metadata_bps = baca_metadata_bps()
    metadata_bps["_sumber_data"] = "bps"
    metadata_bps["_jenis_data"] = "metadata"

    kumpulan.append(metadata_bps)

    mentah = pd.concat(kumpulan, ignore_index=True, sort=False)

    # mencocokkan file dengan manifest
    manifest = baca()
    terbaca = set(mentah["_berkas_raw"].dropna().unique())
    terdaftar = set(manifest)

    if terbaca != terdaftar:
        raise ValueError(
            f"Berkas terlewat: {sorted(terdaftar - terbaca)}; "
            f"berkas tidak dikenal: {sorted(terbaca - terdaftar)}"
        )

    # memeriksa kelengkapan lineage
    if mentah["_berkas_raw"].isna().any():
        raise ValueError("Ada baris tanpa asal berkas")

    if mentah["_sha256_raw"].isna().any():
        raise ValueError("Ada baris tanpa SHA-256")

    if not (
        mentah["_sha256_raw"]
        == mentah["_berkas_raw"].map(manifest)
    ).all():
        raise ValueError("SHA-256 tidak sesuai manifest")

    print(
        f"Ekstraksi: {len(terbaca)}/{jumlah} berkas, "
        f"{len(mentah)} baris terbaca"
    )
    print("Semua berkas sesuai manifest dan lineage lengkap")

    return {"mentah": mentah}
