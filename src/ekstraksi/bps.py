"""Pembaca BPS untuk Kasus 17. Observasi CSV, observasi JSON, dan metadata terpisah."""
import json
import re
from itertools import product

import pandas as pd

from src.common.manifest import RAW
from src.ekstraksi import lineage


def baca_csv(berkas, *, dengan_jumlah=False):
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            df = pd.read_csv(RAW / berkas, sep=None, engine="python", encoding=encoding,
                             dtype=str, keep_default_na=False)
            break
        except UnicodeError:
            continue
    else:
        raise ValueError(f"{berkas}: pengodean CSV tidak dikenali")

    jumlah = len(df)
    kolom_tahun = [c for c in df if re.fullmatch(r"(19|20)\d{2}", c.strip())]
    if kolom_tahun:
        df = df.melt(id_vars=[c for c in df if c not in kolom_tahun], value_vars=kolom_tahun,
                     var_name="tahun", value_name="nilai")
    df = lineage(df, berkas)
    return (df, jumlah) if dengan_jumlah else df


def baca_json(berkas):
    """Uraikan datacontent memakai kode dimensi di halaman yang sama."""
    with (RAW / berkas).open(encoding="utf-8-sig") as f:
        halaman = json.load(f)
    if isinstance(halaman, dict):
        halaman = [halaman]

    data, meta = [], []
    for nomor, hal in enumerate(halaman, start=1):
        dimensi = [hal[k] for k in ("vervar", "var", "turvar", "tahun", "turtahun")]
        if not all(dimensi):
            raise ValueError(f"{berkas} halaman {nomor}: dimensi kosong")
        peta = {}
        for kombinasi in product(*dimensi):
            kunci = "".join(str(item["val"]) for item in kombinasi)
            if kunci in peta:
                raise ValueError(f"{berkas} halaman {nomor}: kode ambigu {kunci}")
            peta[kunci] = kombinasi

        for kunci, nilai in hal["datacontent"].items():
            if kunci not in peta:
                raise ValueError(f"{berkas} halaman {nomor}: kode tidak terpetakan {kunci}")
            wil, var, rincian, tahun, periode = peta[kunci]
            data.append({
                "var_id": str(var["val"]), "wilayah_id": str(wil["val"]), "wilayah": wil["label"],
                "turvar_id": str(rincian["val"]), "turvar": rincian["label"],
                "tahun_id": str(tahun["val"]), "tahun": tahun["label"],
                "turtahun_id": str(periode["val"]), "turtahun": periode["label"],
                "nilai": nilai, "_halaman": nomor,
            })

        for var in hal["var"]:
            meta.append({
                "var_id": str(var["val"]), "judul": var["label"], "satuan": var.get("unit", ""),
                "catatan": var.get("note", ""), "definisi": var.get("def", ""),
                "desimal": var.get("decimal"), "last_update": hal.get("last_update"),
                "tahun_terbit": ",".join(str(t["label"]) for t in hal["tahun"]), "_halaman": nomor,
            })
    return lineage(pd.DataFrame(data), berkas), lineage(pd.DataFrame(meta), berkas)


def baca_manifest_asal(berkas):
    with (RAW / berkas).open(encoding="utf-8-sig") as f:
        tabel = json.load(f)["tabel"]
    data = []
    for nama, isi in tabel.items():
        baris = {k: ",".join(map(str, v)) if isinstance(v, list) else v for k, v in isi.items()}
        data.append({"tabel": nama, **baris})
    return lineage(pd.DataFrame(data), berkas)


def periksa_kecocokan(hasil):
    """Bandingkan CSV dengan JSON berdasar lima kode dimensi dan nilai."""
    csv = hasil["bps_csv"]
    webapi = hasil["bps_json"].rename(columns={"turtahun_id": "periode_id"})
    kunci = ["var_id", "wilayah_id", "tahun_id", "periode_id", "turvar_id"]
    for berkas, baris in csv.groupby("_berkas_raw"):
        jalur = (RAW / berkas).relative_to(RAW)
        pasangan = (jalur.parent / "json" / jalur.with_suffix(".json").name).as_posix()
        tabel = []
        for df in (baris, webapi.loc[webapi["_berkas_raw"].eq(pasangan)]):
            nilai = pd.to_numeric(df["nilai"].astype(str).str.replace(",", ".", regex=False))
            tabel.append(df[kunci].assign(nilai=nilai).sort_values(kunci + ["nilai"]).reset_index(drop=True))
        pd.testing.assert_frame_equal(*tabel, check_dtype=False, check_exact=True)
        print(f"{jalur.stem}: COCOK ({len(baris)} baris)")


if __name__ == "__main__":
    from src.ekstraksi import jalankan

    hasil = jalankan("bps")
    print(hasil["_hitung"].to_string(index=False))
    periksa_kecocokan(hasil)
