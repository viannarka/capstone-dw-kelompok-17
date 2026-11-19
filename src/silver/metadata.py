"""Satuan, nama, dan kode SDG setiap seri berdasarkan metadata sumber."""

import json
import re

import pandas as pd

from src import konfigurasi as K
from src.laporan import ROOT, catat, tabel_md, tulis


def _bersih(teks):
    """Buang tag HTML dan spasi berlebih."""
    if pd.isna(teks):
        return ""
    t = re.sub(r"<[^>]+>", " ", str(teks))
    return re.sub(r"\s+", " ", t).strip()


def _metadata_bps(mentah):
    """Ambil metadata tabel BPS dari kolom detail_tabel."""
    kolom = [
        "seri_kode", "judul", "satuan", "cakupan_tahun",
        "jumlah_baris", "last_update", "berkas_raw",
    ]

    hasil = []
    data = mentah[
        (mentah["_sumber_data"] == "bps")
        & (mentah["_jenis_data"] == "metadata")
    ]

    for _, r in data.iterrows():
        try:
            detail = json.loads(r["detail_tabel"])
        except (TypeError, ValueError):
            continue

        var = detail.get("var")
        if var is None:
            continue

        kode = f"var{int(var)}"
        if kode not in K.SERI:
            continue

        tahun = detail.get("tahun", [])
        last_update = detail.get("last_update", [])

        hasil.append({
            "seri_kode": kode,
            "judul": _bersih(detail.get("judul", "")),
            "satuan": _bersih(detail.get("satuan", "")),
            "cakupan_tahun": ", ".join(map(str, tahun)),
            "jumlah_baris": detail.get("baris"),
            "last_update": ", ".join(map(str, last_update)),
            "berkas_raw": r.get("_berkas_raw", ""),
        })

    return pd.DataFrame(hasil, columns=kolom).drop_duplicates("seri_kode")


def nama_dari_berkas(mentah):
    """Ambil nama seri dari metadata BPS, WDI, dan WHO."""
    nama = {}

    # Metadata BPS
    bps = _metadata_bps(mentah)
    for _, r in bps.iterrows():
        nama[r["seri_kode"]] = (
            r["judul"],
            f"{r['berkas_raw']} detail_tabel.judul",
        )

    # Metadata indikator WDI
    wdi = mentah[
        (mentah["_sumber_data"] == "wdi")
        & (mentah["_jenis_data"] == "indikator")
    ]
    for _, r in wdi.iterrows():
        kode = r.get("indikator_id")
        judul = r.get("indikator_nama")
        if pd.notna(kode) and pd.notna(judul):
            nama[str(kode)] = (
                _bersih(judul),
                f"{r.get('_berkas_raw', '')} indikator_nama",
            )

    # Metadata indikator WHO
    who = mentah[
        (mentah["_sumber_data"] == "who")
        & (mentah["_jenis_data"] == "indikator")
    ]
    for _, r in who.iterrows():
        kode = r.get("IndicatorCode")
        judul = r.get("IndicatorName")
        if pd.notna(kode) and pd.notna(judul):
            nama[str(kode)] = (
                _bersih(judul),
                f"{r.get('_berkas_raw', '')} IndicatorName",
            )

    return nama


def periksa_metadata_ganda(mentah):
    """Periksa apakah metadata indikator WDI muncul berulang."""
    m = mentah[
        (mentah["_sumber_data"] == "wdi")
        & (mentah["_jenis_data"] == "indikator")
    ].copy()

    if m.empty:
        return pd.DataFrame(
            columns=["seri", "jumlah_entri", "berkas", "isi_sama"]
        )

    baris = []

    for kode, g in m.groupby("indikator_id"):
        if len(g) < 2:
            continue

        kolom_banding = [
            k for k in ["indikator_nama", "sumber_catatan", "sumber_organisasi"]
            if k in g.columns
        ]

        sama = all(
            g[k].nunique(dropna=False) == 1
            for k in kolom_banding
        )

        berkas = sorted(
            g["_berkas_raw"].dropna().astype(str).str.split("/").str[-1]
        )

        baris.append({
            "seri": kode,
            "jumlah_entri": len(g),
            "berkas": ", ".join(berkas),
            "isi_sama": "ya" if sama else "tidak",
        })

    return pd.DataFrame(baris)


def jalankan(mentah, cakupan_who):
    """Buat katalog seri dan laporan metadata."""
    nama = nama_dari_berkas(mentah)
    bukti_bps = _metadata_bps(mentah)

    baris = []

    for kode, s in K.SERI.items():
        nb, asal = nama.get(kode, ("", ""))
        cakup = s.get("cakupan", "")

        if kode in cakupan_who and cakupan_who[kode]:
            tetap = "; ".join(
                f"{k}={v}" for k, v in cakupan_who[kode].items()
            )
            cakup = f"{cakup} [dimensi tetap di berkas: {tetap}]".strip()

        baris.append({
            "sumber": s["sumber"],
            "seri_kode": kode,
            "tingkat": s["tingkat"],
            "nama_di_berkas": nb.strip(),
            "asal_nama": asal,
            "nama_baku": s["nama"],
            "satuan": s["satuan"],
            "bukti_satuan": s["bukti_satuan"],
            "sdg_kode": s["sdg"],
            "bukti_sdg": s["bukti_sdg"],
            "cakupan": cakup,
            "katalog_satuan": s["katalog_satuan"],
            "katalog_sdg": s["katalog_sdg"],
            "koreksi_katalog": s.get("koreksi", ""),
        })

    seri = pd.DataFrame(baris)

    (ROOT / "docs").mkdir(parents=True, exist_ok=True)
    seri.to_csv(ROOT / "docs" / "seri.csv", index=False)

    ganda = periksa_metadata_ganda(mentah)
    spasi = [
        k for k, (nb, _) in nama.items()
        if nb != nb.strip()
    ]

    koreksi = seri[seri["koreksi_katalog"] != ""]

    catat(
        koreksi_katalog=len(koreksi),
        metadata_ganda=len(ganda),
    )

    tulis("metadata.md", "\n\n".join([
        "# Metadata seri: nama, satuan, kode SDG",
        "Dihasilkan dari berkas mentah dan `src/konfigurasi.py`.",
        "Tabel lengkap seri tersedia di `docs/seri.csv`.",

        "## Nama di berkas mentah dan nama baku",
        tabel_md(seri[[
            "seri_kode", "nama_di_berkas", "nama_baku"
        ]]),

        "## Satuan dan kode SDG",
        tabel_md(seri[[
            "seri_kode", "katalog_satuan", "satuan",
            "bukti_satuan", "katalog_sdg", "sdg_kode"
        ]]),

        "## Bukti metadata BPS",
        tabel_md(bukti_bps) if len(bukti_bps) else "Tidak ada metadata BPS.",

        "## Koreksi katalog",
        tabel_md(koreksi[[
            "seri_kode", "koreksi_katalog"
        ]]) if len(koreksi) else "Tidak ada.",

        "## Metadata WDI yang muncul lebih dari satu kali",
        tabel_md(ganda) if len(ganda) else "Tidak ada.",

        "## Judul dengan spasi di awal/akhir",
        (
            ", ".join(spasi)
            + ": teks asli disimpan, versi rapi digunakan dalam laporan."
        ) if spasi else "Tidak ada.",

        "## Catatan BPS",
        "Kolom var.note tidak tersedia pada metadata hasil ekstraksi ini.",
    ]))

    return seri