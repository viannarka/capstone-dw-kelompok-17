import json
import re
from itertools import product
from pathlib import Path

import pandas as pd

from src.common.manifest import RAW, sha256_raw


FOLDER_BPS = RAW / "bps" / "2026-10-17"


def tambah_asal(df, path):
    """Menambahkan asal berkas dan SHA-256 dari manifest."""
    berkas = path.relative_to(RAW).as_posix()
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)
    return df


def baca_csv(path):
    """Membaca CSV tanpa membersihkan nilai aslinya."""
    for encoding in ["utf-8-sig", "cp1252", "latin-1"]:
        try:
            df = pd.read_csv(
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
        raise ValueError(f"Encoding CSV tidak terbaca: {path}")

    # Kolom tahun yang melebar diubah menjadi tabel panjang.
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

    return tambah_asal(df, path)


def baca_json(path):
    """Membaca JSON BPS dan meratakan datacontent."""
    with open(path, encoding="utf-8-sig") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    semua_baris = []

    for bagian in data:
        dimensi = [
            "vervar", "var", "turvar",
            "tahun", "turtahun"
        ]

        daftar_dimensi = [
            bagian.get(nama, []) for nama in dimensi
        ]

        # Menyusun pasangan kode gabungan dan label.
        peta = {}

        if all(daftar_dimensi):
            for kombinasi in product(*daftar_dimensi):
                kode = "".join(
                    str(item["val"]) for item in kombinasi
                )
                peta[kode] = {
                    nama + "_kode": item["val"]
                    for nama, item in zip(dimensi, kombinasi)
                }
                peta[kode].update({
                    nama + "_label": item.get("label")
                    for nama, item in zip(dimensi, kombinasi)
                })

        for kode, nilai in bagian.get("datacontent", {}).items():
            baris = {
                "_kode_datacontent": str(kode),
                "nilai": nilai,
            }

            # Pertahankan kode asli jika tidak cocok.
            baris.update(peta.get(str(kode), {}))
            semua_baris.append(baris)

    df = pd.DataFrame(semua_baris)
    return tambah_asal(df, path)


def jalankan():
    """Membaca seluruh CSV dan JSON BPS."""
    hasil = []

def jalankan():
    hasil = []

    for path in sorted(FOLDER_BPS.rglob("*")):
        if not path.is_file():
            continue

        if path.name == "manifest_asal.json":
            continue

        if path.suffix.lower() == ".csv":
            df = baca_csv(path)
        elif path.suffix.lower() == ".json":
            df = baca_json(path)
        else:
            continue

        print(f"{path.name}: {len(df)} baris")
        hasil.append(df)

    if not hasil:
        raise FileNotFoundError(
            "Tidak ada berkas CSV atau JSON BPS."
        )

    gabungan = pd.concat(hasil, ignore_index=True)
    print(f"Total: {len(gabungan)} baris")
    return gabungan


if __name__ == "__main__":
    data = jalankan()

    print("\nHASIL PEMERIKSAAN")
    print("Total baris:", len(data))
    print("Jumlah berkas:", data["_berkas_raw"].nunique())
    print("Kolom asal lengkap:",
          data["_berkas_raw"].notna().all()
          and data["_sha256_raw"].notna().all())

    print("\nJUMLAH BARIS PER BERKAS:")
    print(data.groupby("_berkas_raw").size().to_string())

def periksa_kecocokan():
    from pandas.testing import assert_frame_equal

    for nama in [
        "sdg6_6_1_1_v2741",
        "sdg6_6_2_1_v2749",
        "sdg6_air_layak",
        "sdg6_cuci_tangan",
        "sdg6_sanitasi_aman",
        "sdg6_sanitasi_layak",
    ]:
        csv = baca_csv(FOLDER_BPS / f"{nama}.csv")
        js = baca_json(FOLDER_BPS / "json" / f"{nama}.json")

        a = csv[["wilayah_id", "tahun_id", "turvar_id", "nilai"]].copy()
        b = js[["vervar_kode", "tahun_kode", "turvar_kode", "nilai"]].copy()

        a.columns = ["wilayah", "tahun", "rincian", "nilai"]
        b.columns = ["wilayah", "tahun", "rincian", "nilai"]

        a = a.astype(str).sort_values(list(a.columns)).reset_index(drop=True)
        b = b.astype(str).sort_values(list(b.columns)).reset_index(drop=True)

        try:
            assert_frame_equal(a, b, check_dtype=False)
            print(f"{nama}: COCOK ({len(a)} baris)")
        except AssertionError:
            print(f"{nama}: BELUM COCOK — perlu diperiksa")