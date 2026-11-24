"""Muat Parquet ke DuckDB dan publikasikan gudang setelah semua tabel terverifikasi."""
from pathlib import Path
from tempfile import TemporaryDirectory

import duckdb

from src.gold.nasional import GOLD_NASIONAL_PARQUET, REKONSILIASI
from src.gold.panel import PANEL_GOLD_LEBAR, PANEL_GOLD_PANJANG
from src.laporan import ROOT, catat
from src.silver import SILVER

DB = ROOT / "data" / "gold" / "gudang.duckdb"
PARQUET = {
    "silver": SILVER,
    "gold_provinsi": PANEL_GOLD_PANJANG,
    "panel_provinsi_tahunan": PANEL_GOLD_LEBAR,
    "gold_nasional": GOLD_NASIONAL_PARQUET,
    "rekonsiliasi": REKONSILIASI,
}


def jalankan():
    DB.parent.mkdir(parents=True, exist_ok=True)
    jumlah = {}
    with TemporaryDirectory(dir=DB.parent) as sementara:
        baru = Path(sementara) / DB.name
        with duckdb.connect(str(baru)) as con:
            for nama in ("silver.sql", "gold.sql"):
                con.execute(Path(__file__).with_name(nama).read_text(encoding="utf-8"))
            con.execute(
                "INSERT INTO seri SELECT seri_kode, sumber, tingkat, nama_baku, satuan, sdg_kode "
                "FROM read_csv(?, header=true, all_varchar=true)",
                [str(ROOT / "docs" / "seri.csv")],
            )
            for tabel, berkas in PARQUET.items():
                con.execute(f"INSERT INTO {tabel} BY NAME SELECT * FROM read_parquet(?)", [str(berkas)])
                sql, parquet = con.execute(
                    f"SELECT (SELECT count(*) FROM {tabel}), (SELECT count(*) FROM read_parquet(?))",
                    [str(berkas)],
                ).fetchone()
                if sql != parquet:
                    raise ValueError(f"{tabel}: {sql} baris SQL, {parquet} baris Parquet")
                jumlah[tabel] = sql
        baru.replace(DB)
    catat(baris_sql=jumlah["silver"])
    print("           DuckDB (SQL = Parquet): " + ", ".join(f"{k}={v}" for k, v in jumlah.items()))
    return jumlah["silver"]
