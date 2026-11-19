# Hasil validasi Silver

Dihasilkan `python pipeline.py` (`src/validasi/`). Aturan keras menghentikan pipeline bila gagal; peringatan dilaporkan untuk diperiksa manusia. Aturan juga diuji dengan baris yang sengaja dirusak (`pytest`, berkas `tests/test_validasi.py`).

| aturan | jenis | keterangan | hasil |
|---|---|---|---|
| kolom dan tipe | keras (umum) | setiap kolom ada dengan tipe yang benar; nilai tidak kosong | LOLOS |
| rincian_dari_kamus | keras (umum) | rincian 'total' atau 'dimensi=kode' dengan dimensi/kode dari kamus konfigurasi | LOLOS |
| satu_satuan_per_seri | keras (umum) | satu seri hanya punya satu satuan | LOLOS |
| nilai_dalam_rentang_satuan | keras (umum) | nilai berada di rentang sah satuannya (persen 0–100, per 1.000 0–1.000, ...) | LOLOS |
| batas_bawah_le_nilai_le_batas_atas | keras (umum) | untuk baris yang punya batas: batas bawah ≤ nilai ≤ batas atas | LOLOS |
| kunci unik | keras (umum) | kombinasi sumber + seri_kode + wilayah_kode + periode + rincian + _berkas_raw tidak kembar | LOLOS |
| wilayah dan periode | keras (umum) | wilayah_kode dari kamus 38 provinsi + 9999; periode berbentuk baku | LOLOS |
| tujuan_sdg_sesuai_nama_berkas | keras (kasus) | tujuan SDG setiap seri BPS sama dengan angka di nama berkasnya (sdgN_) | LOLOS |
| dua_tabel_sanitasi_aman_sama | keras (kasus) | var2749 = var2179 gabungan pada sel yang sama | LOLOS |
| total_di_antara_kota_desa | keras (kasus) | sanitasi aman gabungan di antara perkotaan dan perdesaan | LOLOS |
| kota_tidak_lebih_rendah | peringatan (kasus) | sanitasi aman perkotaan < perdesaan (peringatan) | PERINGATAN (4 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### kota_tidak_lebih_rendah

| wilayah_kode | periode | daerah=RURAL | daerah=URBAN | total |
|---|---|---|---|---|
| 2100 | 2022 | 16.52 | 14.87 | 15.04 |
| 7600 | 2024 | 2.54 | 1.79 | 2.39 |
| 8100 | 2021 | 2.39 | 2.25 | 2.33 |
| 8200 | 2023 | 1.67 | 1.53 | 1.63 |
