# Kelengkapan Panel 38 Provinsi × Periode

## 1. Tujuan

Analisis ini dilakukan untuk memeriksa kelengkapan data indikator air minum dan sanitasi pada tingkat provinsi berdasarkan periode penerbitan masing-masing seri. Pemeriksaan dilakukan dengan membentuk grid provinsi × periode agar wilayah dan periode yang tidak memiliki observasi tetap dapat teridentifikasi.

## 2. Sumber dan cakupan data

Data observasi menggunakan berkas CSV BPS hasil ekstraksi. Berkas JSON tidak dihitung sebagai observasi tambahan agar tidak terjadi penghitungan ganda.

Grid dibentuk berdasarkan enam seri BPS:
- `var845`: Air Minum Layak
- `var847`: Sanitasi Layak
- `var1273`: Cuci Tangan
- `var2179`: Sanitasi Aman
- `var2741`: Air Minum Aman
- `var2749`: Air Minum Aman

Struktur grid mencakup 38 provinsi dan periode yang ditemukan pada data observasi. Baris agregat Indonesia dipisahkan dari perhitungan kelengkapan tingkat provinsi.

## 3. Hasil pembentukan grid

Hasil pengujian grid sementara menghasilkan:
- Total sel grid: 3.081
- Sel tingkat provinsi: 3.002
- Sel terisi: 2.549
- Sel kosong: 453

Klasifikasi sel kosong:
| Kategori | Jumlah |
|---|---:|
| `belum_ada` | 413 |
| `batas_lama` | 30 |
| `tidak_diterbitkan` | 8 |
| `missing` | 2 |
| **Total** | **453** |

## 4. Kelengkapan panel per seri

| Seri | Sel Terisi | Total Sel | Kelengkapan |
|---|---:|---:|---:|
| var1273 | 348 | 380 | 91,58% |
| var2179 | 212 | 228 | 92,98% |
| var2741 | 212 | 228 | 92,98% |
| var2749 | 74 | 76 | 97,37% |
| var845 | 699 | 874 | 79,98% |
| var847 | 1.004 | 1.216 | 82,57% |

Persentase dihitung dari jumlah sel terisi dibandingkan seluruh sel provinsi × periode dalam seri tersebut. Sel yang belum menjadi wilayah administratif, tidak diterbitkan, atau berada pada batas wilayah lama tetap diperhitungkan sebagai sel dalam grid.

## 5. Temuan sel missing

Ditemukan dua sel dengan kategori `missing` pada seri `var2749`:

| Seri | Provinsi | Tahun |
|---|---|---:|
| var2749 | Papua Pegunungan | 2024 |
| var2749 | Papua Pegunungan | 2025 |

Pemeriksaan sumber CSV BPS menunjukkan bahwa tidak ditemukan baris `var2749` untuk Papua Pegunungan pada kedua tahun tersebut. Namun, data seri lain untuk Papua Pegunungan pada 2024 dan 2025 tersedia.

Dengan demikian, kedua sel tetap dikategorikan sebagai `missing`. Belum terdapat bukti yang cukup untuk menyatakan bahwa BPS secara resmi tidak menerbitkan angka tersebut. Nilai tidak diisi dengan perkiraan atau nilai dari provinsi lain.

## 6. Strategi penanganan missing

Klasifikasi sel kosong dilakukan dengan membedakan kondisi berikut:

- `belum_ada`: provinsi belum terbentuk pada periode terkait.
- `batas_lama`: data historis masih mengikuti batas wilayah sebelum pemekaran.
- `tidak_diterbitkan`: terdapat keterangan sumber bahwa angka tidak diterbitkan.
- `missing`: provinsi sudah ada, tetapi observasi tidak ditemukan dan belum ada bukti resmi bahwa angka tidak diterbitkan.

Sel kosong tidak langsung diimputasi atau dihapus. Setiap keputusan penanganan harus didukung bukti sumber dan dicatat dalam `log-keputusan.csv`.

## 7. Batasan hasil

Angka dalam laporan ini berasal dari pengujian grid secara langsung menggunakan CSV BPS di memori. Hasil masih perlu divalidasi menggunakan keluaran Silver tim sebelum laporan dan metrik ditetapkan sebagai hasil final pipeline.

## 8. Kesimpulan

Pembentukan grid membantu mengidentifikasi kelengkapan panel dan membedakan sel kosong berdasarkan kondisi wilayah serta ketersediaan data. Pada pengujian sementara ditemukan 453 sel kosong, termasuk dua sel `missing` pada seri `var2749` untuk Papua Pegunungan tahun 2024 dan 2025. Penanganan dilakukan dengan mempertahankan nilai kosong dan mendokumentasikan alasan klasifikasinya, bukan mengisi nilai tanpa bukti sumber.