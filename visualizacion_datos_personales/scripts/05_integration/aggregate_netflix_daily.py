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


def duration_to_minutes(duration_str):
    try:
        return pd.to_timedelta(duration_str).total_seconds() / 60
    except Exception:
        return None


def most_representative_topic(topic_series, trailer_series, default_value="sin_dato"):
    """
    Devuelve la temática predominante del día, ignorando trailers
    si existe al menos otro contenido no-trailer.
    Si solo hubo trailers, devuelve 'solo_trailers'.
    """
    temp = pd.DataFrame({
        "topic": topic_series,
        "is_trailer": trailer_series
    }).dropna(subset=["topic"])

    if temp.empty:
        return default_value

    non_trailer = temp[temp["is_trailer"] == 0]

    if not non_trailer.empty:
        mode = non_trailer["topic"].mode()
        return mode.iloc[0] if not mode.empty else default_value

    return "solo_trailers"


def main():
    input_path = selected_path / "netflix_categorized.csv"
    output_path = aggregated_path / "netflix_daily.csv"

    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    print("\nArchivo netflix_categorized leído correctamente.")
    print("Shape original:", df.shape)

    df["netflix_minutes"] = df["Duration"].apply(duration_to_minutes)
    df["netflix_minutes"] = pd.to_numeric(df["netflix_minutes"], errors="coerce").fillna(0)

    daily = (
        df.groupby(["date", "weekday", "month", "year"], as_index=False)
        .apply(
            lambda g: pd.Series({
                "netflix_minutes_total": g["netflix_minutes"].sum(),
                "netflix_interactions": g["Title"].count(),
                "netflix_main_topic": most_representative_topic(
                    g["content_topic"],
                    g["is_trailer"]
                )
            })
        )
        .reset_index(drop=True)
    )

    daily["netflix_minutes_total"] = daily["netflix_minutes_total"].fillna(0)
    daily["netflix_interactions"] = daily["netflix_interactions"].fillna(0)
    daily["netflix_main_topic"] = daily["netflix_main_topic"].fillna("sin_dato")

    daily.to_csv(output_path, index=False, encoding="utf-8")

    print("\nDataset diario de Netflix creado:")
    print(daily.head())
    print("Shape:", daily.shape)

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()