# Naskah Demo Sprint 2 — Tim Nexora, Kasus 17

Target rekaman 4–5 menit. Tampilkan terminal dan editor dengan teks singkat. Batas pengumpulan 29 November 2026, maksimal 10 menit, MP4/WebM maksimal 50 MB atau tautan.

| Waktu | Yang ditampilkan | Teks di video |
|---|---|---|
| 0:00–0:35 | Klon baru dari main, hash commit, verifikasi manifest | “Kami mulai dari versi yang tersedia bagi tim. Seluruh 22 berkas mentah cocok dengan manifest.” |
| 0:35–1:05 | Perintah pipeline, waktu aktual, hasil Silver | “Silver berisi 3.242 observasi. Tiap observasi membawa jalur dan SHA-256 berkas sumber.” |
| 1:05–1:50 | Panel panjang dan lebar, contoh seri asal dan rincian pada satu provinsi | “Panel panjang menyimpan lima indikator kanonik dengan rincian. Panel lebar menyusun nilai total per provinsi dan tahun.” |
| 1:50–2:30 | Baris keluaran `DuckDB (SQL = Parquet)`, DDL dan kunci primer | “Jumlah baris cocok untuk Silver, panel panjang, panel lebar, nasional, dan rekonsiliasi.” |
| 2:30–3:30 | Rekonsiliasi P1 tahun 2024–2025 dan median per pasangan | “Tahun 2024 memiliki angka BPS dan WDI. Tahun 2025 tetap tampil dengan nilai BPS saja. Median hanya memakai periode berpasangan.” |
| 3:30–4:30 | Validasi dan hasil pemeriksaan keenam Parquet | “Empat aturan Gold lolos. Isi keenam Parquet identik dengan versi commit.” |

### Perintah dari klon bersih

Dari folder induk, jalankan blok berikut di PowerShell. Gunakan nama tujuan yang masih tersedia.

```powershell
git clone --branch main https://github.com/viannarka/capstone-dw-kelompok-17.git demo-sprint-2
cd demo-sprint-2
git rev-parse --short HEAD
python unduh_data.py --kasus 17
$waktu = Measure-Command { python pipeline.py | Out-Host }
"Durasi pipeline: {0:F2} detik" -f $waktu.TotalSeconds
```

### Kueri untuk demo dan laporan #29

Jalankan dari folder klon setelah pipeline selesai. Median dihitung sebagai nilai utama dikurangi nilai pembanding, dalam poin persentase.

```powershell
@'
import duckdb
with duckdb.connect("data/gold/gudang.duckdb", read_only=True) as db:
    print(db.sql("""SELECT periode, seri_kode, rincian, nilai, _berkas_raw
                    FROM gold_provinsi WHERE wilayah_kode=1100
                    AND periode='2025' AND seri_kode='var2179' ORDER BY rincian"""))
    print(db.sql("""SELECT periode, nilai_utama, nilai_pembanding, status
                    FROM rekonsiliasi WHERE pasangan='P1'
                    AND seri_pembanding='SH.H2O.SMDW.ZS' AND periode >= '2024'
                    ORDER BY periode"""))
    print(db.sql("""SELECT pasangan, seri_pembanding, kategori, count(*) AS n,
                           round(median(selisih_poin_persen),4) AS median_pp
                    FROM rekonsiliasi WHERE status='berpasangan'
                    GROUP BY ALL ORDER BY pasangan, seri_pembanding"""))
'@ | python -
```

P1 membandingkan rumah tangga BPS dengan penduduk WHO/WDI. P2 membandingkan air layak BPS dengan WDI *basic*, yang menetapkan batas waktu pengambilan pulang-pergi 30 menit. Pada P3, denominator cuci tangan juga berbeda. P4 menggunakan dua edisi data JMP. P5 adalah konteks pendanaan dalam juta USD konstan 2024.

### Bandingkan dengan commit yang diklon

```powershell
@'
import io
import subprocess
import pandas as pd

files = subprocess.check_output(
    ["git", "ls-files", "data/silver/*.parquet", "data/gold/*.parquet"], text=True
).splitlines()
assert files, "Parquet acuan tidak ditemukan"
for path in files:
    original = subprocess.check_output(["git", "show", "HEAD:" + path])
    acuan = pd.read_parquet(io.BytesIO(original))
    hasil = pd.read_parquet(path)
    pd.testing.assert_frame_equal(acuan, hasil, check_exact=True)
    print(path, len(hasil), "IDENTIK")
'@ | python -
```

**Komentar reproduksi berdasarkan uji 25 November 2026.** Klon bersih `main` pada commit `45b6b2a` berhasil mengunduh Kasus 17 dan memverifikasi 22 berkas. Durasi `python pipeline.py` 11,81 detik. Isi keenam Parquet identik dengan commit: Silver 3.242 baris, Gold provinsi 2.893, panel lebar 1.035, Gold nasional dan tabel nasional masing-masing 183, serta rekonsiliasi 144. Bila merekam eksekusi lain, gunakan hash dan durasi dari rekaman tersebut.
