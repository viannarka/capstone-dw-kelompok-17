# AI_LOG — <Nama tim>

Satu baris per pemakaian AI yang bermakna (ChatGPT, Claude, Copilot, Bravais, dan sejenisnya).
Ringkas dan jujur; transkrip penuh tidak diminta. Yang dinilai bukan "pakai AI atau tidak",
melainkan "mengerti atau tidak" — isi kolom terakhir dengan apa yang Anda ubah dari keluarannya.

| Tanggal | Siapa (NIM) | Alat | Untuk apa | Apa yang diubah dari keluarannya |
|---|---|---|---|---|
| 2026-11-03 | 12345678 | Copilot | kerangka DataLoader | ganti normalisasi, tambah seed worker |
| 2026-11-19 | 124450021 | Codex | Menyelaraskan ekstraksi, profil dan audit metadata Sprint 1 dengan acuan dosen | Pemeriksaan otomatis membandingkan hitungan tiap berkas, sel kandidat IQR, ketersediaan pembanding serta satuan dan kode SDG. |
| 2026-11-19 | 124450021 | Codex | Memisahkan keluaran ekstraksi menurut struktur repo kunci | Profil dan audit membaca tabel per sumber. Perbandingan dilakukan pada 22 berkas dan pada hasil laporan sebelum dan sesudah perubahan. |
| 2026-11-19 | 124450021 | Codex | Memeriksa pekerjaan terhadap folder k17-air-sanitasi/sprint-1 | Alasan IQR dan penanda berulang dihitung per sel pada laporan profil. Audit mengambil judul WHO dari CSV observasi dan memeriksa tahun dasar SDGODAWS di katalog OData. |
| 2026-11-19 | 124450021 | Gemini CLI | Persiapan tahap 6: penyusunan tabel nasional periode × seri dan pasangan rekonsiliasi | Memverifikasi keterbandingan 5 pasangan rekonsiliasi (4 selisih, 1 konteks) dengan 48 periode beririsan, pembentukan tabel nasional (reports/tabel-nasional.csv), dokumentasi DuckDB (reports/basis-data.md), dan pencatatan metrik hasil komponen. |
| 2026-11-19 | 124450021 | Gemini CLI | Persiapan tahap 5: perancangan skema SQL Silver dan evaluasi basis data | Memverifikasi skema DDL (src/gold/silver.sql) dan pemuatan ke DuckDB (src/gold/muat_sql.py), menyusun draf perbandingan tabel SQL vs dokumen JSON (reports/basis-data.md), dan memperbarui laporan tim (reports/tim.md). |
| 2026-11-19 | 124450057 | Antigravity | Verifikasi aturan validasi Silver dasar dan khas kasus Kasus 17 serta pencatatan metrik | Memeriksa 11 aturan validasi skema Pandera (7 umum, 4 kasus), memverifikasi hasil lolos/peringatan di reports/validasi.md, menyusun laporan individu, dan mencatat metrik ke results/124450057/metrics.json. |
| 2026-11-19 | 124450057 | Antigravity | Melengkapi dokumentasi docs/data-dictionary.md seluruh kolom Silver dan penelusuran lineage | Menambahkan atribut nama, tipe, satuan, arti, asal berkas/log untuk 15 kolom Silver, memperbarui generator src/dokumen.py, dan merinci penelusuran satu baris Silver ke berkas mentah. |
| 2026-11-19 | 124450021 | Gemini CLI | Koordinasi Sprint 1: perumusan Sprint Goal, evaluasi standup, panduan log sprint 3 baris, dan naskah demo | Menyusun sprint-goal.md, standup.md, draf log sprint 3 baris seluruh anggota di sprint/sprint-1/, naskah demo 10 menit (DEMO.md), serta menyelaraskan checklist Definition of Done Sprint 1. |
| 2026-11-24 | 124450058 | Antigravity | Tahap 6 (persiapan): seleksi rincian sebanding dan penyelarasan periode pembanding di log-keputusan.csv | Memeriksa ketersediaan rincian di data Silver, menetapkan agregat 'total' dan periode tahunan (YYYY) untuk kelima seri pembanding, serta mencatat alasan pemisahan rincian wilayah dan penetapan SDGODAWS sebagai indikator konteks (K-026 s.d. K-030). |
