# Sprint 1 (9–22 November 2026) — Tim Nexora

## Sprint Goal

Semua berkas mentah Kasus 17 terbaca dengan lineage, setiap seri punya satuan dan kode SDG yang buktinya tercatat, dan Silver pertama lolos pemeriksa skema serta aturan validasi dasar, sehingga Sprint 2 bisa langsung menyusun panel dan tabel rekonsiliasi.

## Definition of Done Sprint 1

- [x] **Pembaca format mentah lengkap:** Pembaca untuk BPS JSON/CSV, WDI JSON, dan WHO GHO CSV/JSON berfungsi di `src/ekstraksi/`; 22 berkas di MANIFEST terverifikasi dan terbaca (6.382 baris mentah observasi).
- [x] **Lineage SHA-256:** Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw` yang dapat ditelusuri langsung ke berkas Bronze.
- [x] **Profil statistik dan anomali:** Profil deskriptif 6 seri BPS, grid wilayah $\times$ periode (453 sel kosong), serta visualisasi boxplot dan deret waktu tersimpan di `reports/gambar/`.
- [x] **Pembersihan dan pencatatan keputusan:** Penanganan missing, pemisahan patahan definisi/wilayah dari outlier statistik, serta deduplikasi tercatat pada `log-keputusan.csv` (K-001 s.d. K-022).
- [x] **Dataset Silver lolos skema minimal:** Berkas `data/silver/silver.parquet` lolos pemeriksaan `python -m src.common.skema` (3.242 baris, 11 seri, 39 wilayah).
- [x] **Validasi otomatis dan data dictionary:** 11 aturan validasi (10 lolos, 1 peringatan) berjalan pada `src/validasi/` dan kamus data `docs/data-dictionary.md` terdokumentasi lengkap.
- [x] **Persiapan integrasi dan SQL:** Tabel nasional `reports/tabel-nasional.csv`, dokumen pasangan rekonsiliasi `reports/pasangan-rekonsiliasi.md`, serta pemuatan 3.242 baris ke DuckDB `data/gold/gudang.duckdb` via `src/gold/silver.sql`.
- [x] **Metrik anggota ter-commit:** Seluruh anggota memiliki bukti artefak di `results/<nim>/metrics.json`.
- [x] **Satu perintah reproduksi:** `python pipeline.py` menghasilkan ulang seluruh artefak dalam waktu $\pm$6.7 detik.
- [x] **Naskah Demo Sprint 1:** Panduan teknis demonstrasi 10 menit tersedia di `DEMO.md` untuk diunggah paling lambat 22 November.
