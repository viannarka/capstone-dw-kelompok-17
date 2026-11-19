# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var845 | Persentase Rumah Tangga yang Memiliki Akses terhadap Sumber Air Minum Layak Menurut Provinsi | Persentase rumah tangga yang memiliki akses terhadap sumber air minum layak |
| var2741 | 6.1.1* Persentase rumah tangga yang menggunakan layanan air minum yang dikelola secara aman menurut provinsi | Persentase rumah tangga yang menggunakan layanan air minum yang dikelola secara aman |
| var847 | Persentase Rumah Tangga menurut Provinsi dan Memiliki Akses terhadap Sanitasi Layak | Persentase rumah tangga yang memiliki akses terhadap sanitasi layak |
| var1273 | 6.2.1* Persentase Rumah Tangga yang Memiliki Fasilitas Cuci Tangan dengan Sabun dan Air Menurut Provinsi | Persentase rumah tangga yang memiliki fasilitas cuci tangan dengan sabun dan air |
| var2179 | Persentase Rumah Tangga Menggunakan Layanan Sanitasi yang Dikelola Secara Aman Menurut Provinsi dan Tipe Daerah | Persentase rumah tangga yang menggunakan layanan sanitasi yang dikelola secara aman, menurut tipe daerah |
| var2749 | 6.2.1* Persentase rumah tangga yang memiliki akses terhadap sanitasi aman menurut provinsi | Persentase rumah tangga yang memiliki akses terhadap sanitasi aman |
| SH.H2O.SMDW.ZS | People using safely managed drinking water services (% of population) | People using safely managed drinking water services (% of population) |
| SH.H2O.BASW.ZS | People using at least basic drinking water services (% of population) | People using at least basic drinking water services (% of population) |
| WSH_WATER_SAFELY_MANAGED | Population using safely managed drinking-water services | Population using safely managed drinking-water services (%) |
| WSH_HYGIENE_BASIC | Population using hand-washing facilities with soap and water | Population with basic handwashing facilities with soap and water at home (%) |
| SDGODAWS | Water and sanitation development assistance as part of official government spending plans | Water- and sanitation-related ODA in government spending plans |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var845 | persen | persen | var.unit: 'Persen' | 6.1.1 | 6.1.1 |
| var2741 | persen | persen | var.unit: 'Persen' | 6.1.1 | 6.1.1 |
| var847 | persen | persen | var.unit: 'Persen' | 11.1.1 | 6.2.1 |
| var1273 | persen | persen | var.unit: 'Persen' | 6.2.1 | 6.2.1 |
| var2179 | persen | persen | var.unit: 'Persen' | 6.2.1 | 6.2.1 |
| var2749 | persen | persen | var.unit: 'Persen' | 6.2.1 | 6.2.1 |
| SH.H2O.SMDW.ZS | — | persen | name: '(% of population)' | — | 6.1.1 |
| SH.H2O.BASW.ZS | — | persen | name: '(% of population)' | — | 1.4.1 |
| WSH_WATER_SAFELY_MANAGED | — | persen | kolom PERCENT_POP_N | 6.1.1 | 6.1.1 |
| WSH_HYGIENE_BASIC | — | persen | kolom PERCENT_POP_N | 6.2.1 | 6.2.1 |
| SDGODAWS | — | juta_usd_konstan_2024 | kolom MONEY_N; odata IndicatorName '(constant 2024 US$ millions)' | 6.a.1 | 6.a.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var847 | kode SDG 11.1.1 -> 6.2.1 (katalog tertukar dengan hunian layak) |
| SH.H2O.SMDW.ZS | kode SDG kosong -> 6.1.1 |
| SH.H2O.BASW.ZS | kode SDG kosong -> 1.4.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2741 | Sumber: Badan Pusat Statistik |
| 2749 | Sumber: Badan Pusat Statistik |
| 845 | Sumber: Susenas Maret |
| 1273 | Sumber: BPS - Angka 2016 merupakan angka hasil Susenas MKP 2016 - Pertanyaan mengenai fasilitas cuci tangan pertama kali ditanyakan di Susenas MKP 2016, untuk data KOR Maret 2016 belum mengakomodir pertanyaan mengenai fasilitas cuci tangan |
| 2179 | Sumber: BPS, Susenas Maret |
| 847 | Sumber: Susenas Maret |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SH.H2O.BASW.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SH.H2O.SMDW.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
