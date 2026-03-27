import pandas as pd
from pathlib import Path

# =========================
# RUTAS 
# =========================
ROOT = Path(__file__).resolve().parents[2]

selected_path = ROOT / "data" / "selected"
aggregated_path = ROOT / "data" / "aggregated"
aggregated_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def main():
    input_path = selected_path / "health_selected.csv"
    output_path = aggregated_path / "health_daily.csv"

    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    print("\nArchivo health_selected leído correctamente.")
    print("Shape original:", df.shape)

    df["value_numeric"] = pd.to_numeric(df["value_numeric"], errors="coerce")

    # =========================
    # AGREGACIÓN PRINCIPAL DE VARIABLES HEALTH
    # =========================
    pivot = (
        df.pivot_table(
            index="date",
            columns="type",
            values="value_numeric",
            aggfunc="sum"
        )
        .reset_index()
    )

    pivot = pivot.rename(columns={
        "HKQuantityTypeIdentifierStepCount": "steps",
        "HKQuantityTypeIdentifierDistanceWalkingRunning": "distance_km",
        "HKQuantityTypeIdentifierActiveEnergyBurned": "energy_burned",
    })

    # =========================
    # CALENDARIO BASE
    # =========================
    calendar_df = (
        df[["date", "weekday", "month", "year"]]
        .drop_duplicates(subset=["date"])
        .copy()
    )

    # =========================
    # MERGE FINAL
    # =========================
    health_daily = calendar_df.merge(pivot, on="date", how="left")

    for col in ["steps", "distance_km", "energy_burned"]:
        if col in health_daily.columns:
            health_daily[col] = health_daily[col].fillna(0)

    health_daily.to_csv(output_path, index=False, encoding="utf-8")

    print("\nDataset diario de health creado:")
    print(health_daily.head())
    print("Shape:", health_daily.shape)

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()