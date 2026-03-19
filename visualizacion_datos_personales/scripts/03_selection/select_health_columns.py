import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS (reproducibilidad)
# =========================
ROOT = Path(__file__).resolve().parents[2]

processed_path = ROOT / "data" / "processed"
selected_path = ROOT / "data" / "selected"
selected_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def main():

    input_file = processed_path / "iphone_health.csv"

    print(f"\nLeyendo archivo: {input_file}")

    df = pd.read_csv(input_file, low_memory=False)

    print("\nArchivo Health leído correctamente.")
    print("Shape original:", df.shape)
    print("Columnas:", df.columns.tolist())

    # =========================
    # CONVERSIÓN FECHAS
    # =========================
    df["startDate"] = pd.to_datetime(df["startDate"], errors="coerce")
    df["endDate"] = pd.to_datetime(df["endDate"], errors="coerce")
    df["creationDate"] = pd.to_datetime(df["creationDate"], errors="coerce")

    # =========================
    # VARIABLES TEMPORALES
    # =========================
    df["date"] = df["startDate"].dt.date
    df["hour"] = df["startDate"].dt.hour
    df["weekday"] = df["startDate"].dt.day_name()
    df["month"] = df["startDate"].dt.month
    df["year"] = df["startDate"].dt.year

    # Filtrar solo año de estudio
    df = df[df["year"] == 2025].copy()

    # =========================
    # VALUE NUMÉRICO
    # =========================
    df["value_numeric"] = pd.to_numeric(df["value"], errors="coerce")

    # =========================
    # TIPOS RELEVANTES (feature selection conceptual)
    # =========================
    relevant_types = [
        "HKQuantityTypeIdentifierStepCount",
        "HKQuantityTypeIdentifierDistanceWalkingRunning",
        "HKQuantityTypeIdentifierActiveEnergyBurned",
        "HKQuantityTypeIdentifierHeadphoneAudioExposure",
    ]

    df_selected = df[df["type"].isin(relevant_types)].copy()

    # =========================
    # FEATURE ENGINEERING AUDIO
    # =========================
    df_selected["audio_exposure_hours"] = (
        df_selected["endDate"] - df_selected["startDate"]
    ).dt.total_seconds() / 3600

    df_selected.loc[
        df_selected["type"] != "HKQuantityTypeIdentifierHeadphoneAudioExposure",
        "audio_exposure_hours"
    ] = None

    # =========================
    # SELECCIÓN FINAL
    # =========================
    df_selected = df_selected[
        [
            "type",
            "unit",
            "startDate",
            "endDate",
            "date",
            "hour",
            "weekday",
            "month",
            "year",
            "value_numeric",
            "audio_exposure_hours",
        ]
    ].copy()

    # =========================
    # GUARDAR
    # =========================
    output_path = selected_path / "health_selected.csv"
    df_selected.to_csv(output_path, index=False, encoding="utf-8")

    print("\nHEALTH seleccionado:")
    print(df_selected.head())
    print("Shape:", df_selected.shape)

    print("\nTipos presentes:")
    print(df_selected["type"].value_counts())

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()