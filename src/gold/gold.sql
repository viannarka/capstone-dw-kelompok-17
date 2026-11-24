CREATE TABLE gold_provinsi (
    wilayah_kode INTEGER NOT NULL,
    periode VARCHAR NOT NULL,
    konsep VARCHAR NOT NULL,
    rincian VARCHAR NOT NULL,
    nama_wilayah VARCHAR NOT NULL,
    seri_kode VARCHAR NOT NULL REFERENCES seri (seri_kode),
    jenis_periode VARCHAR NOT NULL,
    nilai DOUBLE NOT NULL,
    satuan VARCHAR NOT NULL,
    flag_anomali VARCHAR NOT NULL,
    _berkas_raw VARCHAR NOT NULL,
    _sha256_raw VARCHAR NOT NULL,
    PRIMARY KEY (wilayah_kode, periode, konsep, rincian)
);

CREATE TABLE panel_provinsi_tahunan (
    wilayah_kode INTEGER NOT NULL,
    periode VARCHAR NOT NULL,
    nama_wilayah VARCHAR NOT NULL,
    air_aman DOUBLE,
    air_layak DOUBLE,
    cuci_tangan DOUBLE,
    sanitasi_aman DOUBLE,
    sanitasi_layak DOUBLE,
    PRIMARY KEY (wilayah_kode, periode)
);

CREATE TABLE gold_nasional (
    seri_kode VARCHAR NOT NULL REFERENCES seri (seri_kode),
    periode VARCHAR NOT NULL,
    konsep VARCHAR NOT NULL,
    wilayah_kode INTEGER NOT NULL CHECK (wilayah_kode = 9999),
    nama_wilayah VARCHAR NOT NULL,
    jenis_periode VARCHAR NOT NULL,
    rincian VARCHAR NOT NULL CHECK (rincian = 'total'),
    nilai DOUBLE NOT NULL,
    satuan VARCHAR NOT NULL,
    sdg_kode VARCHAR,
    sumber VARCHAR NOT NULL,
    asal VARCHAR NOT NULL,
    asal_angka VARCHAR NOT NULL CHECK (asal_angka = asal),
    _berkas_raw VARCHAR NOT NULL,
    _sha256_raw VARCHAR NOT NULL,
    batas_bawah DOUBLE,
    batas_atas DOUBLE,
    rujukan_tahun INTEGER,
    PRIMARY KEY (seri_kode, periode)
);

CREATE VIEW tabel_nasional AS SELECT * FROM gold_nasional;

CREATE TABLE rekonsiliasi (
    pasangan VARCHAR NOT NULL,
    periode VARCHAR NOT NULL,
    seri_utama VARCHAR NOT NULL,
    seri_pembanding VARCHAR NOT NULL,
    nilai_utama DOUBLE NOT NULL,
    nilai_pembanding DOUBLE NOT NULL,
    selisih_poin_persen DOUBLE NOT NULL,
    kategori VARCHAR NOT NULL,
    PRIMARY KEY (pasangan, periode, seri_pembanding),
    FOREIGN KEY (seri_utama, periode) REFERENCES gold_nasional (seri_kode, periode),
    FOREIGN KEY (seri_pembanding, periode) REFERENCES gold_nasional (seri_kode, periode)
);
