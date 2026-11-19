# Data dictionary — Kasus 17 Air minum, sanitasi, dan kebersihan

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (3,242 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | satuan | kosong | rentang_atau_nilai | arti | asal |
|---|---|---|---|---|---|---|
| sumber | str | — | 0 | bps, wdi, who_gho | lembaga penerbit / produsen data mentah | nama folder sumber di data/raw/ (bps, wdi, who_gho) |
| seri_kode | str | — | 0 | SDGODAWS, SH.H2O.BASW.ZS, SH.H2O.SMDW.ZS, WSH_HYGIENE_BASIC, WSH_WATER_SAFELY_MANAGED, var1273, … (11 nilai) | identitas unik seri indikator; rincian lengkap di docs/seri.csv | kode seri di sumbernya (BPS: 'var' + var.val; WDI: Series; WHO: nama berkas/indikator) |
| wilayah_kode | int64 | — | 0 | 1100 – 9999 | kode wilayah baku (kode BPS dua digit x 100 untuk 38 provinsi; 9999 untuk Indonesia) | kamus src/wilayah.py; pemetaan ISO/M49 ke 9999; keputusan log K-001 |
| nama_wilayah | str | — | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | nama baku susunan 38 provinsi Indonesia 2025 atau 'Indonesia' | kamus src/wilayah.py |
| periode | str | tahun | 0 | 1993, 1994, 1995, 1996, 1997, 1998, … (33 nilai) | waktu pengamatan dalam bentuk baku ISO (YYYY) | tahun/turtahun BPS, date WDI, DIM_TIME WHO |
| jenis_periode | str | — | 0 | tahun | tingkat granularitas waktu: tahun, semester, triwulan, atau bulan | diturunkan dari periode dan turtahun BPS |
| rincian | str | — | 0 | daerah=RURAL, daerah=URBAN, total | kategori disagregasi: 'total' untuk agregat, atau 'dimensi=kode' (mis. daerah=URBAN, daerah=RURAL) | turvar BPS (var2179); kolom DIM_* WHO; keputusan log K-005, K-011 |
| nilai | float64 | mengikuti kolom satuan (persen atau juta_usd_konstan_2024) | 0 | 0.34 – 266.225 | angka observasi riil sesuai satuan (tidak ada nilai kosong di Silver) | datacontent BPS; value WDI; RATE_*_N dan MONEY_N WHO |
| satuan | str | — | 0 | juta_usd_konstan_2024, persen | satuan baku pengukuran angka observasi; satu satuan per seri | var.unit BPS, sourceNote WDI, OData Indicator WHO; keputusan log K-014 |
| sdg_kode | str | — | 0 | 1.4.1, 6.1.1, 6.2.1, 6.a.1 | kode klasifikasi target/indikator SDG (1.4.1, 6.1.1, 6.2.1, 6.a.1) | katalog sumber & judul berkas mentah; koreksi var847 di log K-009; log K-015, K-016 |
| batas_bawah | float64 | persen | 3242 | — | batas bawah selang kepercayaan/ketidakpastian; kosong bila tidak ada | kolom RATE_*_NL pada CSV WHO GHO |
| batas_atas | float64 | persen | 3242 | — | batas atas selang kepercayaan/ketidakpastian; kosong bila tidak ada | kolom RATE_*_NU pada CSV WHO GHO |
| rujukan_tahun | Int64 | tahun | 3242 | — | lebar jendela rujukan survei sebelum tahun pencatatan; kosong jika tidak berlaku | var.note BPS; keputusan log K-012, K-013 |
| _berkas_raw | str | — | 0 | bps/2026-10-17/json/sdg6_6_1_1_v2741.json, bps/2026-10-17/json/sdg6_6_2_1_v2749.json, bps/2026-10-17/json/sdg6_air_layak.json, bps/2026-10-17/json/sdg6_cuci_tangan.json, bps/2026-10-17/json/sdg6_sanitasi_aman.json, bps/2026-10-17/json/sdg6_sanitasi_layak.json, … (10 nilai) | lineage/provenans: berkas asal sumber baris data ini | jalur berkas mentah relatif data/raw/ dari modul ekstraksi |
| _sha256_raw | str | — | 0 | 1f34d5dffa782a45a3e9dc9dced654062335dd8cb013b34713af5e5e98a74072, 3b8b87a62df46405d4fad99058322b09d4675d93c948a0162e0edb644c508bca, 54157cd9f8bebd2f2fa31ebcd826dbb710192a94e742200c3f0c338a673232be, 91e7af0308c7368883c65a217390a0fea456913a0f74488dba2d5a6e068e8402, a42896e397c10d04d7c2f025a9ab572ddc6e6adbc35c84aafc067d43796632f4, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e, … (10 nilai) | lineage: sidik digital kriptografis SHA-256 berkas mentah asal | src.common.manifest.sha256_raw diverifikasi terhadap data/raw/MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `daerah` (var2179, dari turvar BPS): `URBAN` = Perkotaan, `RURAL` = Perdesaan

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | WSH_HYGIENE_BASIC, WSH_WATER_SAFELY_MANAGED, var2179 |
| daerah=URBAN | WSH_HYGIENE_BASIC, WSH_WATER_SAFELY_MANAGED, var2179 |
| total | SDGODAWS, SH.H2O.BASW.ZS, SH.H2O.SMDW.ZS, WSH_HYGIENE_BASIC, WSH_WATER_SAFELY_MANAGED, var1273, var2179, var2741, var2749, var845, var847 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var845 | persen | 6.1.1 | satuan analisis rumah tangga; Susenas; 1993–2010 dan 2021–2025; rumus baru mulai 2011 (var.def d) | var.unit: 'Persen' |
| var2741 | persen | 6.1.1 | satuan analisis rumah tangga; 2020–2025 | var.unit: 'Persen' |
| var847 | persen | 6.2.1 | satuan analisis rumah tangga; Susenas; 1993–2025 tanpa 2005; konsep metadata SDGs sejak 2019 (var.def d) | var.unit: 'Persen' |
| var1273 | persen | 6.2.1 | satuan analisis rumah tangga; 2016 dari Susenas MKP, sesudahnya Susenas Maret (var.note) | var.unit: 'Persen' |
| var2179 | persen | 6.2.1 | satuan analisis rumah tangga; rincian perkotaan, perdesaan, dan gabungan; 2020–2025 | var.unit: 'Persen' |
| var2749 | persen | 6.2.1 | satuan analisis rumah tangga; 2024–2025; nilainya sama dengan var2179 gabungan (log K-011); Papua Pegunungan tidak ada | var.unit: 'Persen' |
| SH.H2O.SMDW.ZS | persen | 6.1.1 | satuan analisis penduduk; WHO/UNICEF JMP | name: '(% of population)' |
| SH.H2O.BASW.ZS | persen | 1.4.1 | satuan analisis penduduk; basic + safely managed; JMP | name: '(% of population)' |
| WSH_WATER_SAFELY_MANAGED | persen | 6.1.1 | satuan analisis penduduk; rincian perkotaan/perdesaan | kolom PERCENT_POP_N |
| WSH_HYGIENE_BASIC | persen | 6.2.1 | satuan analisis penduduk; rincian perkotaan/perdesaan | kolom PERCENT_POP_N |
| SDGODAWS | juta_usd_konstan_2024 | 6.a.1 | bantuan pembangunan resmi, bukan cakupan layanan | kolom MONEY_N; odata IndicatorName '(constant 2024 US$ millions)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | nama_wilayah | periode | rincian | nilai | satuan | sdg_kode | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|---|---|---|
| bps | var1273 | 1100 | Aceh | 2016 | total | 54.39 | persen | 6.2.1 | bps/2026-10-17/json/sdg6_cuci_tangan.json | d67d8f74e290108b3ccca8ddc077b051c8d5c5c7835bb1202c42c246e03cd5d4 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg6_cuci_tangan.json`. Berkas ini merupakan snapshot resmi WebAPI BPS 17 Oktober 2026.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `d67d8f74e290108b3ccca8ddc077b051c8d5c5c7835bb1202c42c246e03cd5d4`; nilainya identik dengan `_sha256_raw`, membuktikan integritas berkas mentah tidak mengalami perubahan.

3. Di berkas mentah, nilai ditemukan pada array halaman 1, dictionary `datacontent` dengan kunci `1100127301160` (nilai `54.39`). Kunci ini diurai oleh `src/ekstraksi/bps.py` menjadi: wilayah_kode 1100 (Aceh), var 1273, turvar 0 (total), kode tahun 116 (2016), dan turtahun 0 (tahunan).

4. Kaitan dengan metadata & log: `sdg_kode` 6.2.1 diperoleh dari `var.label` berkas mentah; satuan `persen` sesuai `var.unit`; dan konteks instrumen Susenas MKP 2016 dicatat pada `var.note` (keputusan log K-004 dan K-019).
