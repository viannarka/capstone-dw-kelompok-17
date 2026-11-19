"""Pembaca pengamatan, metadata indikator, dan katalog sumber World Bank WDI."""
import json

import pandas as pd

from src.common.manifest import RAW
from src.ekstraksi import lineage


SERI_KASUS = {"SH.H2O.SMDW.ZS", "SH.H2O.BASW.ZS"}


def _muat(berkas):
    with (RAW / berkas).open(encoding="utf-8-sig") as f:
        isi = json.load(f)
    if isinstance(isi, list) and len(isi) == 2 and isinstance(isi[0], dict) and "page" in isi[0]:
        ket, baris = isi
        if int(ket.get("pages", 1)) != 1:
            raise ValueError(f"{berkas}: snapshot WDI mencakup lebih dari satu halaman")
        if baris is None or isinstance(baris, list):
            return ket, baris or []
    elif isinstance(isi, list):
        return {}, isi
    raise ValueError(f"{berkas}: bentuk JSON WDI tidak dikenali")


def baca_data(berkas, seri=SERI_KASUS):
    ket, rekaman = _muat(berkas)
    data = []
    for r in rekaman:
        kode = r["indicator"]["id"]
        if seri is None or kode in seri:
            data.append({
                "indicator_id": kode, "indicator_nama": r["indicator"]["value"],
                "country_id": r["country"]["id"], "countryiso3code": r.get("countryiso3code"),
                "date": r["date"], "value": r["value"], "unit": r.get("unit"),
                "obs_status": r.get("obs_status"), "decimal": r.get("decimal"),
            })
    if not data:
        raise ValueError(f"{berkas}: tidak ada pengamatan untuk seri kasus")
    df = pd.DataFrame(data)
    df["_lastupdated"] = ket.get("lastupdated")
    return lineage(df, berkas), len(rekaman)


def baca_metadata(berkas, seri=None, *, dengan_jumlah=False):
    _, rekaman = _muat(berkas)
    data = []
    for r in rekaman:
        if seri is not None and r.get("id") not in seri:
            continue
        baris = {}
        for k, v in r.items():
            if isinstance(v, dict):
                v = v.get("value")
            elif isinstance(v, list):
                v = json.dumps(v, ensure_ascii=False)
            baris[k] = v
        data.append(baris)
    df = lineage(pd.DataFrame(data), berkas)
    return (df, len(rekaman)) if dengan_jumlah else df


if __name__ == "__main__":
    from src.ekstraksi import jalankan

    hasil = jalankan("wdi")
    print(hasil["_hitung"].to_string(index=False))
    print(hasil["wdi_data"].groupby("indicator_id").agg(
        baris=("value", "size"), terisi=("value", "count"), awal=("date", "min"), akhir=("date", "max")))
