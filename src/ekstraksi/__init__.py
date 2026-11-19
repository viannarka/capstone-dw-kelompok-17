"""Ekstraksi Kasus 17. Setiap kunci hasil mewakili satu format dan peran sumber."""
from collections import defaultdict
from fnmatch import fnmatch

import pandas as pd

from src.common.manifest import baca, periksa, sha256_raw


def lineage(df, berkas):
    df["_berkas_raw"] = berkas
    df["_sha256_raw"] = sha256_raw(berkas)
    return df


def jalankan(sumber=None, *, laporan_berkas=None):
    """Baca berkas MANIFEST, pertahankan tabel per jenis dan CSV WHO per jalur."""
    from src.ekstraksi import bps, wdi, who_gho

    _, salah = periksa()
    if salah:
        raise ValueError(f"Berkas tidak cocok dengan manifest: {salah}")
    manifest = baca()
    berkas_sumber = [b for b in manifest if sumber is None or b.startswith(sumber + "/")]
    if not berkas_sumber:
        raise ValueError(f"Sumber tidak ditemukan: {sumber}")

    kumpulan = defaultdict(list)
    who_csv = {}
    hitung = []
    for berkas in berkas_sumber:
        catatan = ""
        jumlah = None
        if fnmatch(berkas, "bps/*/json/*.json"):
            nama = "bps_json"
            df, meta = bps.baca_json(berkas)
            kumpulan["bps_meta"].append(meta)
            catatan = f"{meta['_halaman'].nunique()} halaman"
        elif fnmatch(berkas, "bps/*/manifest_asal.json"):
            nama = "bps_manifest_asal"
            df = bps.baca_manifest_asal(berkas)
            catatan = "semua tabel unduhan BPS, bukan hanya kasus ini"
        elif fnmatch(berkas, "bps/*/*.csv"):
            nama = "bps_csv"
            df, jumlah = bps.baca_csv(berkas, dengan_jumlah=True)
        elif fnmatch(berkas, "wdi/*/data/*.json"):
            nama = "wdi_data"
            df, jumlah = wdi.baca_data(berkas)
            catatan = f"{jumlah:,} baris di berkas, {df['indicator_id'].nunique()} seri kasus disaring"
        elif fnmatch(berkas, "wdi/*/metadata/*_indikator.json"):
            nama = "wdi_meta"
            df, jumlah = wdi.baca_metadata(berkas, wdi.SERI_KASUS, dengan_jumlah=True)
            catatan = "metadata seri kasus saja"
        elif fnmatch(berkas, "wdi/*/metadata/sumber.json"):
            nama = "wdi_sumber"
            df, jumlah = wdi.baca_metadata(berkas, dengan_jumlah=True)
        elif fnmatch(berkas, "who_gho/*/datadot/*.csv"):
            nama = "who_csv"
            df = who_gho.baca_csv(berkas)
            who_csv[berkas] = df
        elif fnmatch(berkas, "who_gho/*/datadot/ddiindicators*.json"):
            nama = "who_ddi"
            df, jumlah = who_gho.baca_metadata_ddi(berkas, dengan_jumlah=True)
            catatan = "definisi lengkap seri kasus"
        elif fnmatch(berkas, "who_gho/*/odata/Indicator.json"):
            nama = "who_odata"
            df, jumlah = who_gho.baca_metadata_odata(berkas, dengan_jumlah=True)
        else:
            raise ValueError(f"Berkas manifest tanpa pembaca: {berkas}")

        if df.empty:
            raise ValueError(f"Berkas tidak menghasilkan baris kasus: {berkas}")
        if not (df["_berkas_raw"].eq(berkas) & df["_sha256_raw"].eq(manifest[berkas])).all():
            raise ValueError(f"Lineage tidak lengkap: {berkas}")
        if nama != "who_csv":
            kumpulan[nama].append(df)
        peran = "data" if nama in {"bps_json", "bps_csv", "wdi_data", "who_csv"} else "meta"
        if jumlah is None:
            jumlah = len(df)
        hitung.append(dict(berkas=berkas, pembaca=nama, peran=peran, baris=len(df),
                           catatan=catatan, baris_mentah=jumlah))
    hasil = {nama: pd.concat(tabel, ignore_index=True) for nama, tabel in kumpulan.items()}
    if who_csv:
        hasil["who_csv"] = who_csv
    hitungan = pd.DataFrame(hitung)
    if laporan_berkas is not None:
        catatan_tim = hitungan.rename(columns={"baris": "baris_terbaca"})
        catatan_tim.sort_values("berkas").to_csv(
            laporan_berkas, index=False, columns=["berkas", "baris_mentah", "baris_terbaca"])
    ringkasan = hitungan.drop(columns="baris_mentah")
    hasil["_hitung"] = ringkasan
    observasi = ringkasan.loc[ringkasan["peran"].eq("data"), "baris"].sum()
    print(f"Ekstraksi: {len(ringkasan)}/{len(berkas_sumber)} berkas, {observasi} baris data; manifest dan lineage sesuai.")
    return hasil
