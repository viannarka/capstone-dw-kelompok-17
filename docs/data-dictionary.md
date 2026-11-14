# Data dictionary — <Nama tim>

Satu tabel per keluaran (Silver dan setiap tabel Gold). Isi dari data nyata, bukan dari ingatan:
tipe, satuan, rentang, dan jumlah kosong dihitung ulang setiap kali pipeline berjalan.

## data/silver/silver.parquet

| Kolom | Tipe | Satuan/format | Boleh kosong | Rentang atau nilai sah | Asal (berkas/aturan) | Keterangan |
|---|---|---|---|---|---|---|
| sumber | string | — | tidak | bps, bnpb, wdi, who_gho, ilostat | nama folder data/raw | |
| wilayah_kode | int | kode BPS x 100 | tidak | 9999 atau 1100–9600 | log K-… | |

## data/gold/<tabel>.parquet

| Kolom | Tipe | Satuan/format | Boleh kosong | Rentang atau nilai sah | Asal (berkas/aturan) | Keterangan |
|---|---|---|---|---|---|---|

## Pencocokan Seri BPS – Kasus 17

Pencocokan dilakukan berdasarkan metadata dan label variabel
pada berkas JSON BPS sebelum penetapan indikator di Silver.

| Seri kode | Nama indikator dari BPS | Satuan | SDG katalog |
|---|---|---|---|
| var845 | Akses sumber air minum layak | Persen | 6.1.1 |
| var2741 | Layanan air minum dikelola secara aman | Persen | 6.1.1 |
| var847 | Akses sanitasi layak | Persen | 11.1.1 |
| var1273 | Fasilitas cuci tangan dengan sabun dan air | Persen | 6.2.1 |
| var2179 | Layanan sanitasi dikelola secara aman menurut tipe daerah | Persen | 6.2.1 |
| var2749 | Akses sanitasi aman | Persen | 6.2.1 |

Sumber:
data/raw/bps/2026-10-17/manifest_asal.json
dan berkas JSON BPS terkait.

Catatan:
- Kode SDG masih mengikuti katalog awal dan perlu diverifikasi
  sebelum digunakan sebagai kode final di Silver.
- var847 membahas akses sanitasi layak, tetapi pada katalog awal
  tercantum kode SDG 11.1.1. Kesesuaian kode indikator perlu
  diperiksa kembali sebelum ditetapkan pada tahap Silver.
- var2179 merupakan seri sanitasi aman yang memiliki
  tiga rincian berdasarkan tipe daerah, yaitu Perkotaan,
  Perdesaan, dan gabungan Perkotaan+Perdesaan.
  Seluruh rincian dipertahankan pada tahap ekstraksi.
- Seri dengan rentang sejak tahun 1990-an memiliki banyak
  halaman/periode tahun dalam JSON.
- Data mentah dan nilai asli tidak diubah pada tahap ekstraksi.