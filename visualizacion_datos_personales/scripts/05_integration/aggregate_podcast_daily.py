import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS (reproducible)
# =========================
ROOT = Path(__file__).resolve().parents[2]

selected_path = ROOT / "data" / "selected"
aggregated_path = ROOT / "data" / "aggregated"
aggregated_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def most_frequent_value(series, default_value="sin_dato"):
    mode = series.mode()
    return mode.iloc[0] if not mode.empty else default_value


def main():
    input_path = selected_path / "podcast_categorized.csv"
    output_path = aggregated_path / "podcast_daily.csv"

    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    print("\nArchivo podcast_categorized leído correctamente.")
    print("Shape original:", df.shape)

    df["minutes_played"] = pd.to_numeric(df["minutes_played"], errors="coerce")

    # =========================
    # AGREGACIÓN DIARIA
    # =========================
    daily = (
        df.groupby(["date", "weekday", "month", "year"], as_index=False)
        .agg(
            podcast_minutes_total=("minutes_played", "sum"),
            podcast_main_topic=("podcast_topic", lambda x: most_frequent_value(x, "sin_dato")),
        )
    )

    # =========================
    # RELLENO DE NaNs
    # =========================
    daily["podcast_minutes_total"] = daily["podcast_minutes_total"].fillna(0)
    daily["podcast_main_topic"] = daily["podcast_main_topic"].fillna("sin_dato")

    # =========================
    # GUARDAR
    # =========================
    daily.to_csv(output_path, index=False, encoding="utf-8")

    print("\nDataset diario de podcast creado:")
    print(daily.head())
    print("Shape:", daily.shape)

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()