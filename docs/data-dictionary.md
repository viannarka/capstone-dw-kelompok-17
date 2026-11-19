# Data dictionary — Nexora, Kasus 17

Satu tabel per keluaran (Silver dan setiap tabel Gold). Isi dari data nyata, bukan dari ingatan:
tipe, satuan, rentang, dan jumlah kosong dihitung ulang setiap kali pipeline berjalan.

## data/silver/silver.parquet

| Kolom | Tipe | Satuan/format | Boleh kosong | Rentang atau nilai sah | Asal (berkas/aturan) | Keterangan |
|---|---|---|---|---|---|---|
| sumber | string | — | tidak | bps, bnpb, wdi, who_gho, ilostat | nama folder data/raw | |
| wilayah_kode | int | kode BPS x 100 | tidak | kode provinsi BPS atau 9999 | konvensi starter | 9999 untuk Indonesia |

## data/gold/<tabel>.parquet

| Kolom | Tipe | Satuan/format | Boleh kosong | Rentang atau nilai sah | Asal (berkas/aturan) | Keterangan |
|---|---|---|---|---|---|---|

## Pencocokan Seri BPS – Kasus 17

Pencocokan dilakukan berdasarkan metadata dan label variabel
pada berkas JSON BPS sebelum penetapan indikator di Silver.

| Seri kode | Nama indikator dari BPS | Satuan | SDG hasil audit |
|---|---|---|---|
| var845 | Akses sumber air minum layak | Persen | 6.1.1 |
| var2741 | Layanan air minum dikelola secara aman | Persen | 6.1.1 |
| var847 | Akses sanitasi layak | Persen | 6.2.1 |
| var1273 | Fasilitas cuci tangan dengan sabun dan air | Persen | 6.2.1 |
| var2179 | Layanan sanitasi dikelola secara aman menurut tipe daerah | Persen | 6.2.1 |
| var2749 | Akses sanitasi aman | Persen | 6.2.1 |

Sumber:
data/raw/bps/2026-10-17/manifest_asal.json
dan berkas JSON BPS terkait.

Catatan:
- Untuk var847, judul tabel BPS menunjukkan sanitasi layak. K-009 mencatat koreksi katalog dari 11.1.1 ke 6.2.1.
- var2179 merupakan seri sanitasi aman yang memiliki
  tiga rincian berdasarkan tipe daerah, yaitu Perkotaan,
  Perdesaan, dan gabungan Perkotaan+Perdesaan.
  Seluruh rincian dipertahankan pada tahap ekstraksi.
- Seri dengan rentang sejak tahun 1990-an memiliki banyak
  halaman/periode tahun dalam JSON.
- Data mentah dan nilai asli tidak diubah pada tahap ekstraksi.

## Audit pembanding nasional

| Seri | Periode | Satuan | SDG hasil audit | Bukti |
|---|---|---|---|---|
| SH.H2O.SMDW.ZS | Tahun | Persen penduduk | 6.1.1 | Nama dan definisi layanan air aman di metadata WDI, K-015 |
| SH.H2O.BASW.ZS | Tahun | Persen penduduk | 1.4.1 | Pemetaan konseptual akses layanan dasar dari definisi WDI, K-016 |
| WSH_WATER_SAFELY_MANAGED | Tahun | Persen penduduk | 6.1.1 | PERCENT_POP_N, K-012 |
| WSH_HYGIENE_BASIC | Tahun | Persen penduduk | 6.2.1 | PERCENT_POP_N, K-013 |
| SDGODAWS | Tahun | Juta USD konstan 2024 | 6.a.1 | MONEY_N dan tahun dasar pada IndicatorName, K-014 |

[Hasil audit 11 seri](seri.csv) memuat judul asli, satuan, frekuensi, kode SDG dan jalur bukti. Kode SDG untuk kedua seri WDI merupakan pemetaan konsep. Metadata WDI menyatakan satuan di judul indikator.

Untuk WHO, `nama_di_berkas` berasal dari `IND_NAME` pada CSV observasi. Pada SDGODAWS, `MONEY_N` menunjukkan nilai uang dan `IndicatorName` di katalog OData menyebut juta USD dengan harga konstan 2024.
