# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih per pembanding tersimpan di `data/gold/rekonsiliasi.parquet` (nilai utama dikurangi pembanding, dalam poin persentase).

Tabel nasional Gold (satu baris per periode x seri, dengan kolom asal angka dan _berkas_raw): `data/gold/tabel_nasional.parquet` dan `data/gold/gold_nasional.parquet`.

Tabel nasional lebar (periode x seri, rincian total): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

Seluruh periode pada salah satu sisi dipertahankan. Dari 144 baris, 53 memiliki kedua nilai. Median selisih bertanda adalah -0.0218 poin persentase. Periode tanpa pasangan dan P5 memiliki selisih kosong.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var2741 | WSH_WATER_SAFELY_MANAGED [total], SH.H2O.SMDW.ZS [total] | selisih | 3 | 2020, 2021, 2022 | definisi berbeda |
| P2 | var845 | SH.H2O.BASW.ZS [total] | selisih | 15 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2021, 2022, 2023, 2024 | definisi berbeda |
| P3 | var1273 | WSH_HYGIENE_BASIC [total] | selisih | 7 | 2016, 2017, 2018, 2019, 2020, 2021, 2022 | definisi berbeda |
| P4 | WSH_WATER_SAFELY_MANAGED | SH.H2O.SMDW.ZS [total] | selisih | 23 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 | vintage berbeda |
| P5 | SDGODAWS | — | konteks | 0 | — | definisi berbeda: uang, bukan cakupan layanan |

## Rincian per pasangan

### P1: Air minum aman: BPS (rumah tangga) vs WHO dan WDI (penduduk)
- Seri utama: `var2741` (rincian `total`)
- Pembanding: `WSH_WATER_SAFELY_MANAGED` (rincian `total`), `SH.H2O.SMDW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2020, 2021, 2022
- Penjelasan: definisi berbeda

Pertanyaan keterbandingan dan jawabannya:

1. **Konsepnya sama?** Ya, dikelola secara aman (var.label 6.1.1*; DefinitionText WHO).
2. **Yang dihitung?** BPS: persentase rumah tangga. WHO/WDI: persentase penduduk.
Metadata BPS var2741 memakai rumah tangga. WHO DefinitionText dan WDI sourceNote mengukur penduduk pengguna layanan air aman.

### P2: Air minum layak (BPS) vs setidaknya dasar (WDI)
- Seri utama: `var845` (rincian `total`)
- Pembanding: `SH.H2O.BASW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2021, 2022, 2023, 2024
- Penjelasan: definisi berbeda

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah layak = basic?** Belum tentu: basic mensyaratkan waktu ambil air (sourceNote WDI); judul BPS tidak menyebutnya.
2. **Tahun mana yang aman dibandingkan?** Sesudah 2011 rumus BPS berubah; 2000–2010 dan 2021–2024 dianalisis terpisah.
BPS var845 mengukur rumah tangga dengan air layak dan mencatat perubahan rumus pada 2011. WDI sourceNote mensyaratkan sumber layak dengan waktu ambil pulang-pergi maksimal 30 menit untuk basic; kedua indikator tidak setara.

### P3: Cuci tangan dengan sabun dan air: BPS vs WHO
- Seri utama: `var1273` (rincian `total`)
- Pembanding: `WSH_HYGIENE_BASIC` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2016, 2017, 2018, 2019, 2020, 2021, 2022
- Penjelasan: definisi berbeda

Pertanyaan keterbandingan dan jawabannya:

1. **Tahun 2016 sebanding?** Sumbernya modul MKP, bukan KOR Maret; ditandai patahan sumber.
Label BPS var1273 memakai rumah tangga. WHO DefinitionText menghitung penduduk dalam rumah tangga dengan fasilitas cuci tangan, sabun, dan air.

### P4: Air minum aman: WHO vs WDI (keduanya JMP)
- Seri utama: `WSH_WATER_SAFELY_MANAGED` (rincian `total`)
- Pembanding: `SH.H2O.SMDW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
- Penjelasan: vintage berbeda

Pertanyaan keterbandingan dan jawabannya:

1. **Sumbernya sama?** Ya, WHO/UNICEF JMP (sourceOrganization WDI).
Metadata WHO DataUpdateLast bertanggal 10 Juli 2023. WDI sourceOrganization mencantumkan publikasi JMP 25 Agustus 2025. Kedua publikasi memakai edisi data berbeda.

### P5: Bantuan pembangunan air dan sanitasi (WHO): konteks
- Seri utama: `SDGODAWS` (rincian `total`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Penjelasan: definisi berbeda: uang, bukan cakupan layanan

Pertanyaan keterbandingan dan jawabannya:

1. **Satuan?** Juta USD konstan 2024 (odata IndicatorName), bukan persen.
WHO SDGODAWS mengukur bantuan pembangunan dalam juta USD konstan 2024. Nilainya disajikan sebagai konteks pendanaan.
