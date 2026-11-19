# Laporan tim — Nexora, kasus 17 Air minum dan sanitasi

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan `log-keputusan.csv` (id K-001 s.d. K-022).

## Ringkasan

Kasus ini menyatukan enam seri tingkat provinsi BPS untuk lima konsep (air layak, air aman, sanitasi layak, sanitasi aman, dan cuci tangan) dengan dua seri pembanding World Bank WDI dan tiga seri WHO GHO. Dataset Silver pertama berhasil dibentuk dengan 3.242 baris dari 11 seri indikator. Panel pengamatan terpanjang mencakup periode 1993–2025, menghadirkan tantangan berlapis: ketidaksesuaian label kode SDG katalog dengan isi berkas, pergeseran definisi di tengah seri waktu, daerah yang tidak dicacah atau hanya dicacah di ibu kota provinsi, pemekaran wilayah sejak 1999, serta keberadaan dua tabel BPS dengan angka yang sama.

## Data dan lineage

Sebanyak 22 berkas mentah digunakan:
- BPS snapshot 17 Oktober 2026: 6 CSV, 6 JSON berhalaman, 1 catatan unduhan `manifest_asal.json`.
- WDI snapshot 20 Oktober 2026: 1 data JSON dan 3 metadata JSON.
- WHO GHO snapshot 20 Oktober 2026: 3 CSV dan 2 metadata JSON.

Seluruh berkas diproses melalui pembaca modular di `src/ekstraksi/` (menghasilkan 6.382 baris mentah pada berkas data). Setiap baris di Silver mempertahankan provenans ketat melalui kolom `_berkas_raw` dan `_sha256_raw` yang diverifikasi terhadap `MANIFEST.csv`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Kode SDG katalog tertukar | `var847`: judul sanitasi layak, katalog 11.1.1 | Dikoreksi ke 6.2.1; dijaga aturan validasi tujuan SDG vs nama berkas | 1.036 | K-009 |
| Kode tahun beda panjang | daftar `tahun` BPS: 2 digit (1993–1999) dan 3 digit (2000+) | Pemotong kunci datacontent mencoba semua kombinasi panjang yang sah | 6.382 mentah | K-001 / K-003 |
| Provinsi tidak dicacah | Susenas 2000 (NAD, Maluku, Maluku Utara) & 2001 (NAD) di `var.def` a, b | Diklasifikasikan sebagai `tidak_diterbitkan` per provinsi, bukan missing biasa | 8 sel | K-017 |
| Cakupan hanya ibu kota | `var.def` c tahun 2002 (NAD, Maluku, Maluku Utara, Papua) | Ditandai sebagai `cakupan_parsial` | 6 calon | K-012 |
| Definisi berganti | `var.def` d air layak 2011, sanitasi layak 2019, `var.note` cuci tangan 2016 | Ditandai sebagai `patahan_seri` / `patahan_definisi`, bukan outlier | 52 calon | K-013 / K-019 |
| Dua tabel sanitasi aman | `var2749` identik dengan `var2179` rincian gabungan | Keduanya disimpan di Silver; dijaga aturan validasi | 0 | K-011 |
| Missing murni | Papua Pegunungan di `var2749` (2024–2025) | Tidak diimputasi di Silver; Gold akan memakai `var2179` yang lengkap | 2 sel | K-018 |
| Pemekaran wilayah | Pemekaran sejak 1999 (9 provinsi baru sampai Papua 2024) | Grid lengkap 38 provinsi: 413 `belum_ada`, 30 `batas_lama`, 26 `patahan_wilayah` | 469 sel | K-017 |
| Perbedaan struktural | IQR berulang di ujung distribusi | Ditandai perbedaan struktural, nilai asli dipertahankan | 7 provinsi | K-005 |
| Calon anomali statistik | IQR tiga arah (antarwilayah, antarperiode, dalam provinsi) | 266 outlier ditandai tanpa modifikasi nilai | 403 calon | K-002–K-007, K-019 |
| Satuan bantuan pembangunan | odata WHO: Juta USD konstan 2024 | Satuan baku `juta_usd_konstan_2024`, bukan persen | 14 baris | K-014 |
| Sumber ganda BPS | Nilai CSV identik dengan JSON | JSON ditetapkan sebagai sumber utama Silver | 3.058 baris | K-020 |

