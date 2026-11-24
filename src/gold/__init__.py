"""Tahap 4–6 — Gold. Sprint 1: tabel nasional, daftar pasangan rekonsiliasi, dan Silver di DuckDB.

Panel provinsi x periode x indikator dan tabel rekonsiliasi dengan selisih dikerjakan di Sprint 2.
"""
from src.gold import muat_sql, nasional, panel


def jalankan(silver):
    hasil = nasional.jalankan(silver)
    hasil["baris_sql"] = muat_sql.jalankan(silver, hasil.get("nasional_gold"))
    hasil["panel"] = panel.bentuk_panel(silver)
    return hasil
