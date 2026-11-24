"""Tahap Gold: tabel nasional, rekonsiliasi, panel provinsi, dan penyimpanan SQL."""
from src.gold import muat_sql, nasional, panel


def jalankan(silver):
    hasil = nasional.jalankan(silver)
    hasil["panel"] = panel.bentuk_panel(silver)
    hasil["baris_sql"] = muat_sql.jalankan()
    return hasil
