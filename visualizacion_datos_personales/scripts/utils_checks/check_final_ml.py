import pandas as pd
from pathlib import Path

# =========================
# RUTA ROBUSTA
# =========================
ROOT = Path(__file__).resolve().parents[2]
file_path = ROOT / "data" / "processed" / "mercadolibre_final.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df = pd.read_csv(file_path)

print("\nShape:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

print("\nPrimeras filas completas:")
print(df.head())

print("\nColumnas de pago:")
print(df[[
    "paid_amount",
    "total_paid_amount",
    "installment_amount",
    "installments",
    "payment_method_id",
    "payment_type",
    "shipping_cost",
    "payment_status"
]].head())

print("\nProducto:")
print(df[["product_title"]].head())

print("\nFrecuencia por hora de compra:")
print(df["purchase_hour"].value_counts().sort_index())

print("\nGasto total por día de la semana:")
print(df.groupby("purchase_weekday")["paid_amount"].sum())

print("\nFrecuencia por tipo de pago:")
print(df["payment_type"].value_counts())