# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1273 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1273 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1273 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2179 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2179 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2179 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2179 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2179 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2179 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2741 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2741 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2741 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2741 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2741 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2741 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2749 | 2024 | 38 | 37 | 38 | 97.40 | 97.40 |
| var2749 | 2025 | 38 | 37 | 38 | 97.40 | 97.40 |
| var845 | 1993 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1994 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1995 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1996 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1997 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1998 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 1999 | 38 | 26 | 26 | 68.40 | 100.00 |
| var845 | 2000 | 38 | 24 | 24 | 63.20 | 100.00 |
| var845 | 2001 | 38 | 29 | 29 | 76.30 | 100.00 |
| var845 | 2002 | 38 | 30 | 30 | 78.90 | 100.00 |
| var845 | 2003 | 38 | 30 | 30 | 78.90 | 100.00 |
| var845 | 2004 | 38 | 30 | 30 | 78.90 | 100.00 |
| var845 | 2005 | 38 | 31 | 31 | 81.60 | 100.00 |
| var845 | 2006 | 38 | 33 | 33 | 86.80 | 100.00 |
| var845 | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| var845 | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| var845 | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| var845 | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| var845 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var845 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var845 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var845 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var845 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var847 | 1993 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1994 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1995 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1996 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1997 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1998 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 1999 | 38 | 26 | 26 | 68.40 | 100.00 |
| var847 | 2000 | 38 | 24 | 24 | 63.20 | 100.00 |
| var847 | 2001 | 38 | 29 | 29 | 76.30 | 100.00 |
| var847 | 2002 | 38 | 30 | 30 | 78.90 | 100.00 |
| var847 | 2003 | 38 | 30 | 30 | 78.90 | 100.00 |
| var847 | 2004 | 38 | 30 | 30 | 78.90 | 100.00 |
| var847 | 2006 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| var847 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var847 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var847 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | missing | terisi | tidak_diterbitkan |
|---|---|---|---|---|---|
| var1273 | 4 | 28 | 0 | 348 | 0 |
| var2179 | 4 | 12 | 0 | 212 | 0 |
| var2741 | 4 | 12 | 0 | 212 | 0 |
| var2749 | 0 | 0 | 2 | 74 | 0 |
| var845 | 9 | 162 | 0 | 699 | 4 |
| var847 | 9 | 199 | 0 | 1004 | 4 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var845 | 1993 | terisi |  |
| var845 | 1994 | terisi |  |
| var845 | 1995 | terisi |  |
| var845 | 1996 | terisi |  |
| var845 | 1997 | terisi |  |
| var845 | 1998 | terisi |  |
| var845 | 1999 | terisi |  |
| var845 | 2000 | terisi |  |
| var845 | 2001 | terisi |  |
| var845 | 2002 | terisi |  |
| var845 | 2003 | terisi |  |
| var845 | 2004 | terisi |  |
| var845 | 2005 | terisi |  |
| var845 | 2006 | terisi |  |
| var845 | 2007 | terisi |  |
| var845 | 2008 | terisi |  |
| var845 | 2009 | terisi |  |
| var845 | 2010 | terisi |  |
| var845 | 2021 | terisi |  |
| var845 | 2022 | terisi |  |
| var845 | 2023 | terisi |  |
| var845 | 2024 | terisi |  |
| var845 | 2025 | terisi |  |
| var2741 | 2020 | terisi |  |
| var2741 | 2021 | terisi |  |
| var2741 | 2022 | terisi |  |
| var2741 | 2023 | terisi |  |
| var2741 | 2024 | terisi |  |
| var2741 | 2025 | terisi |  |
| var847 | 1993 | terisi |  |
| var847 | 1994 | terisi |  |
| var847 | 1995 | terisi |  |
| var847 | 1996 | terisi |  |
| var847 | 1997 | terisi |  |
| var847 | 1998 | terisi |  |
| var847 | 1999 | terisi |  |
| var847 | 2000 | terisi |  |
| var847 | 2001 | terisi |  |
| var847 | 2002 | terisi |  |
| var847 | 2003 | terisi |  |
| var847 | 2004 | terisi |  |
| var847 | 2006 | terisi |  |
| var847 | 2007 | terisi |  |
| var847 | 2008 | terisi |  |
| var847 | 2009 | terisi |  |
| var847 | 2010 | terisi |  |
| var847 | 2011 | terisi |  |
| var847 | 2012 | terisi |  |
| var847 | 2013 | terisi |  |
| var847 | 2014 | terisi |  |
| var847 | 2015 | terisi |  |
| var847 | 2016 | terisi |  |
| var847 | 2017 | terisi |  |
| var847 | 2018 | terisi |  |
| var847 | 2019 | terisi |  |
| var847 | 2020 | terisi |  |
| var847 | 2021 | terisi |  |
| var847 | 2022 | terisi |  |
| var847 | 2023 | terisi |  |
| var847 | 2024 | terisi |  |
| var847 | 2025 | terisi |  |
| var1273 | 2016 | terisi |  |
| var1273 | 2017 | terisi |  |
| var1273 | 2018 | terisi |  |
| var1273 | 2019 | terisi |  |
| var1273 | 2020 | terisi |  |
| var1273 | 2021 | terisi |  |
| var1273 | 2022 | terisi |  |
| var1273 | 2023 | terisi |  |
| var1273 | 2024 | terisi |  |
| var1273 | 2025 | terisi |  |
| var2179 | 2020 | terisi |  |
| var2179 | 2021 | terisi |  |
| var2179 | 2022 | terisi |  |
| var2179 | 2023 | terisi |  |
| var2179 | 2024 | terisi |  |
| var2179 | 2025 | terisi |  |
| var2749 | 2024 | terisi |  |
| var2749 | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1273 | nasional | 2016 | 2025 | 10 |
| var1273 | provinsi | 2016 | 2025 | 10 |
| var2179 | nasional | 2020 | 2025 | 6 |
| var2179 | provinsi | 2020 | 2025 | 6 |
| var2741 | nasional | 2020 | 2025 | 6 |
| var2741 | provinsi | 2020 | 2025 | 6 |
| var2749 | nasional | 2024 | 2025 | 2 |
| var2749 | provinsi | 2024 | 2025 | 2 |
| var845 | nasional | 1993 | 2025 | 23 |
| var845 | provinsi | 1993 | 2025 | 23 |
| var847 | nasional | 1993 | 2025 | 32 |
| var847 | provinsi | 1993 | 2025 | 32 |

Provinsi yang belum ada pada sebagian periode panel: Banten, Gorontalo, Kalimantan Utara, Kepulauan Bangka Belitung, Kepulauan Riau, Maluku Utara, Papua Barat, Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah, Sulawesi Barat.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.

## Garis waktu konsep

Seri mana berlaku pada periode berapa. Seri kanonik per konsep per tahun dipilih di Gold (Sprint 2); Silver menyimpan semua seri apa adanya.

| konsep | seri_kode | periode_pertama | periode_terakhir | jumlah_periode | tahun_tidak_terbit | definisi_berganti |
|---|---|---|---|---|---|---|
| air minum aman | var2741 | 2020 | 2025 | 6 | — | — |
| air minum layak | var845 | 1993 | 2025 | 23 | 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020 | mulai 2021 |
| cuci tangan | var1273 | 2016 | 2025 | 10 | — | mulai 2017 |
| sanitasi aman | var2179 | 2020 | 2025 | 6 | — | — |
| sanitasi aman | var2749 | 2024 | 2025 | 2 | — | — |
| sanitasi layak | var847 | 1993 | 2025 | 32 | 2005 | mulai 2019 |
