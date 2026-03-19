import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]
input_path = ROOT / "data" / "normalized" / "music_normalized.csv"


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")

    df = pd.read_csv(input_path)

    freq = df["artistName"].value_counts().reset_index()
    freq.columns = ["artist", "plays"]

    freq["cum_plays"] = freq["plays"].cumsum()
    total = freq["plays"].sum()
    freq["coverage"] = freq["cum_plays"] / total

    print("\nTop 30 artistas por reproducciones:")
    print(freq.head(30))

    print("\nCobertura top 50:", freq.iloc[49]["coverage"])
    print("Cobertura top 100:", freq.iloc[99]["coverage"])
    print("Cobertura top 200:", freq.iloc[199]["coverage"])
    print("Cobertura top 300:", freq.iloc[299]["coverage"])


if __name__ == "__main__":
    main()