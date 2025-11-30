"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    input_path = Path("files/input/news.csv")
    plots_dir = Path("files/plots")
    plots_dir.mkdir(parents=True, exist_ok=True)
    output_path = plots_dir / "news.png"

    df = pd.read_csv(input_path)

    # 🔹 Normalizar nombres de columnas a minúsculas
    df.columns = [c.lower() for c in df.columns]

    years = df.iloc[:, 0]
    tv = df["television"]
    newspaper = df["newspaper"]
    radio = df["radio"]
    internet = df["internet"]

    plt.style.use("default")
    fig, ax = plt.subplots(figsize=(8, 6))

    color_tv = "#4c4c4c"
    color_newspaper = "#7f7f7f"
    color_radio = "#d0d0d0"
    color_internet = "#007acc"

    ax.plot(years, tv, color=color_tv, linewidth=2.5)
    ax.plot(years, newspaper, color=color_newspaper, linewidth=2.5)
    ax.plot(years, radio, color=color_radio, linewidth=2.5)
    ax.plot(years, internet, color=color_internet, linewidth=3)

    ax.scatter(years.iloc[0], tv.iloc[0], color=color_tv, s=30)
    ax.scatter(years.iloc[0], newspaper.iloc[0], color=color_newspaper, s=30)
    ax.scatter(years.iloc[0], radio.iloc[0], color=color_radio, s=30)
    ax.scatter(years.iloc[0], internet.iloc[0], color=color_internet, s=30)

    ax.scatter(years.iloc[-1], tv.iloc[-1], color=color_tv, s=30)
    ax.scatter(years.iloc[-1], newspaper.iloc[-1], color=color_newspaper, s=30)
    ax.scatter(years.iloc[-1], radio.iloc[-1], color=color_radio, s=30)
    ax.scatter(years.iloc[-1], internet.iloc[-1], color=color_internet, s=30)

    ax.set_title("How people get their news", fontsize=18, pad=20)
    ax.text(
        0.5,
        1.02,
        "An increasing proportion cite the internet as their primary news source",
        ha="center",
        va="bottom",
        transform=ax.transAxes,
        fontsize=10,
    )

    ax.text(
        years.iloc[0] - 0.1,
        tv.iloc[0],
        f"Television {tv.iloc[0]}%",
        ha="right",
        va="center",
        color=color_tv,
        fontsize=9,
    )
    ax.text(
        years.iloc[0] - 0.1,
        newspaper.iloc[0],
        f"Newspaper {newspaper.iloc[0]}%",
        ha="right",
        va="center",
        color=color_newspaper,
        fontsize=9,
    )
    ax.text(
        years.iloc[0] - 0.1,
        radio.iloc[0],
        f"Radio {radio.iloc[0]}%",
        ha="right",
        va="center",
        color=color_radio,
        fontsize=9,
    )
    ax.text(
        years.iloc[0] - 0.1,
        internet.iloc[0],
        f"Internet {internet.iloc[0]}%",
        ha="right",
        va="center",
        color=color_internet,
        fontsize=9,
    )

    ax.text(
        years.iloc[-1] + 0.1,
        tv.iloc[-1],
        f"{tv.iloc[-1]}%",
        ha="left",
        va="center",
        color=color_tv,
        fontsize=9,
    )
    ax.text(
        years.iloc[-1] + 0.1,
        newspaper.iloc[-1],
        f"{newspaper.iloc[-1]}%",
        ha="left",
        va="center",
        color=color_newspaper,
        fontsize=9,
    )
    ax.text(
        years.iloc[-1] + 0.1,
        radio.iloc[-1],
        f"{radio.iloc[-1]}%",
        ha="left",
        va="center",
        color=color_radio,
        fontsize=9,
    )
    ax.text(
        years.iloc[-1] + 0.1,
        internet.iloc[-1],
        f"{internet.iloc[-1]}%",
        ha="left",
        va="center",
        color=color_internet,
        fontsize=9,
    )

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks(years)
    ax.set_xlim(years.min() - 0.5, years.max() + 0.5)
    ax.set_ylim(0, max(tv.max(), newspaper.max(), radio.max(), internet.max()) + 10)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=100)
    plt.close(fig)
