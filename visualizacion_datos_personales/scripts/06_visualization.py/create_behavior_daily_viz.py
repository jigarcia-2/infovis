import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

input_csv_path = ROOT / "data" / "final" / "behavior_daily_final.csv"
input_excel_path = ROOT / "data" / "final" / "behavior_daily_final.xlsx"

output_csv_path = ROOT / "data" / "final" / "behavior_daily_viz.csv"
output_excel_path = ROOT / "data" / "final" / "behavior_daily_viz.xlsx"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def load_input_dataset():
    """
    Prioriza CSV. Si no existe, usa Excel.
    """
    if input_csv_path.exists():
        print(f"Usando CSV como input: {input_csv_path}")
        return pd.read_csv(input_csv_path)

    print(f"CSV no encontrado. Usando Excel como input: {input_excel_path}")
    return pd.read_excel(input_excel_path)


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Output CSV: {output_csv_path}")
    print(f"Output Excel: {output_excel_path}")

    df = load_input_dataset()

    print("\nArchivo final leído correctamente.")
    print("Shape original:", df.shape)

    # =========================
    # RENOMBRES PARA VISUALIZACIÓN
    # =========================
    rename_map = {
        "active_kcal": "calorias",
        "music_minutes_total": "music_minutes",
        "podcast_minutes_total": "podcast_minutes",
        "netflix_minutes_total": "netflix_minutes",
    }

    df = df.rename(columns=rename_map)

    # =========================
    # AJUSTES DE FORMATO
    # =========================
    if "distance_km" in df.columns:
        df["distance_km"] = (
            pd.to_numeric(df["distance_km"], errors="coerce")
            .fillna(0)
            .round(1)
        )

    integer_cols = [
        "calorias",
        "music_minutes",
        "podcast_minutes",
        "netflix_minutes",
        "netflix_interactions",
        "ml_purchases",
        "steps",
        "music_unique_artists",
    ]

    for col in integer_cols:
        if col in df.columns:
            df[col] = (
                pd.to_numeric(df[col], errors="coerce")
                .fillna(0)
                .round(0)
                .astype(int)
            )

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
        "calorias",
        "music_minutes",
        "music_unique_artists",
        "music_main_context",
        "podcast_minutes",
        "podcast_main_topic",
        "netflix_minutes",
        "netflix_interactions",
        "netflix_content_topic",
        "ml_purchases",
        "ml_main_category",
    ]

    existing_final_cols = [col for col in final_cols if col in df.columns]
    df_viz = df[existing_final_cols].copy()

    # =========================
    # GUARDAR
    # =========================
    df_viz.to_csv(output_csv_path, index=False, encoding="utf-8")
    df_viz.to_excel(output_excel_path, index=False)

    print("\nDataset final para visualización creado:")
    print(df_viz.head())
    print("Shape:", df_viz.shape)

    print(f"\nArchivo CSV guardado en: {output_csv_path}")
    print(f"Archivo Excel guardado en: {output_excel_path}")


if __name__ == "__main__":
    main()