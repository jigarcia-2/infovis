import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

aggregated_path = ROOT / "data" / "aggregated"
output_path = ROOT / "data" / "final"
output_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Leyendo agregados desde: {aggregated_path}")
    print(f"Guardando final en: {output_path}")

    health = pd.read_csv(aggregated_path / "health_daily.csv")
    music = pd.read_csv(aggregated_path / "music_daily.csv")
    podcast = pd.read_csv(aggregated_path / "podcast_daily.csv")
    netflix = pd.read_csv(aggregated_path / "netflix_daily.csv")
    ml = pd.read_csv(aggregated_path / "mercadolibre_daily.csv")

    df = health.copy()

    merge_keys = ["date", "weekday", "month", "year"]

    df = df.merge(music, on=merge_keys, how="left")
    df = df.merge(podcast, on=merge_keys, how="left")
    df = df.merge(netflix, on=merge_keys, how="left")
    df = df.merge(ml, on=merge_keys, how="left")

    # =========================
    # RENOMBRES
    # =========================
    rename_map = {
        "energy_burned": "active_kcal",
    }
    df = df.rename(columns=rename_map)

    # =========================
    # COLUMNAS NUMÉRICAS
    # =========================
    numeric_cols = [
        "steps",
        "distance_km",
        "active_kcal",
        "music_minutes_total",
        "music_unique_artists",
        "podcast_minutes_total",
        "netflix_minutes_total",
        "netflix_interactions",
        "ml_purchases",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # =========================
    # AJUSTES DE FORMATO
    # =========================
    if "distance_km" in df.columns:
        df["distance_km"] = df["distance_km"].round(1)

    int_cols = [
        "active_kcal",
        "music_minutes_total",
        "music_unique_artists",
        "podcast_minutes_total",
        "netflix_minutes_total",
        "netflix_interactions",
        "ml_purchases",
    ]

    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].round(0).astype(int)

    # =========================
    # COLUMNAS CATEGÓRICAS
    # =========================
    categorical_defaults = {
        "music_main_context": "sin_musica",
        "podcast_main_topic": "sin_podcast",
        "netflix_content_topic": "sin_netflix",
        "ml_main_category": "sin_compras",
    }

    for col, default_value in categorical_defaults.items():
        if col in df.columns:
            df[col] = df[col].fillna(default_value).astype(str).str.strip()

    # =========================
    # ORDEN FINAL DE COLUMNAS
    # =========================
    final_cols = [
        "date",
        "weekday",
        "month",
        "year",
        "steps",
        "distance_km",
        "active_kcal",
        "music_minutes_total",
        "music_unique_artists",
        "music_main_context",
        "podcast_minutes_total",
        "podcast_main_topic",
        "netflix_minutes_total",
        "netflix_interactions",
        "netflix_content_topic",
        "ml_purchases",
        "ml_main_category",
    ]

    existing_final_cols = [col for col in final_cols if col in df.columns]
    df_final = df[existing_final_cols].copy()

    # =========================
    # GUARDAR CSV Y EXCEL
    # =========================
    final_csv = output_path / "behavior_daily_final.csv"
    final_excel = output_path / "behavior_daily_final.xlsx"

    df_final.to_csv(final_csv, index=False, encoding="utf-8")
    df_final.to_excel(final_excel, index=False)

    print("\nDataset final integrado creado:")
    print(df_final.head())
    print("Shape:", df_final.shape)
    print(f"\nArchivo CSV guardado en: {final_csv}")
    print(f"Archivo Excel guardado en: {final_excel}")


if __name__ == "__main__":
    main()