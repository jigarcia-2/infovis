import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

processed_path = ROOT / "data" / "processed"
selected_path = ROOT / "data" / "selected"
selected_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# =========================
# FUNCIÓN AUXILIAR
# =========================
def add_time_columns(df, datetime_col):
    """
    Convierte una columna a datetime y agrega variables temporales comunes.
    """
    df[datetime_col] = pd.to_datetime(df[datetime_col], errors="coerce")

    df["date"] = df[datetime_col].dt.date
    df["hour"] = df[datetime_col].dt.hour
    df["weekday"] = df[datetime_col].dt.day_name()
    df["month"] = df[datetime_col].dt.month
    df["year"] = df[datetime_col].dt.year

    return df


def main():
    print(f"Proyecto root: {ROOT}")

    # =========================
    # 1. MUSIC
    # =========================
    music1 = pd.read_csv(processed_path / "music1.csv")
    music2 = pd.read_csv(processed_path / "music2.csv")

    music = pd.concat([music1, music2], ignore_index=True)
    music = add_time_columns(music, "endTime")

    # filtrar 2025
    music = music[music["year"] == 2025].copy()

    # crear duración en minutos
    music["minutes_played"] = pd.to_numeric(music["msPlayed"], errors="coerce") / 1000 / 60

    music_selected = music[
        [
            "endTime",
            "date",
            "hour",
            "weekday",
            "month",
            "year",
            "artistName",
            "trackName",
            "msPlayed",
            "minutes_played",
        ]
    ].copy()

    music_output = selected_path / "music_selected.csv"
    music_selected.to_csv(music_output, index=False, encoding="utf-8")

    print("\nMUSIC seleccionado:")
    print(music_selected.head())
    print("Shape:", music_selected.shape)
    print(f"Archivo guardado en: {music_output}")

    # =========================
    # 2. PODCAST
    # =========================
    podcast = pd.read_csv(processed_path / "podcast.csv")
    podcast = add_time_columns(podcast, "endTime")

    # filtrar 2025
    podcast = podcast[podcast["year"] == 2025].copy()

    # crear duración en minutos
    podcast["minutes_played"] = pd.to_numeric(podcast["msPlayed"], errors="coerce") / 1000 / 60

    podcast_selected = podcast[
        [
            "endTime",
            "date",
            "hour",
            "weekday",
            "month",
            "year",
            "podcastName",
            "episodeName",
            "msPlayed",
            "minutes_played",
        ]
    ].copy()

    podcast_output = selected_path / "podcast_selected.csv"
    podcast_selected.to_csv(podcast_output, index=False, encoding="utf-8")

    print("\nPODCAST seleccionado:")
    print(podcast_selected.head())
    print("Shape:", podcast_selected.shape)
    print(f"Archivo guardado en: {podcast_output}")

    # =========================
    # 3. NETFLIX
    # =========================
    netflix = pd.read_csv(processed_path / "netflix.csv")
    netflix = add_time_columns(netflix, "Start Time")

    # filtrar 2025
    netflix = netflix[netflix["year"] == 2025].copy()

    netflix_selected = netflix[
        [
            "Start Time",
            "date",
            "hour",
            "weekday",
            "month",
            "year",
            "Duration",
            "Title",
            "Device Type",
            "Profile Name",
        ]
    ].copy()

    netflix_output = selected_path / "netflix_selected.csv"
    netflix_selected.to_csv(netflix_output, index=False, encoding="utf-8")

    print("\nNETFLIX seleccionado:")
    print(netflix_selected.head())
    print("Shape:", netflix_selected.shape)
    print(f"Archivo guardado en: {netflix_output}")

    # =========================
    # 4. MERCADO LIBRE
    # =========================
    ml = pd.read_csv(processed_path / "mercadolibre_final.csv")
    ml["date_created"] = pd.to_datetime(ml["date_created"], errors="coerce")

    # variables temporales y filtro 2025
    ml["date"] = ml["date_created"].dt.date
    ml["hour"] = ml["date_created"].dt.hour
    ml["weekday"] = ml["date_created"].dt.day_name()
    ml["month"] = ml["date_created"].dt.month
    ml["year"] = ml["date_created"].dt.year

    ml = ml[ml["year"] == 2025].copy()

    ml_selected = ml[
        [
            "date_created",
            "date",
            "hour",
            "weekday",
            "month",
            "year",
            "paid_amount",
            "total_paid_amount",
            "payment_type",
            "payment_method_id",
            "status",
            "product_title",
        ]
    ].copy()

    ml_output = selected_path / "mercadolibre_selected.csv"
    ml_selected.to_csv(ml_output, index=False, encoding="utf-8")

    print("\nMERCADO LIBRE seleccionado:")
    print(ml_selected.head())
    print("Shape:", ml_selected.shape)
    print(f"Archivo guardado en: {ml_output}")

    print("\nArchivos seleccionados guardados en data/selected/")


if __name__ == "__main__":
    main()