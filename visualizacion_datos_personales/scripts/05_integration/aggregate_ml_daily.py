import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

selected_path = ROOT / "data" / "selected"
aggregated_path = ROOT / "data" / "aggregated"
aggregated_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def most_frequent_category(series):
    mode = series.mode()
    return mode.iloc[0] if not mode.empty else "sin_compras"


def main():
    input_path = selected_path / "mercadolibre_categorized.csv"
    output_path = aggregated_path / "mercadolibre_daily.csv"

    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    print("\nArchivo mercadolibre_categorized leído correctamente.")
    print("Shape original:", df.shape)

    daily = (
        df.groupby(["date", "weekday", "month", "year"], as_index=False)
        .agg(
            ml_purchases=("product_title", "count"),
            ml_main_category=("consumption_category", most_frequent_category),
        )
    )

    daily.to_csv(output_path, index=False, encoding="utf-8")

    print("\nDataset diario de Mercado Libre creado:")
    print(daily.head())
    print("Shape:", daily.shape)

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()