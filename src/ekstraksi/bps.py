"""Tahap 1 (Ekstraksi): pembaca berkas mentah BPS, kasus 17.

Prinsip: pembaca hanya mengubah berkas mentah CSV dan JSON BPS
menjadi tabel panjang. Tidak ada baris dibuang atau nilai dibetulkan.
Setiap baris diberi informasi asal berkas dan SHA-256 dari manifest.

Seri BPS: var845, var2741, var847, var1273, var2179, var2749.
"""

from __future__ import annotations

import json
import re
from itertools import product
from pathlib import Path

import pandas as pd

from src.common.manifest import sha256_raw


RAW = Path(__file__).resolve().parents[2] / "data" / "raw"
SNAPSHOT = "bps/2026-10-17"


# util
def lineage(df: pd.DataFrame, berkas: str) -> pd.DataFrame:
    """Menambahkan asal berkas dan SHA-256 pada setiap baris."""
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)
    return df


# pembaca
def baca_csv_bps(berkas: str):
    """Membaca CSV BPS dan mengembalikan (df, baris_mentah)."""
    path = RAW / berkas

    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            mentah = pd.read_csv(
                path,
                sep=None,
                engine="python",
                encoding=encoding,
                dtype=str,
                keep_default_na=False,
            )
            break
        except UnicodeError:
            continue
    else:
        raise ValueError(f"{berkas}: pengodean CSV tidak dikenali")

    baris_mentah = len(mentah)
    df = mentah.copy()

    # Jika tahun masih berupa kolom, ubah menjadi tabel panjang.
    kolom_tahun = [
        kolom for kolom in df.columns
        if re.fullmatch(r"(19|20)\d{2}", str(kolom).strip())
    ]

    if kolom_tahun:
        kolom_lain = [
            kolom for kolom in df.columns
            if kolom not in kolom_tahun
        ]
        df = df.melt(
            id_vars=kolom_lain,
            value_vars=kolom_tahun,
            var_name="tahun",
            value_name="nilai",
        )

    return lineage(df, berkas), baris_mentah


def baca_json_bps(berkas: str):
    """Membaca JSON WebAPI BPS dengan struktur bersarang.

    Dimensi vervar, var, turvar, tahun, dan turtahun
    digunakan untuk membaca kode pada datacontent.
    """
    with open(RAW / berkas, encoding="utf-8-sig") as f:
        isi = json.load(f)

    if isinstance(isi, dict):
        isi = [isi]

    if not isinstance(isi, list):
        raise ValueError(f"{berkas}: bentuk JSON tidak dikenali")

    semua_baris = []
    baris_mentah = 0

    for bagian in isi:
        dimensi = ["vervar", "var", "turvar", "tahun", "turtahun"]
        daftar_dimensi = [
            bagian.get(nama, []) for nama in dimensi
        ]

        if not all(daftar_dimensi):
            raise ValueError(
                f"{berkas}: ada dimensi BPS yang tidak tersedia"
            )

        # Membuat peta kode datacontent ke label dimensi.
        peta = {}

        for kombinasi in product(*daftar_dimensi):
            kode = "".join(str(item["val"]) for item in kombinasi)

            peta[kode] = {}

            for nama, item in zip(dimensi, kombinasi):
                peta[kode][nama + "_kode"] = item["val"]
                peta[kode][nama + "_label"] = item.get("label")

        datacontent = bagian.get("datacontent", {})
        baris_mentah += len(datacontent)

        for kode, nilai in datacontent.items():
            kode = str(kode)

            if kode not in peta:
                raise ValueError(
                    f"{berkas}: kode datacontent {kode} tidak terpetakan"
                )

            baris = {
                "_kode_datacontent": kode,
                "nilai": nilai,
            }
            baris.update(peta[kode])
            semua_baris.append(baris)

    df = pd.DataFrame(semua_baris)

    return lineage(df, berkas), baris_mentah


# pembacaan seluruh berkas BPS
def baca_semua_bps():
    """Membaca seluruh berkas BPS kasus 17.

    Kembalikan (hasil, catatan):
      hasil   : {"data": DataFrame}
      catatan : daftar dict berisi
                berkas, baris_mentah, baris_terbaca
    """
    dasar = RAW / SNAPSHOT

    berkas = sorted(
        p.relative_to(RAW).as_posix()
        for p in dasar.rglob("*")
        if p.is_file() and p.name != "manifest_asal.json"
    )

    kumpulan = []
    catatan = []

    for b in berkas:
        if b.endswith(".csv"):
            df, mentah = baca_csv_bps(b)

        elif b.endswith(".json"):
            df, mentah = baca_json_bps(b)

        else:
            raise ValueError(f"Berkas BPS tidak dikenali: {b}")

        kumpulan.append(df)

        catatan.append({
            "berkas": b,
            "baris_mentah": mentah,
            "baris_terbaca": len(df),
        })

    if not kumpulan:
        raise FileNotFoundError("Tidak ada berkas BPS yang ditemukan")

    data = pd.concat(kumpulan, ignore_index=True)

    assert data["_berkas_raw"].notna().all()
    assert data["_sha256_raw"].notna().all()

    hasil = {"data": data}

    return hasil, catatan


def hasil_bps():
    """Mengembalikan DataFrame BPS untuk integrasi tim."""
    hasil, catatan = baca_semua_bps()
    return hasil["data"]


# pengujian
def periksa_kecocokan():
    """Memeriksa kecocokan enam pasangan CSV dan JSON BPS."""
    dasar = RAW / SNAPSHOT

    for csv_path in sorted(dasar.glob("*.csv")):
        json_path = dasar / "json" / (csv_path.stem + ".json")

        if not json_path.exists():
            raise FileNotFoundError(json_path)

        csv_berkas = csv_path.relative_to(RAW).as_posix()
        json_berkas = json_path.relative_to(RAW).as_posix()

        csv_df, _ = baca_csv_bps(csv_berkas)
        json_df, _ = baca_json_bps(json_berkas)

        a = csv_df[
            ["wilayah_id", "tahun_id", "turvar_id", "nilai"]
        ].copy()

        b = json_df[
            ["vervar_kode", "tahun_kode", "turvar_kode", "nilai"]
        ].copy()

        a.columns = ["wilayah", "tahun", "rincian", "nilai"]
        b.columns = ["wilayah", "tahun", "rincian", "nilai"]

        a = (
            a.astype(str)
            .sort_values(list(a.columns))
            .reset_index(drop=True)
        )
        b = (
            b.astype(str)
            .sort_values(list(b.columns))
            .reset_index(drop=True)
        )

        pd.testing.assert_frame_equal(a, b, check_dtype=False)
        print(f"{csv_path.stem}: COCOK ({len(a)} baris)")


if __name__ == "__main__":
    hasil, catatan = baca_semua_bps()

    print(f"{'berkas':65} {'mentah':>8} {'terbaca':>8}")

    for c in catatan:
        print(
            f"{c['berkas']:65} "
            f"{c['baris_mentah']:>8} "
            f"{c['baris_terbaca']:>8}"
        )

    print()
    print("berkas_dibaca =", len(catatan))
    print("baris_mentah  =", sum(
        c["baris_mentah"] for c in catatan
    ))
    print("baris_terbaca =", len(hasil["data"]))

    d = hasil["data"]

    assert d["_berkas_raw"].notna().all()
    assert d["_sha256_raw"].notna().all()

    print("\nLineage lengkap di semua baris data: OK")

    print("\nPemeriksaan kecocokan CSV dan JSON:")
    periksa_kecocokan()