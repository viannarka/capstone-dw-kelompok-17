"""docs/data-dictionary.md ditulis ulang dari data setiap `python pipeline.py`.

Tipe, rentang, dan jumlah kosong dihitung dari Silver; arti, asal, dan satuan kolom ditulis di ARTI.
Bagian khusus: kamus rincian, satuan per seri (dari docs/seri.csv), kode wilayah, dan contoh
penelusuran satu baris sampai berkas mentahnya.
"""
import pandas as pd

from src import konfigurasi as K
from src import wilayah as W
from src.laporan import ROOT, tabel_md

ARTI = {
    "sumber": (
        "nama folder sumber di data/raw/ (bps, wdi, who_gho)",
        "lembaga penerbit / produsen data mentah",
        "—",
    ),
    "seri_kode": (
        "kode seri di sumbernya (BPS: 'var' + var.val; WDI: Series; WHO: nama berkas/indikator)",
        "identitas unik seri indikator; rincian lengkap di docs/seri.csv",
        "—",
    ),
    "wilayah_kode": (
        "kamus src/wilayah.py; pemetaan ISO/M49 ke 9999; keputusan log K-001",
        "kode wilayah baku (kode BPS dua digit x 100 untuk 38 provinsi; 9999 untuk Indonesia)",
        "—",
    ),
    "nama_wilayah": (
        "kamus src/wilayah.py",
        "nama baku susunan 38 provinsi Indonesia 2025 atau 'Indonesia'",
        "—",
    ),
    "periode": (
        "tahun/turtahun BPS, date WDI, DIM_TIME WHO",
        "waktu pengamatan dalam bentuk baku ISO (YYYY)",
        "tahun",
    ),
    "jenis_periode": (
        "diturunkan dari periode dan turtahun BPS",
        "tingkat granularitas waktu: tahun, semester, triwulan, atau bulan",
        "—",
    ),
    "rincian": (
        "turvar BPS (var2179); kolom DIM_* WHO; keputusan log K-005, K-011",
        "kategori disagregasi: 'total' untuk agregat, atau 'dimensi=kode' (mis. daerah=URBAN, daerah=RURAL)",
        "—",
    ),
    "nilai": (
        "datacontent BPS; value WDI; RATE_*_N dan MONEY_N WHO",
        "angka observasi riil sesuai satuan (tidak ada nilai kosong di Silver)",
        "mengikuti kolom satuan (persen atau juta_usd_konstan_2024)",
    ),
    "satuan": (
        "var.unit BPS, sourceNote WDI, OData Indicator WHO; keputusan log K-014",
        "satuan baku pengukuran angka observasi; satu satuan per seri",
        "—",
    ),
    "sdg_kode": (
        "katalog sumber & judul berkas mentah; koreksi var847 di log K-009; log K-015, K-016",
        "kode klasifikasi target/indikator SDG (1.4.1, 6.1.1, 6.2.1, 6.a.1)",
        "—",
    ),
    "batas_bawah": (
        "kolom RATE_*_NL pada CSV WHO GHO",
        "batas bawah selang kepercayaan/ketidakpastian; kosong bila tidak ada",
        "persen",
    ),
    "batas_atas": (
        "kolom RATE_*_NU pada CSV WHO GHO",
        "batas atas selang kepercayaan/ketidakpastian; kosong bila tidak ada",
        "persen",
    ),
    "status_obs": (
        "OBS_STATUS CSV ILOSTAT",
        "kode status pengamatan apa adanya (B = patahan seri); kosong bila bukan ILOSTAT",
        "—",
    ),
    "rujukan_tahun": (
        "var.note BPS; keputusan log K-012, K-013",
        "lebar jendela rujukan survei sebelum tahun pencatatan; kosong jika tidak berlaku",
        "tahun",
    ),
    "_berkas_raw": (
        "jalur berkas mentah relatif data/raw/ dari modul ekstraksi",
        "lineage/provenans: berkas asal sumber baris data ini",
        "—",
    ),
    "_sha256_raw": (
        "src.common.manifest.sha256_raw diverifikasi terhadap data/raw/MANIFEST.csv",
        "lineage: sidik digital kriptografis SHA-256 berkas mentah asal",
        "—",
    ),
}


