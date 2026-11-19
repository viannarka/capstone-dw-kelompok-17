from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


FOLDER_LAPORAN = Path(__file__).resolve().parent
FOLDER_GAMBAR = FOLDER_LAPORAN / "gambar"

KODE_SERI = [845, 847, 1273, 2179, 2741, 2749]


def jalankan(bps_json):
    # Nama kolom laporan dipertahankan agar seri statistik tim dapat dibandingkan.
    data = bps_json.rename(columns={"var_id": "var_kode", "wilayah_id": "vervar_kode",
                                    "wilayah": "vervar_label", "turvar": "turvar_label",
                                    "tahun": "tahun_plot"}).copy()
    data["var_kode"] = pd.to_numeric(data["var_kode"]).astype(float)
    if set(data["var_kode"]) != set(KODE_SERI):
        raise ValueError("Enam seri BPS diperlukan untuk profil")
    data["nilai"] = pd.to_numeric(data["nilai"].astype(str).str.replace(",", ".", regex=False))
    data["tahun_plot"] = pd.to_numeric(data["tahun_plot"])
    data["turvar_label"] = data["turvar_label"].fillna("Tidak ada")
    data = data.dropna(subset=["nilai", "tahun_plot", "vervar_label"])
    data = data[data["vervar_kode"].ne("9999")]

    print("Jumlah baris untuk analisis:", len(data))

    statistik(data)
    calon_iqr(data)
    calon_per_periode(data)
    gambar(data)


def statistik(data):
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


def calon_iqr(data):
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

    print("Kandidat IQR per seri dan rincian (metode awal tim):", len(anomali))
    print("Daftar calon anomali berhasil disimpan.")


def calon_per_periode(data):
    """Profil pembanding dengan metode IQR tiga arah pada rincian total, sesuai acuan #5."""
    total = data[data["turvar_label"].isin(["Tidak ada", "Perkotaan+Perdesaan"])].copy()
    total["seri_kode"] = "var" + total["var_kode"].astype(int).astype(str)
    total["wilayah_kode"] = total["vervar_kode"].astype(int)
    total["periode"] = total["tahun_plot"].astype(int)
    kunci = ["seri_kode", "wilayah_kode", "periode"]
    total = total.sort_values(kunci)
    seri_tahun = ["seri_kode", "periode"]
    seri_prov = ["seri_kode", "wilayah_kode"]
    total["nama_wilayah"] = (
        total["vervar_label"].str.title().str.replace(r"^Kep\. ", "Kepulauan ", regex=True)
        .replace({"Di Yogyakarta": "DI Yogyakarta", "Dki Jakarta": "DKI Jakarta"})
    )
    # Pergeseran satu kolom memilih tahun terbit sebelumnya, termasuk bila sel lokal kosong.
    lebar = total.pivot(index=seri_prov, columns="periode", values="nilai")
    perubahan = []
    periode_lalu = {}
    for seri, blok in lebar.groupby(level="seri_kode"):
        tahun = sorted(total.loc[total["seri_kode"].eq(seri), "periode"].unique())
        periode_lalu.update({(seri, b): a for a, b in zip(tahun, tahun[1:])})
        perubahan.append(blok[tahun].diff(axis=1).stack().rename("perubahan"))
    total = total.join(pd.concat(perubahan), on=kunci)
    calon = []
    for arah, kolom, grup, minimum in [
        ("ke bawah", "nilai", seri_tahun, 8),
        ("perubahan", "perubahan", seri_tahun, 8),
        ("ke samping", "nilai", seri_prov, 6),
    ]:
        nilai = total.groupby(grup)[kolom]
        q1 = nilai.transform("quantile", q=0.25)
        q3 = nilai.transform("quantile", q=0.75)
        iqr = q3 - q1
        bawah, atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        jumlah = nilai.transform("count")
        pilih = jumlah.ge(minimum) & ~total[kolom].between(bawah, atas) & total[kolom].notna()
        terpilih = total.loc[pilih].assign(bawah=bawah, atas=atas, jumlah=jumlah, arah=arah)
        alasan = []
        for r in terpilih.itertuples():
            batas = f"di luar [{r.bawah:.2f}, {r.atas:.2f}]"
            if arah == "ke bawah":
                alasan.append(f"{batas} (IQR x 1.5) dibanding {r.jumlah} provinsi tahun itu")
            elif arah == "perubahan":
                awal = periode_lalu[r.seri_kode, r.periode]
                alasan.append(f"perubahan {awal}→{r.periode} sebesar {r.perubahan:+.2f} {batas}")
            else:
                alasan.append(f"{batas} dibanding {r.jumlah} tahun di provinsi ini")
        calon.append(terpilih.assign(alasan=alasan))

    tanda = pd.concat(calon, ignore_index=True)
    tersedia = total.groupby(seri_prov)["periode"].nunique()
    lintas_provinsi = tanda.loc[tanda["arah"].eq("ke bawah")].groupby(seri_prov)["periode"].nunique()
    berulang = (lintas_provinsi >= 2) & (lintas_provinsi / tersedia >= 0.5)
    gabung = tanda.groupby(kunci, as_index=False).agg(
        nama_wilayah=("nama_wilayah", "first"), nilai=("nilai", "first"),
        arah=("arah", " + ".join), alasan=("alasan", "; ".join))
    gabung["berulang"] = gabung.set_index(seri_prov).index.isin(berulang[berulang].index)
    gabung.sort_values(["seri_kode", "periode", "wilayah_kode"]).to_csv(
        FOLDER_LAPORAN / "calon-anomali.csv", index=False,
        columns=["seri_kode", "wilayah_kode", "nama_wilayah", "periode", "nilai", "arah", "alasan", "berulang"])
    print("Kandidat IQR tiga arah pada rincian total (metode acuan):", len(gabung))


def gambar(data):
    FOLDER_GAMBAR.mkdir(parents=True, exist_ok=True)
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

        plt.boxplot(nilai_boxplot)
        plt.xticks(range(1, len(detail_list) + 1), detail_list)

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


if __name__ == "__main__":
    from src import ekstraksi
    jalankan(ekstraksi.jalankan("bps")["bps_json"])
