# Metadata seri: nama, satuan, kode SDG

Dihasilkan dari berkas mentah dan `src/konfigurasi.py`.

Tabel lengkap seri tersedia di `docs/seri.csv`.

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
| WSH_WATER_SAFELY_MANAGED | Population using safely managed drinking-water services (%) | Population using safely managed drinking-water services (%) |
| WSH_HYGIENE_BASIC | Population with basic handwashing facilities at home (%) | Population with basic handwashing facilities with soap and water at home (%) |
| SDGODAWS | Amount of water- and sanitation-related official development assistance that is part of a government-coordinated spending plan (constant 2024 US$ millions) | Water- and sanitation-related ODA in government spending plans |

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

## Bukti metadata BPS

| seri_kode | judul | satuan | cakupan_tahun | jumlah_baris | last_update | berkas_raw |
|---|---|---|---|---|---|---|
| var845 | Persentase Rumah Tangga yang Memiliki Akses terhadap Sumber Air Minum Layak Menurut Provinsi | Persen | 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2021, 2022, 2023, 2024, 2025 | 722 | 2025-12-16 10:31:12 | bps/2026-10-17/manifest_asal.json |
| var847 | Persentase Rumah Tangga menurut Provinsi dan Memiliki Akses terhadap Sanitasi Layak | Persen | 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | 1036 | 2025-12-16 14:31:07 | bps/2026-10-17/manifest_asal.json |
| var2179 | Persentase Rumah Tangga Menggunakan Layanan Sanitasi yang Dikelola Secara Aman Menurut Provinsi dan Tipe Daerah | Persen | 2020, 2021, 2022, 2023, 2024, 2025 | 648 | 2025-12-15 15:07:24 | bps/2026-10-17/manifest_asal.json |
| var1273 | 6.2.1* Persentase Rumah Tangga yang Memiliki Fasilitas Cuci Tangan dengan Sabun dan Air Menurut Provinsi | Persen | 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | 358 | 2026-07-06 15:13:09 | bps/2026-10-17/manifest_asal.json |
| var2741 | 6.1.1* Persentase rumah tangga yang menggunakan layanan air minum yang dikelola secara aman menurut provinsi | Persen | 2020, 2021, 2022, 2023, 2024, 2025 | 218 | 2026-06-04 12:45:09 | bps/2026-10-17/manifest_asal.json |
| var2749 | 6.2.1* Persentase rumah tangga yang memiliki akses terhadap sanitasi aman menurut provinsi | Persen | 2024, 2025 | 76 | 2026-06-17 15:37:14 | bps/2026-10-17/manifest_asal.json |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var847 | kode SDG 11.1.1 -> 6.2.1 (katalog tertukar dengan hunian layak) |
| SH.H2O.SMDW.ZS | kode SDG kosong -> 6.1.1 |
| SH.H2O.BASW.ZS | kode SDG kosong -> 1.4.1 |

## Metadata WDI yang muncul lebih dari satu kali

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SH.H2O.BASW.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SH.H2O.SMDW.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.

## Catatan BPS

Kolom var.note tidak tersedia pada metadata hasil ekstraksi ini.