Tidak ditemukan galat input (0 baris di luar rentang sah atau salah ketik desimal).

## Integrasi dan rekonsiliasi

Persiapan Tahap 6 telah diselesaikan pada Sprint 1 (`reports/pasangan-rekonsiliasi.md` dan `reports/tabel-nasional.csv`):
- **Tabel nasional periode $\times$ seri:** Matriks lebar 33 periode $\times$ 11 seri nasional untuk memetakan irisan waktu observasi.
- **P1 (Air minum aman):** BPS `var2741` vs WHO `WSH_WATER_SAFELY_MANAGED` vs WDI `SH.H2O.SMDW.ZS` (3 tahun irisan: 2020–2022; selisih definisi rumah tangga vs penduduk dan metode pemodelan JMP).
- **P2 (Air minum layak vs dasar):** BPS `var845` vs WDI `SH.H2O.BASW.ZS` (15 tahun irisan; konsep layak BPS tidak sama dengan basic WDI karena waktu ambil air $\le$ 30 menit).
- **P3 (Cuci tangan):** BPS `var1273` vs WHO `WSH_HYGIENE_BASIC` (7 tahun irisan; rumah tangga vs penduduk; tahun 2016 dari modul MKP).
- **P4 (Air aman WHO vs WDI):** WHO vs WDI (23 tahun irisan: 2000–2022; selisih vintage pembaruan JMP).
- **P5 (Konteks):** WHO `SDGODAWS` sebagai konteks pendanaan resmi air dan sanitasi.

## Validasi, penyimpanan, dan reproduksibilitas

### Pilihan basis data dan pemuatan SQL (Tahap 5)
Dataset Silver dimuat ke **DuckDB** (`data/gold/gudang.duckdb`) menggunakan DDL relasional di `src/gold/silver.sql` melalui skrip `src/gold/muat_sql.py`. Sebanyak 3.242 baris berhasil termuat.
- **Alasan pemilihan DuckDB:** Berkas tunggal embedded tanpa dependensi server, eksekusi kueri analitik (OLAP/agregasi/pivot) sangat cepat, dan integrasi mulus dengan Parquet untuk perbandingan kinerja di Sprint 3.
- **Perbandingan Tabel Relasional vs Dokumen JSON mentah:** Dokumen JSON mentah (hierarki bertingkat) cocok sebagai arsip lapis Bronze untuk mempertahankan metadata asli. Sebaliknya, tabel SQL relasional di Silver/Gold memecah observasi ke kolom baku (`wilayah_kode`, `periode`, `rincian`, `nilai`) dengan *primary key*, *foreign key* ke katalog seri, dan *CHECK constraint* sebagai lapis validasi integritas data terakhir. Rincian selengkapnya ada di `reports/basis-data.md`.

### Validasi dan reproduksi
Sebanyak 11 aturan validasi otomatis dijalankan setiap pipeline (10 lolos, 1 peringatan; `reports/validasi.md`). Seluruh alur dapat direproduksi ulang dari data mentah melalui perintah tunggal:
```powershell
python pipeline.py
```
Durasi eksekusi pipeline dari data mentah hingga validasi memakan waktu $\pm$6,7 detik pada mesin pengujian.

## Pembagian kerja

| Anggota | NIM | Komponen | Tugas sampingan | Bagian laporan yang ditulis |
|---|---|---|---|---|
| Ayu Andriani | 124450041 | Ekstraksi dan lineage | Penjaga Data & Evaluasi | Data dan lineage, ekstraksi per berkas |
| Azzelya Thianandry | 124450057 | Ekstraksi dan lineage | Penjaga Data & Evaluasi | Lineage SHA-256, verifikasi manifest |
| Salavi Naharani | 124450090 | Profil dan pembersihan | Analis Utama | Masalah data, profiling IQR, anomali |
| Asri Meilani | 124450010 | Transformasi dan panel | Integrator | Skema Silver, penyeragaman satuan & SDG |
| Favian Arkaanda | 124450021 | Integrasi, penyimpanan, dan skala | Koordinator | Integrasi & rekonsiliasi, basis data DuckDB |
| Abdul Hakim MT | 124450058 | Validasi dan dokumentasi | Reproduksi & Demo | Validasi otomatis, data dictionary, demo |
