# Pilihan basis data (draf bagian laporan tim)

**Pilihan: DuckDB** (`data/gold/gudang.duckdb`, dibuat ulang oleh `python pipeline.py`; tidak di-commit).

- Satu berkas tanpa server: semua anggota dan pemeriksa bisa menjalankan pipeline tanpa memasang layanan.
- Dirancang untuk kueri analitik (agregasi, pivot), yang menjadi pekerjaan utama Gold di Sprint 2.
- Bisa membaca Parquet langsung, sehingga dipakai lagi untuk perbandingan pandas vs DuckDB di Sprint 3.

Skema di `src/gold/silver.sql`: kunci primer sama dengan kunci unik Silver; `CHECK` untuk wilayah,
jenis periode, panjang sha256, dan `batas_bawah ≤ nilai ≤ batas_atas`; foreign key `silver.seri_kode` ke
tabel `seri` (dari `docs/seri.csv`). Basis data menjadi lapis validasi terakhir: baris yang melanggar
ditolak saat dimuat. 3.242 baris termuat.

Alternatif yang juga sah: SQLite (paling sederhana, ada di pustaka standar Python) dan PostgreSQL (dekat
dengan lingkungan produksi, tetapi butuh server).

## Tabel vs dokumen

Respons JSON BPS adalah dokumen bersarang: satu objek per halaman berisi daftar label (`vervar`, `tahun`),
metadata seri (`var`, termasuk `note` berisi HTML), dan `datacontent` berkunci gabungan. Menyimpannya
sebagai dokumen (misalnya satu kolom JSON per berkas) mempertahankan metadata apa adanya dan cocok untuk
arsip. Untuk analisis, bentuk tabel Silver lebih tepat: setiap angka punya kolom wilayah, periode, dan
rincian yang bisa difilter, digabung, dan diberi kunci primer. Kunci ini menyimpan keduanya: berkas mentah
tetap di `data/raw/` (dokumen), Silver di DuckDB (tabel).
