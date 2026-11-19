"""Keputusan wrangling Kasus 17 — Air minum, sanitasi, dan kebersihan.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri dan konsepnya, kode
SDG beserta buktinya, sel yang dinyatakan tidak dicacah, cakupan parsial, pergantian definisi, ambang
anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 17
SLUG = "air-sanitasi"
JUDUL = "Air minum, sanitasi, dan kebersihan"

FORMAT_BPS = "json"

_RT = "satuan analisis rumah tangga"
SERI = {
    "var845": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang memiliki akses terhadap sumber air minum layak",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.1.1", katalog_sdg="6.1.1",
        bukti_sdg="berkas sdg6_air_layak; konsep 'layak', bukan 'dikelola secara aman' (lihat var2741)",
        cakupan=f"{_RT}; Susenas; 1993–2010 dan 2021–2025; rumus baru mulai 2011 (var.def d)",
    ),
    "var2741": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang menggunakan layanan air minum yang dikelola secara aman",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.1.1", katalog_sdg="6.1.1", bukti_sdg="var.label diawali '6.1.1*'",
        cakupan=f"{_RT}; 2020–2025",
    ),
    "var847": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang memiliki akses terhadap sanitasi layak",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.2.1", katalog_sdg="11.1.1",
        bukti_sdg="var.label 'Memiliki Akses terhadap Sanitasi Layak' dan nama berkas sdg6_sanitasi_layak; "
                  "11.1.1 adalah hunian layak, bukan seri ini",
        cakupan=f"{_RT}; Susenas; 1993–2025 tanpa 2005; konsep metadata SDGs sejak 2019 (var.def d)",
        koreksi="kode SDG 11.1.1 -> 6.2.1 (katalog tertukar dengan hunian layak)",
    ),
    "var1273": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang memiliki fasilitas cuci tangan dengan sabun dan air",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.2.1", katalog_sdg="6.2.1", bukti_sdg="var.label diawali '6.2.1*'",
        cakupan=f"{_RT}; 2016 dari Susenas MKP, sesudahnya Susenas Maret (var.note)",
    ),
    "var2179": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang menggunakan layanan sanitasi yang dikelola secara aman, menurut tipe daerah",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.2.1", katalog_sdg="6.2.1", bukti_sdg="var.def: definisi safely managed (leher angsa, tangki septik disedot, IPLT/SPALD-T)",
        cakupan=f"{_RT}; rincian perkotaan, perdesaan, dan gabungan; 2020–2025",
    ),
    "var2749": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang memiliki akses terhadap sanitasi aman",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="6.2.1", katalog_sdg="6.2.1", bukti_sdg="var.label diawali '6.2.1*'",
        cakupan=f"{_RT}; 2024–2025; nilainya sama dengan var2179 gabungan (log K-011); Papua Pegunungan tidak ada",
    ),
    "SH.H2O.SMDW.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="People using safely managed drinking water services (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="6.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="satuan analisis penduduk; WHO/UNICEF JMP", koreksi="kode SDG kosong -> 6.1.1",
    ),
    "SH.H2O.BASW.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="People using at least basic drinking water services (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="1.4.1", katalog_sdg="—", bukti_sdg="tercantum di sumber SDG (sumber46) tanpa kode; layanan dasar air minum adalah komponen indikator "
                  "1.4.1 (akses layanan dasar), bukan 6.1.1 (dikelola aman)",
        cakupan="satuan analisis penduduk; basic + safely managed; JMP", koreksi="kode SDG kosong -> 1.4.1",
    ),
    "WSH_WATER_SAFELY_MANAGED": dict(
        sumber="who_gho", tingkat="nasional", nama="Population using safely managed drinking-water services (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom PERCENT_POP_N",
        sdg="6.1.1", katalog_sdg="6.1.1", bukti_sdg="metadata WHO", cakupan="satuan analisis penduduk; rincian perkotaan/perdesaan",
    ),
    "WSH_HYGIENE_BASIC": dict(
        sumber="who_gho", tingkat="nasional", nama="Population with basic handwashing facilities with soap and water at home (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom PERCENT_POP_N",
        sdg="6.2.1", katalog_sdg="6.2.1", bukti_sdg="metadata WHO", cakupan="satuan analisis penduduk; rincian perkotaan/perdesaan",
    ),
    "SDGODAWS": dict(
        sumber="who_gho", tingkat="nasional", nama="Water- and sanitation-related ODA in government spending plans",
        satuan="juta_usd_konstan_2024", katalog_satuan="—",
        bukti_satuan="kolom MONEY_N; odata IndicatorName '(constant 2024 US$ millions)'",
        sdg="6.a.1", katalog_sdg="6.a.1", bukti_sdg="metadata WHO", cakupan="bantuan pembangunan resmi, bukan cakupan layanan",
    ),
}

# Konsep per seri (garis waktu definisi; seri kanonik per tahun dipilih di Gold, Sprint 2)
KONSEP = {"var845": "air minum layak", "var2741": "air minum aman", "var847": "sanitasi layak",
          "var2179": "sanitasi aman", "var2749": "sanitasi aman", "var1273": "cuci tangan"}

RINCIAN_TOTAL_BPS = {"tidak ada", "perkotaan+perdesaan"}
RINCIAN_BPS = {"var2179": ("daerah", {"Perkotaan": "URBAN", "Perdesaan": "RURAL"})}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {"DIM_DEG_URB": "daerah"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"daerah": {"URBAN", "RURAL"}}

RUJUKAN_TAHUN = {}

# K-005: provinsi yang tidak dicacah Susenas (var.def butir a dan b var845 dan var847)
_TIDAK = {(1100, "2000"): "var.def a: tahun 2000 Susenas tidak dicacah di NAD (Aceh)",
          (8100, "2000"): "var.def a: tahun 2000 Susenas tidak dicacah di Maluku",
          (8200, "2000"): "var.def a: Maluku tidak dicacah 2000; Maluku Utara baru dipisah dari Maluku (1999)",
          (1100, "2001"): "var.def b: tahun 2001 Susenas tidak dicacah di NAD (Aceh)"}
TIDAK_TERBIT = {(s, kode, per): bukti for s in ("var845", "var847") for (kode, per), bukti in _TIDAK.items()}

# K-012: cakupan parsial (var.def c): 2002 hanya ibu kota provinsi
CAKUPAN_PARSIAL = {(s, "2002"): (1100, 8100, 8200, 9400) for s in ("var845", "var847")}

# K-013: pergantian definisi yang dinyatakan penerbit
PATAHAN_DEFINISI = {
    "var845": {"2021": "var.def d: mulai 2011 rumus baru (air minum utama dan air mandi/cuci); tabel melompat 2010 -> 2021"},
    "var847": {"2019": "var.def d: sejak 2019 konsep mengacu metadata SDGs"},
    "var1273": {"2017": "var.note: angka 2016 dari Susenas MKP 2016; KOR Maret 2016 belum menanyakan cuci tangan"},
}

TAHUN_TERBIT = {}

RENTANG = {"persen": (0, 100), "juta_usd_konstan_2024": (0, 1_000_000)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Air minum aman: BPS (rumah tangga) vs WHO dan WDI (penduduk)",
         utama="var2741", rincian_utama="total", pembanding=[("WSH_WATER_SAFELY_MANAGED", "total"), ("SH.H2O.SMDW.ZS", "total")],
         jenis="selisih", kategori="definisi (satuan analisis rumah tangga vs penduduk) dan metode (JMP memodelkan dari banyak survei)",
         alasan_rincian="WHO rincian total daerah",
         pertanyaan=[
             ("Konsepnya sama?", "Ya, dikelola secara aman (var.label 6.1.1*; DefinitionText WHO)."),
             ("Yang dihitung?", "BPS: persentase rumah tangga. WHO/WDI: persentase penduduk."),
         ]),
    dict(id="P2", judul="Air minum layak (BPS) vs setidaknya dasar (WDI)",
         utama="var845", rincian_utama="total", pembanding=[("SH.H2O.BASW.ZS", "total")],
         jenis="selisih", kategori="definisi (layak vs basic: syarat waktu ambil air ≤ 30 menit di WDI; rumus BPS berganti 2011)",
         alasan_rincian="tanpa rincian",
         pertanyaan=[
             ("Apakah layak = basic?", "Belum tentu: basic mensyaratkan waktu ambil air (sourceNote WDI); judul BPS tidak menyebutnya."),
             ("Tahun mana yang aman dibandingkan?", "Sesudah 2011 rumus BPS berubah; 2000–2010 dan 2021–2024 dianalisis terpisah."),
         ]),
    dict(id="P3", judul="Cuci tangan dengan sabun dan air: BPS vs WHO",
         utama="var1273", rincian_utama="total", pembanding=[("WSH_HYGIENE_BASIC", "total")],
         jenis="selisih", kategori="definisi (rumah tangga vs penduduk); 2016 dari Susenas MKP",
         alasan_rincian="WHO rincian total daerah",
         pertanyaan=[("Tahun 2016 sebanding?", "Sumbernya modul MKP, bukan KOR Maret; ditandai patahan sumber.")]),
    dict(id="P4", judul="Air minum aman: WHO vs WDI (keduanya JMP)",
         utama="WSH_WATER_SAFELY_MANAGED", rincian_utama="total", pembanding=[("SH.H2O.SMDW.ZS", "total")],
         jenis="selisih", kategori="vintage", alasan_rincian="rincian total",
         pertanyaan=[("Sumbernya sama?", "Ya, WHO/UNICEF JMP (sourceOrganization WDI).")]),
    dict(id="P5", judul="Bantuan pembangunan air dan sanitasi (WHO): konteks",
         utama="SDGODAWS", rincian_utama="total", pembanding=[],
         jenis="konteks", kategori="definisi berbeda: uang, bukan cakupan layanan", alasan_rincian="tanpa rincian",
         pertanyaan=[("Satuan?", "Juta USD konstan 2024 (odata IndicatorName), bukan persen.")]),
]