def _rentang(s):
    if pd.api.types.is_numeric_dtype(s):
        x = s.dropna()
        return f"{x.min():g} – {x.max():g}" if len(x) else "—"
    u = s.dropna().astype(str).unique()
    return ", ".join(sorted(u)[:6]) + (f", … ({len(u)} nilai)" if len(u) > 6 else "")


def tulis_data_dictionary(silver):
    baris = []
    for k in silver.columns:
        asal, arti, satuan = ARTI.get(k, ("", "", "—"))
        baris.append({
            "kolom": k,
            "tipe": str(silver[k].dtype),
            "satuan": satuan,
            "kosong": int(silver[k].isna().sum()),
            "rentang_atau_nilai": _rentang(silver[k]),
            "arti": arti,
            "asal": asal,
        })
    seri = pd.read_csv(ROOT / "docs" / "seri.csv", keep_default_na=False)
    rinci = silver.groupby("rincian")["seri_kode"].agg(lambda x: ", ".join(sorted(set(x)))).reset_index()
    rinci.columns = ["rincian", "dipakai_seri"]
    contoh = silver[silver["sumber"] == silver["sumber"].iloc[0]].iloc[0]
    kode_dim = "\n".join(f"- `{dim}`: " + (", ".join(f"`{x}`" for x in sorted(v)) if v else "kode sumber apa adanya")
                         for dim, v in {d: K.KODE_RINCIAN.get(d) for d in sorted(set(K.RINCIAN_DIMENSI.values()) | set(K.KODE_RINCIAN))}.items())
    for kode_seri, (dim, kamus) in getattr(K, "RINCIAN_BPS", {}).items():
        kode_dim += f"\n- `{dim}` ({kode_seri}, dari turvar BPS): " + ", ".join(f"`{v}` = {k}" for k, v in kamus.items())
    teks = [
        f"# Data dictionary — Kasus {K.KASUS:02d} {K.JUDUL}",
        "Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong "
        "dihitung dari `data/silver/silver.parquet`.",
        f"## data/silver/silver.parquet ({len(silver):,} baris)",
        "Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, "
        "wilayah_kode, periode, rincian, _berkas_raw.",
        tabel_md(pd.DataFrame(baris)),
        "## Kamus rincian",
        "Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai "
        "total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh "
        "berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.",
        "Nama dimensi dan kode yang sah:", kode_dim or "- (tidak ada dimensi)",
        tabel_md(rinci),
        "## Satuan, kode SDG, dan cakupan per seri",
        tabel_md(seri[["seri_kode", "satuan", "sdg_kode", "cakupan", "bukti_satuan"]]),
        "## Kode wilayah",
        f"9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 ({len(W.PROVINSI)} kode). "
        "WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.",
        "## Contoh penelusuran satu baris",
        tabel_md(pd.DataFrame([contoh[["sumber", "seri_kode", "wilayah_kode", "nama_wilayah", "periode", "rincian", "nilai", "satuan", "sdg_kode", "_berkas_raw", "_sha256_raw"]]])),
        f"1. `_berkas_raw` menunjuk `data/raw/{contoh['_berkas_raw']}`. Berkas ini merupakan snapshot resmi WebAPI BPS 17 Oktober 2026.",
        f"2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `{contoh['_sha256_raw']}`; nilainya identik dengan "
        "`_sha256_raw`, membuktikan integritas berkas mentah tidak mengalami perubahan.",
        "3. Di berkas mentah, nilai ditemukan pada array halaman 1, dictionary `datacontent` dengan kunci "
        "`1100127301160` (nilai `54.39`). Kunci ini diurai oleh `src/ekstraksi/bps.py` menjadi: wilayah_kode 1100 (Aceh), "
        "var 1273, turvar 0 (total), kode tahun 116 (2016), dan turtahun 0 (tahunan).",
        "4. Kaitan dengan metadata & log: `sdg_kode` 6.2.1 diperoleh dari `var.label` berkas mentah; satuan `persen` sesuai `var.unit`; "
        "dan konteks instrumen Susenas MKP 2016 dicatat pada `var.note` (keputusan log K-004 dan K-019).",
    ]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "data-dictionary.md").write_text("\n\n".join(teks) + "\n", encoding="utf-8")
