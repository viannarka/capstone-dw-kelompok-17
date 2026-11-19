# Naskah Demo Sprint 1 (±10 menit) — Kasus 17 (Tim Nexora)

Demo memperlihatkan alur yang dapat diulang secara konsisten dan transparan, bukan sekadar tampilan antarmuka. Rekam layar terminal dan editor kode. Demo Sprint 1 wajib diunggah paling lambat 22 November 2026.

## Susunan Demonstrasi

| Menit | Bagian yang Ditunjukkan | Perintah atau Berkas Rujukan |
|---|---|---|
| **0–1** | Kasus 17 (Air Minum dan Sanitasi) dan Sprint Goal | `sprint/sprint-1/sprint-goal.md` |
| **1–2** | Verifikasi data mentah lolos SHA-256 dari klon bersih | `python unduh_data.py --kasus 17` (22 berkas terverifikasi) |
| **2–4** | Eksekusi satu perintah pipeline utama dari Bronze ke Silver, Gold, dan Validasi | `python pipeline.py` (±6.7 detik) |
| **4–5** | Pemeriksa skema minimal Silver | `python -m src.common.skema data/silver/silver.parquet` → **LOLOS** (3.242 baris, 11 seri, 39 wilayah) |
| **5–6** | Pembaca modular dan jumlah baris mentah per berkas | `src/ekstraksi/`, `reports/ekstraksi.md` (6.382 baris mentah di berkas data) |
| **6–7** | Temuan koreksi kode SDG `var847` (Sanitasi Layak), garis waktu konsep, dan patahan definisi | `reports/metadata.md`, `reports/kelengkapan-panel.md` |
| **7–8** | Penanganan kunci dinamis beda panjang di JSON BPS, Susenas 2000–2002, dan keselarasan `var2749` = `var2179` | `src/ekstraksi/bps.py` (`potong_kunci`), `reports/grid-sel-kosong.csv`, `reports/validasi.md` |
| **8–9** | Validasi aturan skema Pandera, pemuatan DuckDB, dan tabel nasional rekonsiliasi | `reports/validasi.md`, `reports/basis-data.md`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` |
| **9–10** | Penelusuran lineage satu baris Silver sampai berkas mentah dan rencana kerja Sprint 2 | `docs/data-dictionary.md` bagian contoh penelusuran lineage |

---

## Uji Reproduksi (Tugas Reproduksi & Demo)

Klon repositori ke direktori baru, jalankan perintah dari awal, lalu bandingkan `data/silver/silver.parquet` hasil jalan ulang dengan yang di-commit di repositori utama:

```powershell
python -c "import pandas as pd; a = pd.read_parquet('data/silver/silver.parquet'); b = pd.read_parquet('../capstone-dw-kelompok-17/data/silver/silver.parquet'); print('HASIL IDENTIK' if a.equals(b) else 'BERBEDA')"
```

Catat durasi total eksekusi pada komentar tugas Reproduksi di Papan Tim.
