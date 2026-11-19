# Catatan Standup Mingguan Sprint 1 — Tim Nexora

Kanal Komunikasi: Google Meet & WhatsApp Group Nexora  
Koordinator: Favian Arkaanda (124450021)

---

## Standup Minggu 2 (9–15 November 2026)

### Agenda & Evaluasi Perkembangan
- **Pembagian Komponen & Papan Tim:** Memastikan seluruh anggota mengikat akun Workbench dan mengambil tiket backlog Sprint 1 (#1 s.d. #15).
- **Ekstraksi Data:** 
  - Pembaca BPS JSON berhalaman ditangani dengan pemotong kunci dinamis (`potong_kunci`) untuk mengantisipasi perbedaan panjang kode tahun (2 digit era 1990-an vs 3 digit era 2000-an).
  - Pembaca WDI JSON memfilter indikator kasus persis (`SH.H2O.SMDW.ZS`, `SH.H2O.BASW.ZS`) dan mempertahankan nilai null apa adanya.
  - Pembaca WHO GHO CSV mengenali kolom nilai `PERCENT_POP_N` dan `MONEY_N`.
- **Profiling Awal & Metadata:**
  - Penemuan bahwa kode SDG `var847` di katalog tertulis `11.1.1` (hunian layak), padahal judul tabel adalah sanitasi layak. Disepakati untuk dikoreksi menjadi `6.2.1`.
  - Pemeriksaan kelengkapan 22 berkas mentah terhadap `MANIFEST.csv`.

---

## Standup Minggu 3 (16–22 November 2026)

### Agenda & Evaluasi Perkembangan
- **Pembersihan Data & Pencatatan Log:**
  - Salavi Naharani memaparkan hasil deteksi IQR tiga arah (403 calon anomali). Diputuskan tidak menghapus baris outlier, melainkan membedakan patahan definisi (2011/2021 air layak, 2019 sanitasi layak) dan pencacahan parsial Susenas 2000–2002. Seluruh keputusan dicatat di `log-keputusan.csv`.
- **Transformasi & Pemeriksaan Skema Silver:**
  - Asri Meilani menyusun `data/silver/silver.parquet` (3.242 baris). Pemeriksaan skema minimal `python -m src.common.skema data/silver/silver.parquet` berhasil lolos.
- **Integrasi, SQL, dan Validasi:**
  - Favian Arkaanda menyiapkan tabel nasional `reports/tabel-nasional.csv` dan mendokumentasikan 5 pasangan rekonsiliasi di `reports/pasangan-rekonsiliasi.md`, serta memuat Silver ke DuckDB `data/gold/gudang.duckdb`.
  - Abdul Hakim MT melengkapi aturan validasi Pandera di `src/validasi/` dan kamus data `docs/data-dictionary.md`.
- **Persiapan Demo & Pengumpulan:**
  - Menyiapkan naskah rekaman di `DEMO.md` (durasi ±10 menit).
  - Memastikan seluruh anggota mengunggah `results/<nim>/metrics.json` dan mengisi Log Sprint 3 baris di Papan Tim sebelum tenggat waktu 23 November 2026 pukul 23.59 WIB.
