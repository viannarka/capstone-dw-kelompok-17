# Sprint 2 · Tim Nexora · 23–29 November 2026

## Sprint Goal

Pengguna dapat menjalankan satu pipeline untuk membandingkan indikator air minum dan sanitasi antarprovinsi dan antarsumber nasional. Setiap nilai dapat ditelusuri ke Silver, jumlah baris Silver dan Gold di DuckDB cocok dengan Parquet, dan perbedaan angka BPS, WHO, serta WDI dapat dijelaskan dari metadata.

## Bukti untuk kartu #27

| Definition of Done | Hasil yang dapat diperiksa | Jejak GitHub untuk Papan Tim |
|---|---|---|
| Panel Gold provinsi × periode × indikator | Panel lebar berisi 1.035 baris provinsi–tahun. Panel panjang berisi 2.893 observasi dengan seri asal dan rincian. | [Pembentukan panel](https://github.com/viannarka/capstone-dw-kelompok-17/pull/30) |
| Silver dan Gold tersimpan di SQL dengan kunci primer dan alasan pemilihan | DuckDB memuat 3.242 baris Silver. Pipeline memeriksa jumlah baris tiap tabel terhadap Parquet. Bagian *Data dan lineage* pada laporan tim menjelaskan pemilihan DuckDB. | [Skema dan pemuatan SQL](https://github.com/viannarka/capstone-dw-kelompok-17/pull/32) |
| Rekonsiliasi nasional menyertakan penjelasan selisih | Dari 144 baris, 53 memiliki kedua nilai, 77 hanya satu sisi, dan 14 memuat konteks pendanaan. Median selisih bertanda adalah −0,0218 poin persentase. | [Tabel dan bukti penjelasan](https://github.com/viannarka/capstone-dw-kelompok-17/pull/33) · [Validasi Gold](https://github.com/viannarka/capstone-dw-kelompok-17/pull/34) |

## Log anggota dan penutupan sprint

Draf log mengikuti format tiga baris Sprint 1. Tiap anggota meninjau isinya sebelum mengisi Log Sprint resmi pada kartu pribadi. Tenggat log 30 November pukul 23.59 WIB.

- [Salavi Naharani · 124450090](124450090.md)
- [Asri Meilani · 124450010](124450010.md)
- [Azzelya Thianandry · 124450041](124450041.md)
- [Ayu Andriani · 124450058](124450058.md)
- [Favian Arkaanda · 124450021](124450021.md)
- [Abdul Hakim MT · 124450057](124450057.md)

[Catatan standup](standup.md) · [Naskah Demo Sprint 2 dan hasil uji reproduksi](DEMO.md)
