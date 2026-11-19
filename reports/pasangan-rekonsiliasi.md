# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var2741 | WSH_WATER_SAFELY_MANAGED [total], SH.H2O.SMDW.ZS [total] | selisih | 3 | 2020, 2021, 2022 | definisi (satuan analisis rumah tangga vs penduduk) dan metode (JMP memodelkan dari banyak survei) |
| P2 | var845 | SH.H2O.BASW.ZS [total] | selisih | 15 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2021, 2022, 2023, 2024 | definisi (layak vs basic: syarat waktu ambil air ≤ 30 menit di WDI; rumus BPS berganti 2011) |
| P3 | var1273 | WSH_HYGIENE_BASIC [total] | selisih | 7 | 2016, 2017, 2018, 2019, 2020, 2021, 2022 | definisi (rumah tangga vs penduduk); 2016 dari Susenas MKP |
| P4 | WSH_WATER_SAFELY_MANAGED | SH.H2O.SMDW.ZS [total] | selisih | 23 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022 | vintage |
| P5 | SDGODAWS | — | konteks | 0 | — | definisi berbeda: uang, bukan cakupan layanan |

## Rincian per pasangan

### P1: Air minum aman: BPS (rumah tangga) vs WHO dan WDI (penduduk)
- Seri utama: `var2741` (rincian `total`)
- Pembanding: `WSH_WATER_SAFELY_MANAGED` (rincian `total`), `SH.H2O.SMDW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2020, 2021, 2022
- Dugaan kategori selisih (diuji di Sprint 2): definisi (satuan analisis rumah tangga vs penduduk) dan metode (JMP memodelkan dari banyak survei)

Pertanyaan keterbandingan dan jawabannya:

1. **Konsepnya sama?** Ya, dikelola secara aman (var.label 6.1.1*; DefinitionText WHO).
2. **Yang dihitung?** BPS: persentase rumah tangga. WHO/WDI: persentase penduduk.

### P2: Air minum layak (BPS) vs setidaknya dasar (WDI)
- Seri utama: `var845` (rincian `total`)
- Pembanding: `SH.H2O.BASW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2021, 2022, 2023, 2024
- Dugaan kategori selisih (diuji di Sprint 2): definisi (layak vs basic: syarat waktu ambil air ≤ 30 menit di WDI; rumus BPS berganti 2011)

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah layak = basic?** Belum tentu: basic mensyaratkan waktu ambil air (sourceNote WDI); judul BPS tidak menyebutnya.
2. **Tahun mana yang aman dibandingkan?** Sesudah 2011 rumus BPS berubah; 2000–2010 dan 2021–2024 dianalisis terpisah.

### P3: Cuci tangan dengan sabun dan air: BPS vs WHO
- Seri utama: `var1273` (rincian `total`)
- Pembanding: `WSH_HYGIENE_BASIC` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2016, 2017, 2018, 2019, 2020, 2021, 2022
- Dugaan kategori selisih (diuji di Sprint 2): definisi (rumah tangga vs penduduk); 2016 dari Susenas MKP

Pertanyaan keterbandingan dan jawabannya:

1. **Tahun 2016 sebanding?** Sumbernya modul MKP, bukan KOR Maret; ditandai patahan sumber.

### P4: Air minum aman: WHO vs WDI (keduanya JMP)
- Seri utama: `WSH_WATER_SAFELY_MANAGED` (rincian `total`)
- Pembanding: `SH.H2O.SMDW.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022
- Dugaan kategori selisih (diuji di Sprint 2): vintage

Pertanyaan keterbandingan dan jawabannya:

1. **Sumbernya sama?** Ya, WHO/UNICEF JMP (sourceOrganization WDI).

### P5: Bantuan pembangunan air dan sanitasi (WHO): konteks
- Seri utama: `SDGODAWS` (rincian `total`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: uang, bukan cakupan layanan

Pertanyaan keterbandingan dan jawabannya:

1. **Satuan?** Juta USD konstan 2024 (odata IndicatorName), bukan persen.
