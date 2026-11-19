# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var845 | 1993→1994 | 26 | 0.08 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1994→1995 | 26 | 0.04 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1995→1996 | 26 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1996→1997 | 26 | 0.04 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1997→1998 | 26 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1998→1999 | 26 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 1999→2000 | 24 | 0.00 | 0.08 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2000→2001 | 24 | 0.46 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2001→2002 | 29 | 0.07 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2002→2003 | 30 | 0.00 | 0.17 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2003→2004 | 30 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2004→2005 | 30 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2005→2006 | 31 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2006→2007 | 33 | 0.06 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2007→2008 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2008→2009 | 33 | 0.09 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2009→2010 | 33 | 0.03 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2010→2021 | 33 | 1.00 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var845 | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2741 | 2020→2021 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2741 | 2021→2022 | 34 | 0.09 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2741 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2741 | 2023→2024 | 34 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2741 | 2024→2025 | 38 | 0.05 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1993→1994 | 26 | 0.19 | 0.04 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1994→1995 | 26 | 0.12 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1995→1996 | 26 | 0.50 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1996→1997 | 26 | 0.15 | 0.04 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1997→1998 | 26 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1998→1999 | 26 | 0.23 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 1999→2000 | 24 | 0.04 | 0.08 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2000→2001 | 24 | 0.17 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2001→2002 | 29 | 0.10 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2002→2003 | 30 | 0.00 | 0.13 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2003→2004 | 30 | 0.10 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2004→2006 | 30 | 0.00 | 0.23 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2006→2007 | 33 | 0.88 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2007→2008 | 33 | 0.21 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2008→2009 | 33 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2009→2010 | 33 | 0.24 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2010→2011 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2011→2012 | 33 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2012→2013 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2013→2014 | 33 | 0.03 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2014→2015 | 33 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2015→2016 | 34 | 0.21 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2018→2019 | 34 | 0.18 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var847 | 2024→2025 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2016→2017 | 34 | 0.18 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2017→2018 | 34 | 0.18 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2022→2023 | 34 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1273 | 2024→2025 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2179 | 2020→2021 | 34 | 0.06 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2179 | 2021→2022 | 34 | 0.71 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var2179 | 2022→2023 | 34 | 0.06 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2179 | 2023→2024 | 34 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2179 | 2024→2025 | 38 | 0.00 | 0.21 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2749 | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |

## Pergantian definisi yang dinyatakan penerbit

- `var845` mulai 2021: var.def d: mulai 2011 rumus baru (air minum utama dan air mandi/cuci); tabel melompat 2010 -> 2021
- `var847` mulai 2019: var.def d: sejak 2019 konsep mengacu metadata SDGs
- `var1273` mulai 2017: var.note: angka 2016 dari Susenas MKP 2016; KOR Maret 2016 belum menanyakan cuci tangan

## Cakupan parsial yang dinyatakan penerbit

- `var845` 2002: Aceh, Maluku, Maluku Utara, Papua
- `var847` 2002: Aceh, Maluku, Maluku Utara, Papua

