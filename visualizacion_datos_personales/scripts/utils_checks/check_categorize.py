import pandas as pd
from pathlib import Path

# =========================
# RUTA ROBUSTA
# =========================
ROOT = Path(__file__).resolve().parents[2]

file_path = ROOT / "data" / "selected" / "music_categorized.csv"

# =========================
# LOAD
# =========================
df = pd.read_csv(file_path)

otros = df[df["music_origin"] == "otros"]

print("\nCantidad total de filas 'otros':")
print(otros.shape)

print("\nArtistas únicos en 'otros':")
print(otros["artistName"].nunique())

print("\nTop artistas en 'otros':")
print(
    otros["artistName"]
    .value_counts()
    .head(50)
)