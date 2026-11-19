"""Aturan validasi khas Kasus 17 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import re

import pandas as pd

from src import konfigurasi as K


def tujuan_sdg_sesuai_nama_berkas(silver):
    """Tujuan SDG (angka sebelum titik pertama) setiap seri BPS sama dengan angka di nama berkasnya (sdg6_...)."""
    b = silver[silver["sumber"] == "bps"].drop_duplicates(["seri_kode", "_berkas_raw"])
    buruk = []
    for r in b.to_dict("records"):
        m = re.search(r"/sdg(\d+)_", "/" + r["_berkas_raw"].split("/")[-1])
        if m and r["sdg_kode"].split(".")[0] != m.group(1):
            buruk.append({"seri_kode": r["seri_kode"], "sdg_kode": r["sdg_kode"], "berkas": r["_berkas_raw"]})
    return pd.DataFrame(buruk)


def dua_tabel_sanitasi_aman_sama(silver):
    """var2749 dan var2179 (rincian total) bernilai sama pada wilayah dan tahun yang sama-sama ada."""
    a = silver[(silver["seri_kode"] == "var2179") & (silver["rincian"] == "total")].set_index(["wilayah_kode", "periode"])["nilai"]
    b = silver[silver["seri_kode"] == "var2749"].set_index(["wilayah_kode", "periode"])["nilai"]
    g = pd.DataFrame({"var2179": a, "var2749": b}).dropna()
    return g[(g["var2179"] - g["var2749"]).abs() > 0.005].reset_index()


def total_di_antara_kota_desa(silver):
    """Sanitasi aman gabungan berada di antara perkotaan dan perdesaan (toleransi 0,05 poin)."""
    s = silver[silver["seri_kode"] == "var2179"]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    lo = lebar[["daerah=URBAN", "daerah=RURAL"]].min(axis=1) - 0.05
    hi = lebar[["daerah=URBAN", "daerah=RURAL"]].max(axis=1) + 0.05
    return lebar[(lebar["total"] < lo) | (lebar["total"] > hi)].reset_index()


def kota_tidak_lebih_rendah(silver):
    """Peringatan: sanitasi aman perkotaan lebih rendah dari perdesaan."""
    s = silver[silver["seri_kode"] == "var2179"]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    return lebar[lebar["daerah=URBAN"] < lebar["daerah=RURAL"]].reset_index()


ATURAN = [
    ("tujuan_sdg_sesuai_nama_berkas", "tujuan SDG setiap seri BPS sama dengan angka di nama berkasnya (sdgN_)", True,
     tujuan_sdg_sesuai_nama_berkas),
    ("dua_tabel_sanitasi_aman_sama", "var2749 = var2179 gabungan pada sel yang sama", True, dua_tabel_sanitasi_aman_sama),
    ("total_di_antara_kota_desa", "sanitasi aman gabungan di antara perkotaan dan perdesaan", True, total_di_antara_kota_desa),
    ("kota_tidak_lebih_rendah", "sanitasi aman perkotaan < perdesaan (peringatan)", False, kota_tidak_lebih_rendah),
]
