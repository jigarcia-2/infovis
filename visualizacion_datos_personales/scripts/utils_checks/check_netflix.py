import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
input_path = ROOT / "data" / "normalized" / "netflix_normalized.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 150)

df = pd.read_csv(input_path)

print("Proyecto root:", ROOT)
print("Archivo leído:", input_path)

print("\nColumnas:")
print(df.columns.tolist())

print("\nPrimeras filas:")
print(df.head(10))