## Perubahan batas wilayah di tengah panel: 26

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var845 | Riau | 1400 | 2005 | Kepulauan Riau | 49.84 | 49.58 |
| var845 | Sumatera Selatan | 1600 | 2001 | Kepulauan Bangka Belitung | 36.51 | 45.16 |
| var845 | Jawa Barat | 3200 | 2001 | Banten | 24.24 | 40.33 |
| var845 | Kalimantan Timur | 6400 | 2021 | Kalimantan Utara | 43.27 | 85.80 |
| var845 | Sulawesi Utara | 7100 | 2001 | Gorontalo | 46.05 | 58.90 |
| var845 | Sulawesi Selatan | 7300 | 2006 | Sulawesi Barat | 45.82 | 50.12 |
| var845 | Maluku | 8100 | 2001 | Maluku Utara | 42.26 | 59.02 |
| var845 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 81.57 | 82.38 |
| var845 | Papua | 9400 | 2006 | Papua Barat | 38.72 | 36.33 |
| var845 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 66.49 | 85.84 |
| var2741 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 30.72 | 41.63 |
| var2741 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 25.86 | 34.97 |
| var847 | Riau | 1400 | 2006 | Kepulauan Riau | 37.95 | 32.74 |
| var847 | Sumatera Selatan | 1600 | 2001 | Kepulauan Bangka Belitung | 25.90 | 23.69 |
| var847 | Jawa Barat | 3200 | 2001 | Banten | 34.04 | 33.44 |
| var847 | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 72.65 | 68.83 |
| var847 | Sulawesi Utara | 7100 | 2001 | Gorontalo | 45.80 | 50.60 |
| var847 | Sulawesi Selatan | 7300 | 2006 | Sulawesi Barat | 39.22 | 36.74 |
| var847 | Maluku | 8100 | 2001 | Maluku Utara | 30.85 | 22.70 |
| var847 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 76.30 | 79.00 |
| var847 | Papua | 9400 | 2006 | Papua Barat | 23.47 | 13.06 |
| var847 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 43.00 | 80.57 |
| var1273 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 65.38 | 64.43 |
| var1273 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 31.78 | 65.15 |
| var2179 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 4.63 | 2.55 |
| var2179 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 1.82 | 5.02 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (403)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1273 | Sumatera Barat | 2016 | 59.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Riau | 2016 | 59.09 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Jambi | 2016 | 55.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Sumatera Selatan | 2016 | 58.36 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Bengkulu | 2016 | 64.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Lampung | 2016 | 55.60 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Kepulauan Bangka Belitung | 2016 | 69.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Jawa Tengah | 2016 | 72.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | DI Yogyakarta | 2016 | 76.72 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Jawa Timur | 2016 | 64.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Bali | 2016 | 74.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Barat | 2016 | 42.84 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Timur | 2016 | 19.63 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Kalimantan Barat | 2016 | 56.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Kalimantan Tengah | 2016 | 68.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Kalimantan Timur | 2016 | 69.61 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Sulawesi Utara | 2016 | 69.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Sulawesi Tengah | 2016 | 71.26 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Sulawesi Selatan | 2016 | 79.77 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Gorontalo | 2016 | 59.89 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Maluku | 2016 | 42.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Maluku Utara | 2016 | 43.69 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Papua Barat | 2016 | 45.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2016 | 23.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Riau | 2017 | 61.54 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Jambi | 2017 | 59.49 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Sumatera Selatan | 2017 | 65.82 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Bengkulu | 2017 | 69.25 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Lampung | 2017 | 62.81 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Kepulauan Bangka Belitung | 2017 | 79.01 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Kepulauan Riau | 2017 | 67.13 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Jawa Barat | 2017 | 64.43 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Jawa Tengah | 2017 | 73.64 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Bali | 2017 | 82.49 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Nusa Tenggara Barat | 2017 | 61.13 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Nusa Tenggara Timur | 2017 | 43.15 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Kalimantan Tengah | 2017 | 67.77 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Kalimantan Selatan | 2017 | 73.68 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Kalimantan Timur | 2017 | 69.02 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Sulawesi Selatan | 2017 | 79.28 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Maluku | 2017 | 77.70 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Maluku Utara | 2017 | 73.68 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Papua | 2017 | 32.85 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1273 | Sumatera Selatan | 2018 | 82.58 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Barat | 2018 | 83.92 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Timur | 2018 | 63.90 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Kalimantan Utara | 2018 | 86.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Maluku | 2018 | 91.26 | ke samping | outlier | tandai, nilai tidak diubah |
| var1273 | Papua Barat | 2018 | 85.26 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2018 | 37.63 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Nusa Tenggara Timur | 2019 | 51.92 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Maluku | 2019 | 75.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua Barat | 2019 | 69.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2019 | 35.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Sumatera Utara | 2020 | 67.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Timur | 2020 | 54.43 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Maluku Utara | 2020 | 80.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2020 | 36.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Nusa Tenggara Timur | 2021 | 56.33 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Sulawesi Barat | 2021 | 76.25 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2021 | 36.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Nusa Tenggara Timur | 2022 | 56.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua | 2022 | 40.91 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Nusa Tenggara Timur | 2023 | 43.50 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Kalimantan Utara | 2023 | 76.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua Barat | 2023 | 65.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Papua | 2023 | 31.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Sumatera Barat | 2024 | 86.83 | perubahan | outlier | tandai, nilai tidak diubah |
| var1273 | Nusa Tenggara Timur | 2024 | 44.06 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua | 2024 | 65.15 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1273 | Papua Selatan | 2024 | 52.48 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua Tengah | 2024 | 27.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua Pegunungan | 2024 | 4.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Nusa Tenggara Timur | 2025 | 42.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua | 2025 | 65.57 | ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua Selatan | 2025 | 47.92 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua Tengah | 2025 | 27.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1273 | Papua Pegunungan | 2025 | 5.01 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | DKI Jakarta | 2020 | 15.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | Aceh | 2021 | 14.44 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kepulauan Bangka Belitung | 2021 | 5.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | DKI Jakarta | 2021 | 15.99 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | Bali | 2021 | 11.77 | ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | Kepulauan Riau | 2022 | 15.04 | ke samping | patahan_seri | tandai; cari catatan metode |
| var2179 | Kalimantan Tengah | 2022 | 13.96 | perubahan | patahan_seri | tandai; cari catatan metode |
| var2179 | Kalimantan Selatan | 2022 | 12.82 | perubahan | patahan_seri | tandai; cari catatan metode |
| var2179 | Sulawesi Selatan | 2022 | 12.92 | perubahan | patahan_seri | tandai; cari catatan metode |
| var2179 | Kepulauan Bangka Belitung | 2023 | 6.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kepulauan Riau | 2023 | 12.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | DKI Jakarta | 2023 | 23.10 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | Jawa Tengah | 2023 | 10.83 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kalimantan Tengah | 2023 | 11.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kalimantan Selatan | 2023 | 8.70 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Gorontalo | 2023 | 4.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Sulawesi Barat | 2023 | 2.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Maluku | 2023 | 4.39 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Papua | 2023 | 1.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | DKI Jakarta | 2024 | 22.93 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | Nusa Tenggara Barat | 2024 | 6.84 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kalimantan Selatan | 2024 | 8.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Sulawesi Selatan | 2024 | 10.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Maluku Utara | 2024 | 2.76 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | Papua Barat | 2024 | 2.55 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2179 | Papua | 2024 | 5.02 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2179 | Kepulauan Bangka Belitung | 2025 | 7.61 | ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | DKI Jakarta | 2025 | 23.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2179 | Jawa Tengah | 2025 | 12.16 | ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | Bali | 2025 | 17.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var2179 | Kalimantan Barat | 2025 | 4.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var2179 | Sulawesi Utara | 2025 | 4.13 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Aceh | 2020 | 36.96 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Riau | 2020 | 32.99 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Bengkulu | 2020 | 37.36 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Lampung | 2020 | 47.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Kalimantan Selatan | 2020 | 36.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Sulawesi Utara | 2020 | 34.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Nusa Tenggara Barat | 2021 | 43.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Kalimantan Utara | 2021 | 20.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Sulawesi Barat | 2021 | 40.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Aceh | 2022 | 41.12 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | DKI Jakarta | 2022 | 30.28 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | DI Yogyakarta | 2022 | 71.88 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2741 | Jawa Timur | 2022 | 54.57 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Sulawesi Utara | 2022 | 41.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Gorontalo | 2022 | 26.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Jambi | 2023 | 51.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | DKI Jakarta | 2023 | 25.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Maluku | 2023 | 39.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Papua | 2023 | 25.86 | perubahan | outlier | tandai, nilai tidak diubah |
| var2741 | Papua Barat | 2024 | 41.63 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2741 | Papua | 2024 | 34.97 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2741 | Maluku Utara | 2025 | 48.20 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2741 | Papua Tengah | 2025 | 41.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var2749 | DKI Jakarta | 2024 | 22.93 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2749 | DKI Jakarta | 2025 | 23.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2749 | Bali | 2025 | 17.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var2749 | Sulawesi Utara | 2025 | 4.13 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 1993 | 20.13 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 1993 | 15.20 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 1993 | 45.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 1994 | 45.94 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 1994 | 59.87 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Maluku | 1994 | 44.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 1995 | 57.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 1996 | 49.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 1997 | 22.58 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 1997 | 22.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 1997 | 59.20 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 1997 | 63.88 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 1997 | 59.95 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 1999 | 63.96 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 1999 | 52.87 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 1999 | 61.84 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 2000 | 41.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 2000 | 63.43 | ke bawah | outlier | tandai, nilai tidak diubah |
| var845 | Maluku Utara | 2002 | 81.69 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var845 | Papua | 2002 | 89.63 | ke bawah + perubahan + ke samping | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var845 | Aceh | 2003 | 37.48 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kepulauan Bangka Belitung | 2003 | 31.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Maluku | 2003 | 49.94 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Maluku Utara | 2003 | 41.90 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Papua | 2003 | 35.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Gorontalo | 2004 | 39.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Aceh | 2005 | 31.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Maluku | 2005 | 60.86 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Utara | 2006 | 56.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kepulauan Riau | 2007 | 43.10 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2009 | 34.81 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Papua Barat | 2009 | 48.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Kepulauan Riau | 2010 | 23.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2010 | 28.41 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 2010 | 43.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Maluku Utara | 2010 | 54.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Utara | 2021 | 90.89 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sumatera Barat | 2021 | 83.40 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Riau | 2021 | 89.76 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Jambi | 2021 | 79.70 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sumatera Selatan | 2021 | 84.70 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Bengkulu | 2021 | 67.39 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Lampung | 2021 | 80.20 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | DKI Jakarta | 2021 | 99.86 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Jawa Barat | 2021 | 93.24 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Jawa Tengah | 2021 | 93.62 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | DI Yogyakarta | 2021 | 95.69 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Jawa Timur | 2021 | 95.02 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Banten | 2021 | 93.51 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Bali | 2021 | 97.56 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Nusa Tenggara Barat | 2021 | 94.60 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Nusa Tenggara Timur | 2021 | 85.40 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Kalimantan Barat | 2021 | 78.76 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Kalimantan Tengah | 2021 | 77.05 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Kalimantan Selatan | 2021 | 76.40 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Kalimantan Timur | 2021 | 85.80 | ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var845 | Sulawesi Utara | 2021 | 91.65 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sulawesi Tengah | 2021 | 88.51 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sulawesi Selatan | 2021 | 91.18 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sulawesi Tenggara | 2021 | 91.94 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var845 | Sumatera Utara | 2022 | 92.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Barat | 2022 | 85.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Riau | 2022 | 90.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jambi | 2022 | 79.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Selatan | 2022 | 86.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 2022 | 73.07 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 2022 | 81.60 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kepulauan Bangka Belitung | 2022 | 80.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2022 | 97.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Barat | 2022 | 93.04 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Tengah | 2022 | 93.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DI Yogyakarta | 2022 | 96.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 2022 | 95.05 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 2022 | 98.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Barat | 2022 | 95.40 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Timur | 2022 | 86.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 2022 | 80.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Tengah | 2022 | 77.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Selatan | 2022 | 76.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 2022 | 87.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Utara | 2022 | 94.15 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tengah | 2022 | 86.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Selatan | 2022 | 91.96 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tenggara | 2022 | 94.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Utara | 2023 | 92.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Barat | 2023 | 85.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Riau | 2023 | 90.47 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jambi | 2023 | 80.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Selatan | 2023 | 87.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 2023 | 73.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 2023 | 82.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2023 | 99.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Barat | 2023 | 93.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Tengah | 2023 | 93.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DI Yogyakarta | 2023 | 96.69 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 2023 | 96.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 2023 | 98.31 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Barat | 2023 | 96.03 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Timur | 2023 | 88.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 2023 | 82.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Tengah | 2023 | 77.72 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Selatan | 2023 | 76.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 2023 | 87.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Utara | 2023 | 94.37 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tengah | 2023 | 86.85 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Selatan | 2023 | 92.12 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tenggara | 2023 | 94.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Utara | 2024 | 92.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Barat | 2024 | 86.85 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Riau | 2024 | 92.24 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jambi | 2024 | 82.16 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Selatan | 2024 | 87.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 2024 | 72.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 2024 | 84.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2024 | 99.96 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Barat | 2024 | 94.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Tengah | 2024 | 95.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DI Yogyakarta | 2024 | 96.91 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 2024 | 96.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 2024 | 98.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Barat | 2024 | 96.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Timur | 2024 | 88.55 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 2024 | 82.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Tengah | 2024 | 78.71 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Selatan | 2024 | 77.34 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 2024 | 89.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Utara | 2024 | 94.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tengah | 2024 | 87.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Selatan | 2024 | 92.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tenggara | 2024 | 95.31 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Papua | 2024 | 85.84 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var845 | Papua Pegunungan | 2024 | 30.64 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var845 | Sumatera Utara | 2025 | 93.24 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Barat | 2025 | 87.26 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Riau | 2025 | 92.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jambi | 2025 | 82.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sumatera Selatan | 2025 | 86.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bengkulu | 2025 | 70.47 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Lampung | 2025 | 85.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DKI Jakarta | 2025 | 99.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Barat | 2025 | 95.84 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Tengah | 2025 | 95.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | DI Yogyakarta | 2025 | 97.33 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Jawa Timur | 2025 | 97.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Bali | 2025 | 98.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Barat | 2025 | 96.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Nusa Tenggara Timur | 2025 | 89.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Barat | 2025 | 84.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Tengah | 2025 | 80.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Selatan | 2025 | 78.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Kalimantan Timur | 2025 | 88.45 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Utara | 2025 | 94.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tengah | 2025 | 87.55 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Selatan | 2025 | 93.25 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Sulawesi Tenggara | 2025 | 94.91 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Papua | 2025 | 87.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var845 | Papua Pegunungan | 2025 | 32.89 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 1993 | 78.70 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 1993 | 40.96 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 1993 | 40.14 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 1994 | 84.82 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Kalimantan Barat | 1994 | 7.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 1995 | 57.52 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 1995 | 42.54 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 1995 | 42.19 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 1996 | 66.82 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 1996 | 43.13 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 1996 | 50.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Kalimantan Timur | 1996 | 39.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 1997 | 57.92 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 1997 | 56.10 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Nusa Tenggara Barat | 1997 | 30.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Kalimantan Tengah | 1997 | 10.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Kalimantan Timur | 1997 | 33.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 1998 | 56.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 1998 | 50.30 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 1998 | 59.32 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 1999 | 72.50 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 1999 | 52.32 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 1999 | 58.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 2000 | 66.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2000 | 64.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 2001 | 73.01 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 2001 | 57.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 2001 | 59.58 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Aceh | 2002 | 93.97 | ke bawah | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var847 | DKI Jakarta | 2002 | 76.10 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Maluku | 2002 | 39.49 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var847 | Maluku Utara | 2002 | 67.81 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var847 | Papua | 2002 | 32.93 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var847 | Aceh | 2003 | 30.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 2003 | 68.82 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2003 | 61.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Maluku | 2003 | 23.48 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Maluku Utara | 2003 | 33.93 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2003 | 17.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 2004 | 71.46 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DI Yogyakarta | 2004 | 61.91 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 2004 | 63.08 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Kepulauan Riau | 2006 | 34.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | DKI Jakarta | 2006 | 65.21 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2006 | 61.16 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 2007 | 74.49 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2007 | 74.10 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 2008 | 75.61 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2008 | 77.13 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | DKI Jakarta | 2009 | 80.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bali | 2009 | 75.95 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Nusa Tenggara Timur | 2009 | 14.98 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Kepulauan Riau | 2010 | 72.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Sulawesi Barat | 2010 | 41.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua Barat | 2011 | 39.23 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DI Yogyakarta | 2012 | 84.01 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 2012 | 82.71 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua Barat | 2012 | 55.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2012 | 26.97 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Papua Barat | 2013 | 49.06 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2013 | 27.89 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Aceh | 2014 | 33.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Riau | 2014 | 48.74 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Nusa Tenggara Timur | 2014 | 16.12 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Papua Barat | 2014 | 61.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Aceh | 2015 | 54.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Nusa Tenggara Timur | 2015 | 23.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Kalimantan Barat | 2015 | 39.78 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Riau | 2016 | 71.36 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Nusa Tenggara Timur | 2016 | 40.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Kalimantan Utara | 2016 | 64.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2016 | 31.43 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2017 | 42.71 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Kepulauan Riau | 2017 | 86.33 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2017 | 33.06 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2018 | 44.31 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 2018 | 91.14 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua | 2018 | 33.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2019 | 75.91 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | Lampung | 2019 | 79.22 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | DI Yogyakarta | 2019 | 94.67 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | Bali | 2019 | 94.59 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | Kalimantan Barat | 2019 | 72.08 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | Papua | 2019 | 38.27 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var847 | Bengkulu | 2020 | 78.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | DI Yogyakarta | 2020 | 96.96 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2020 | 40.31 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2021 | 79.81 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | DI Yogyakarta | 2021 | 97.12 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bali | 2021 | 95.95 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua | 2021 | 40.81 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2022 | 79.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | Kepulauan Riau | 2022 | 87.74 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | DI Yogyakarta | 2022 | 96.21 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Papua Barat | 2022 | 73.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2022 | 40.34 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2023 | 80.28 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2023 | 43.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var847 | Bengkulu | 2024 | 83.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2024 | 80.57 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var847 | Papua Selatan | 2024 | 60.85 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua Tengah | 2024 | 41.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua Pegunungan | 2024 | 12.61 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Bengkulu | 2025 | 85.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var847 | Kalimantan Barat | 2025 | 88.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var847 | Papua | 2025 | 76.71 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var847 | Papua Selatan | 2025 | 65.06 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua Tengah | 2025 | 39.73 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var847 | Papua Pegunungan | 2025 | 16.34 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1273 | 358 | 358 | 358 | 0 | 0 | 0 | Persen |
| var2179 | 648 | 648 | 648 | 0 | 0 | 0 | Persen |
| var2741 | 218 | 218 | 218 | 0 | 0 | 0 | Persen |
| var2749 | 76 | 76 | 76 | 0 | 0 | 0 | Persen |
| var845 | 722 | 722 | 722 | 0 | 0 | 0 | Persen |
| var847 | 1036 | 1036 | 1036 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
