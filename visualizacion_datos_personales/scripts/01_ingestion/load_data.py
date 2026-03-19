import json
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

raw_path = ROOT / "data" / "raw"
processed_path = ROOT / "data" / "processed"
processed_path.mkdir(parents=True, exist_ok=True)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# =========================
# FUNCIONES DE LECTURA
# =========================

def load_apple_health_xml(file_path):
    """
    Lee Apple Health en formato XML y devuelve un DataFrame
    con los nodos Record.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    records = []
    for record in root.findall("Record"):
        records.append(record.attrib)

    df = pd.DataFrame(records)
    return df


def load_json_file(file_path):
    """
    Lee un archivo JSON.
    Si el JSON es una lista de diccionarios, devuelve DataFrame directo.
    Si es un diccionario, intenta normalizarlo.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        try:
            df = pd.json_normalize(data)
        except Exception:
            df = pd.DataFrame([data])
    else:
        df = pd.DataFrame()

    return df


def load_csv_file(file_path):
    """
    Lee archivo CSV y devuelve un DataFrame.
    """
    df = pd.read_csv(file_path)
    return df


def load_excel_file(file_path):
    """
    Lee archivo Excel y devuelve un DataFrame.
    """
    df = pd.read_excel(file_path)
    return df


# =========================
# FUNCIÓN AUXILIAR DE EXPLORACIÓN
# =========================

def inspect_dataframe(df, name):
    print("\n" + "=" * 60)
    print(f"DATASET: {name}")
    print("=" * 60)

    print("Shape:", df.shape)

    print("\nColumnas:")
    print(df.columns.tolist())

    print("\nPrimeras filas:")
    print(df.head())

    print("\nTipos de datos:")
    print(df.dtypes)


# =========================
# GUARDAR CSV PROCESADO
# =========================

def save_processed_csv(df, output_path):
    """
    Guarda un DataFrame como CSV en la carpeta processed.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")


# =========================
# MAIN
# =========================

def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Leyendo datos desde: {raw_path}")
    print(f"Guardando procesados en: {processed_path}")

    files = {
        "iphone_health": raw_path / "iphone_health.xml",
        "music1": raw_path / "music1.json",
        "music2": raw_path / "music2.json",
        "podcast": raw_path / "podcast.json",
        "historial_comprasML": raw_path / "historial_comprasML.json",
        "netflix": raw_path / "netflix.csv",
    }

    dataframes = {}

    # Lectura de archivos crudos
    dataframes["iphone_health"] = load_apple_health_xml(files["iphone_health"])
    dataframes["music1"] = load_json_file(files["music1"])
    dataframes["music2"] = load_json_file(files["music2"])
    dataframes["podcast"] = load_json_file(files["podcast"])
    dataframes["historial_comprasML"] = load_json_file(files["historial_comprasML"])
    dataframes["netflix"] = load_csv_file(files["netflix"])

    # Inspección y guardado preliminar
    for name, df in dataframes.items():
        inspect_dataframe(df, name)
        save_processed_csv(df, processed_path / f"{name}.csv")

    print("\nTodos los archivos fueron leídos y guardados en data/processed/")

    return dataframes


if __name__ == "__main__":
    main()