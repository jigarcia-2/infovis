import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

selected_path = ROOT / "data" / "selected"
aggregated_path = ROOT / "data" / "aggregated"
normalized_path = ROOT / "data" / "normalized"
normalized_path.mkdir(parents=True, exist_ok=True)

LOCAL_TZ = "America/Argentina/Buenos_Aires"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# =========================
# FUNCIÓN DE NORMALIZACIÓN TEMPORAL
# =========================
def normalize_datetime_column(df, source_col, assume_local_naive=True):
    """
    Normaliza una columna datetime a una zona horaria local común.

    Reglas:
    - Si la columna ya tiene timezone, se convierte a LOCAL_TZ.
    - Si no tiene timezone:
        - assume_local_naive=True: se asume que ya está en horario local.
        - assume_local_naive=False: se interpreta como UTC y se convierte.
    """
    dt = pd.to_datetime(df[source_col], errors="coerce")

    if getattr(dt.dt, "tz", None) is None:
        if assume_local_naive:
            dt = dt.dt.tz_localize(LOCAL_TZ, nonexistent="NaT", ambiguous="NaT")
        else:
            dt = (
                dt.dt.tz_localize("UTC", nonexistent="NaT", ambiguous="NaT")
                .dt.tz_convert(LOCAL_TZ)
            )
    else:
        dt = dt.dt.tz_convert(LOCAL_TZ)

    df["timestamp_local"] = dt
    df["date"] = df["timestamp_local"].dt.date
    df["hour"] = df["timestamp_local"].dt.hour
    df["weekday"] = df["timestamp_local"].dt.day_name()
    df["month"] = df["timestamp_local"].dt.month
    df["year"] = df["timestamp_local"].dt.year

    return df


# =========================
# 1. MUSIC
# =========================
def normalize_music():
    input_file = selected_path / "music_selected.csv"
    output_file = normalized_path / "music_normalized.csv"

    df = pd.read_csv(input_file)

    # Spotify suele venir sin tz explícita; se asume horario local de uso
    df = normalize_datetime_column(df, "endTime", assume_local_naive=True)

    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nMUSIC normalizado:")
    print(df.head())
    print("Shape:", df.shape)
    print(f"Archivo guardado en: {output_file}")


# =========================
# 2. PODCAST
# =========================
def normalize_podcast():
    input_file = selected_path / "podcast_selected.csv"
    output_file = normalized_path / "podcast_normalized.csv"

    df = pd.read_csv(input_file)

    # Mismo criterio que Spotify
    df = normalize_datetime_column(df, "endTime", assume_local_naive=True)

    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nPODCAST normalizado:")
    print(df.head())
    print("Shape:", df.shape)
    print(f"Archivo guardado en: {output_file}")


# =========================
# 3. NETFLIX
# =========================
def normalize_netflix():
    input_file = selected_path / "netflix_selected.csv"
    output_file = normalized_path / "netflix_normalized.csv"

    df = pd.read_csv(input_file)

    # Netflix puede venir naive; por ahora se asume horario local
    df = normalize_datetime_column(df, "Start Time", assume_local_naive=True)

    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nNETFLIX normalizado:")
    print(df.head())
    print("Shape:", df.shape)
    print(f"Archivo guardado en: {output_file}")


# =========================
# 4. MERCADO LIBRE
# =========================
def normalize_mercadolibre():
    input_file = selected_path / "mercadolibre_categorized.csv"
    output_file = normalized_path / "mercadolibre_normalized.csv"

    df = pd.read_csv(input_file)

    # Mercado Libre ya trae timezone explícita
    df = normalize_datetime_column(df, "date_created", assume_local_naive=True)

    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nMERCADO LIBRE normalizado:")
    print(df.head())
    print("Shape:", df.shape)
    print(f"Archivo guardado en: {output_file}")


# =========================
# 5. HEALTH DAILY
# =========================
def normalize_health_daily():
    input_file = aggregated_path / "health_daily.csv"
    output_file = normalized_path / "health_daily_normalized.csv"

    df = pd.read_csv(input_file)

    # health_daily ya está agregado por día
    dt = pd.to_datetime(df["date"], errors="coerce")
    dt = dt.dt.tz_localize(LOCAL_TZ, nonexistent="NaT", ambiguous="NaT")

    df["timestamp_local"] = dt
    df["date"] = df["timestamp_local"].dt.date
    df["hour"] = 0
    df["weekday"] = df["timestamp_local"].dt.day_name()
    df["month"] = df["timestamp_local"].dt.month
    df["year"] = df["timestamp_local"].dt.year

    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nHEALTH DAILY normalizado:")
    print(df.head())
    print("Shape:", df.shape)
    print(f"Archivo guardado en: {output_file}")


# =========================
# MAIN
# =========================
def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Normalizando timestamps a zona horaria común: {LOCAL_TZ}")

    normalize_music()
    normalize_podcast()
    normalize_netflix()
    normalize_mercadolibre()
    normalize_health_daily()

    print("\nArchivos normalizados guardados en data/normalized/")


if __name__ == "__main__":
    main()