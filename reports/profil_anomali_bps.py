
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from src.ekstraksi import jalankan


# ==================================================
# 1. PENGATURAN FOLDER DAN SERI BPS
# ==================================================

FOLDER_LAPORAN = Path("reports")
FOLDER_GAMBAR = FOLDER_LAPORAN / "gambar"

FOLDER_GAMBAR.mkdir(parents=True, exist_ok=True)

KODE_SERI = [845, 847, 1273, 2179, 2741, 2749]


# ==================================================
# 2. EKSTRAKSI DAN PEMILIHAN DATA
# ==================================================

print("Mengambil data hasil ekstraksi...")

hasil = jalankan()
df = hasil["mentah"]

# Memilih data BPS yang berjenis data
data = df[
    (df["_sumber_data"] == "bps")
    & (df["_jenis_data"] == "data")
].copy()

# Memilih enam seri yang menjadi tugas
data["var_kode"] = pd.to_numeric(
    data["var_kode"], errors="coerce"
)

data = data[data["var_kode"].isin(KODE_SERI)].copy()

# Mengubah nilai dan tahun menjadi numerik
data["nilai"] = pd.to_numeric(
    data["nilai"], errors="coerce"
)

data["tahun_plot"] = pd.to_numeric(
    data["tahun_label"], errors="coerce"
)

# Mengisi detail kosong agar mudah dikelompokkan
data["turvar_label"] = (
    data["turvar_label"].fillna("Tidak ada")
)

# Mengeluarkan baris yang tidak memiliki nilai atau tahun
data = data.dropna(
    subset=["nilai", "tahun_plot", "vervar_label"]
)

# Indonesia tidak digabungkan dengan data provinsi
data = data[
    data["vervar_label"].str.upper() != "INDONESIA"
].copy()

print("Jumlah baris untuk analisis:", len(data))


# ==================================================
# 3. PROFIL STATISTIK PER SERI DAN DETAIL
# ==================================================

profil = (
    data.groupby(["var_kode", "turvar_label"])["nilai"]
    .agg(
        jumlah="count",
        rata_rata="mean",
        median="median",
        standar_deviasi="std",
        minimum="min",
        Q1=lambda x: x.quantile(0.25),
        Q3=lambda x: x.quantile(0.75),
        maksimum="max"
    )
    .reset_index()
)

profil.to_csv(
    FOLDER_LAPORAN / "profil_statistik_bps.csv",
    index=False
)

print("\nProfil statistik berhasil disimpan.")


# ==================================================
# 4. PROFIL STATISTIK PER PROVINSI
# ==================================================

profil_provinsi = (
    data.groupby(
        ["var_kode", "turvar_label", "vervar_label"]
    )["nilai"]
    .agg(
        jumlah="count",
        rata_rata="mean",
        minimum="min",
        maksimum="max"
    )
    .reset_index()
)

profil_provinsi.to_csv(
    FOLDER_LAPORAN / "profil_per_provinsi_bps.csv",
    index=False
)

print("Profil per provinsi berhasil disimpan.")


# ==================================================
# 5. IDENTIFIKASI CALON ANOMALI DENGAN IQR
# ==================================================

daftar_anomali = []

for (kode, detail), kelompok in data.groupby(
    ["var_kode", "turvar_label"]
):
    q1 = kelompok["nilai"].quantile(0.25)
    q3 = kelompok["nilai"].quantile(0.75)

    iqr = q3 - q1

    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr

    calon = kelompok[
        (kelompok["nilai"] < batas_bawah)
        | (kelompok["nilai"] > batas_atas)
    ].copy()

    for _, baris in calon.iterrows():
        if baris["nilai"] < batas_bawah:
            alasan = "Di bawah batas bawah IQR"
        else:
            alasan = "Di atas batas atas IQR"

        daftar_anomali.append({
            "var_kode": int(kode),
            "detail": detail,
            "provinsi": baris["vervar_label"],
            "tahun": int(baris["tahun_plot"]),
            "nilai": baris["nilai"],
            "batas_bawah": batas_bawah,
            "batas_atas": batas_atas,
            "alasan": alasan
        })

anomali = pd.DataFrame(daftar_anomali)

anomali.to_csv(
    FOLDER_LAPORAN / "calon_anomali_bps.csv",
    index=False
)

print("Jumlah calon anomali:", len(anomali))
print("Daftar calon anomali berhasil disimpan.")


# ==================================================
# 6. MEMBUAT BOXPLOT SETIAP SERI
# ==================================================

for kode in KODE_SERI:
    kelompok = data[data["var_kode"] == kode]

    detail_list = sorted(
        kelompok["turvar_label"].unique()
    )

    nilai_boxplot = [
        kelompok.loc[
            kelompok["turvar_label"] == detail,
            "nilai"
        ].dropna()
        for detail in detail_list
    ]

    plt.figure(figsize=(9, 6))

    plt.boxplot(
        nilai_boxplot,
        tick_labels=detail_list
    )

    plt.title(f"Boxplot Seri BPS {kode}")
    plt.xlabel("Detail")
    plt.ylabel("Nilai (Persen)")
    plt.xticks(rotation=15)
    plt.tight_layout()

    plt.savefig(
        FOLDER_GAMBAR / f"boxplot_{kode}.png",
        dpi=300
    )

    plt.close()


# ==================================================
# 7. MEMBUAT GRAFIK TIME SERIES SETIAP SERI
# ==================================================

for kode in KODE_SERI:
    kelompok = data[data["var_kode"] == kode]

    detail_list = sorted(
        kelompok["turvar_label"].unique()
    )

    fig, axes = plt.subplots(
        len(detail_list),
        1,
        figsize=(12, 5 * len(detail_list)),
        squeeze=False
    )

    for i, detail in enumerate(detail_list):
        ax = axes[i, 0]

        bagian = kelompok[
            kelompok["turvar_label"] == detail
        ]

        # Setiap garis mewakili satu provinsi
        for provinsi, data_provinsi in bagian.groupby(
            "vervar_label"
        ):
            data_provinsi = data_provinsi.sort_values(
                "tahun_plot"
            )

            ax.plot(
                data_provinsi["tahun_plot"],
                data_provinsi["nilai"],
                marker="o",
                markersize=3,
                linewidth=1,
                label=provinsi
            )

        ax.set_title(f"Detail: {detail}")
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Nilai (Persen)")
        ax.grid(True, alpha=0.3)

        ax.legend(
            bbox_to_anchor=(1.02, 1),
            loc="upper left",
            fontsize=7
        )

    fig.suptitle(
        f"Time Series Seri BPS {kode}",
        fontsize=14
    )

    fig.tight_layout()

    fig.savefig(
        FOLDER_GAMBAR / f"time_series_{kode}.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)


# ==================================================
# 8. RINGKASAN HASIL
# ==================================================

print("\n===== PROSES SELESAI =====")
print("Jumlah seri:", data["var_kode"].nunique())
print("Jumlah baris:", len(data))
print("Jumlah calon anomali:", len(anomali))
print("Tabel tersimpan di folder reports.")
print("Grafik tersimpan di folder reports/gambar.")
