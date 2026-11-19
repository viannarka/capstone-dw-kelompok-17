"""CSV DATADOT tetap per berkas agar kolom nilai, batas, dan dimensi asli terjaga."""
import json

import pandas as pd

from src.common.manifest import RAW
from src.ekstraksi import lineage


KODE_KASUS = {"WSH_WATER_SAFELY_MANAGED", "WSH_HYGIENE_BASIC", "SDGODAWS"}


def baca_csv(berkas):
    df = pd.read_csv(RAW / berkas, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    return lineage(df, berkas)


def kolom_nilai(df):
    pilihan = [c for c in df if c.endswith("_N") and not c.startswith(("DIM_", "IND_", "GEO_"))]
    if len(pilihan) != 1:
        raise ValueError(f"Kolom nilai WHO tidak tunggal: {pilihan}")
    nilai, = pilihan
    dasar = nilai[:-2]
    return {"nilai": nilai, "bawah": dasar + "_NL" if dasar + "_NL" in df else None,
            "atas": dasar + "_NU" if dasar + "_NU" in df else None,
            "penyebut": int(dasar.removeprefix("RATE_PER_")) if dasar.startswith("RATE_PER_") else None}


def _rekaman(berkas):
    with (RAW / berkas).open(encoding="utf-8-sig") as f:
        isi = json.load(f)
    if isinstance(isi, dict):
        isi = isi.get("value")
    if not isinstance(isi, list):
        raise ValueError(f"Bentuk metadata WHO tidak dikenali: {berkas}")
    return isi


def baca_metadata_odata(berkas, seri=KODE_KASUS, *, dengan_jumlah=False):
    data = _rekaman(berkas)
    rows = [r for r in data if r.get("IndicatorCode") in seri]
    df = lineage(pd.DataFrame(rows), berkas)
    return (df, len(data)) if dengan_jumlah else df


def baca_metadata_ddi(berkas, seri=KODE_KASUS, *, dengan_jumlah=False):
    data = _rekaman(berkas)
    rows = []
    for r in data:
        konfigurasi = json.loads(r.get("DataVisualizationConfiguration") or "{}")
        kode = konfigurasi.get("indicator") or r.get("AlternativeCodes")
        if kode in seri:
            rows.append({"seri_kode": kode, **{
                k: v for k, v in r.items() if isinstance(v, (str, int, float))
            }})
    df = lineage(pd.DataFrame(rows), berkas)
    return (df, len(data)) if dengan_jumlah else df


def main():
    from src.ekstraksi import jalankan
    print(jalankan("who_gho")["_hitung"].to_string(index=False))


if __name__ == "__main__":
    main()
