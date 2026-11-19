# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg6_6_1_1_v2741.json | bps_json | data | 218 | 2 halaman |
| bps/2026-10-17/json/sdg6_6_2_1_v2749.json | bps_json | data | 76 | 1 halaman |
| bps/2026-10-17/json/sdg6_air_layak.json | bps_json | data | 722 | 8 halaman |
| bps/2026-10-17/json/sdg6_cuci_tangan.json | bps_json | data | 358 | 4 halaman |
| bps/2026-10-17/json/sdg6_sanitasi_aman.json | bps_json | data | 648 | 2 halaman |
| bps/2026-10-17/json/sdg6_sanitasi_layak.json | bps_json | data | 1036 | 11 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg6_6_1_1_v2741.csv | bps_csv | data | 218 |  |
| bps/2026-10-17/sdg6_6_2_1_v2749.csv | bps_csv | data | 76 |  |
| bps/2026-10-17/sdg6_air_layak.csv | bps_csv | data | 722 |  |
| bps/2026-10-17/sdg6_cuci_tangan.csv | bps_csv | data | 358 |  |
| bps/2026-10-17/sdg6_sanitasi_aman.csv | bps_csv | data | 648 |  |
| bps/2026-10-17/sdg6_sanitasi_layak.csv | bps_csv | data | 1036 |  |
| wdi/2026-10-20/data/kelompok-05-hal-01.json | wdi_data | data | 132 | 3,960 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| who_gho/2026-10-20/datadot/1548EA3_WSH_WATER_SAFELY_MANAGED.csv | who_csv | data | 69 |  |
| who_gho/2026-10-20/datadot/4AF995F_SDGODAWS.csv | who_csv | data | 14 |  |
| who_gho/2026-10-20/datadot/D1223E8_WSH_HYGIENE_BASIC.csv | who_csv | data | 51 |  |
| who_gho/2026-10-20/datadot/ddiindicators_skip0000.json | who_ddi | meta | 3 | definisi lengkap seri kasus |
| who_gho/2026-10-20/odata/Indicator.json | who_odata | meta | 3 |  |

Jumlah: 22 berkas dari 22 di MANIFEST, 6,382 baris mentah di berkas data.
