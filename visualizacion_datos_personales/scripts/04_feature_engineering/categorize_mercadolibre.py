import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

selected_path = ROOT / "data" / "selected"
input_path = selected_path / "mercadolibre_selected.csv"
output_path = selected_path / "mercadolibre_categorized.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def categorize_product(title):
    """
    Asigna una categoría general a partir del título del producto.
    La idea no es conservar el detalle comercial sino abstraer
    el tipo de consumo para el análisis conductual.
    """
    if pd.isna(title):
        return "otros"

    title = str(title).lower()

    # bienestar físico / salud
    if any(word in title for word in [
        "q10", "capsulas", "hongo", "magnesio", "suplemento",
        "vitamina", "salud", "coenzima", "adaptogeno",
        "codera", "compresion"
    ]):
        return "bienestar"

    # belleza / cuidado personal
    if any(word in title for word in [
        "labial", "opi", "gel", "crema", "serum",
        "cosmetico", "protector"
    ]):
        return "belleza"

    # tecnología / digital
    if any(word in title for word in [
        "cable", "cargador", "iphone", "usb", "adaptador",
        "teclado", "mouse", "auricular", "electrónico",
        "soporte", "notebook", "celular"
    ]):
        return "tecnologia"

    # indumentaria / accesorios personales
    if any(word in title for word in [
        "pollera", "falda", "zapatilla", "sombrero",
        "ropa", "panty", "media", "remera",
        "vestido", "campera", "aro", "aros", "blanco crudo"
    ]):
        return "indumentaria"

    # hogar / vida cotidiana
    if any(word in title for word in [
        "calendario", "organizador", "caja", "hogar", "decoración",
        "taza", "yogurtera", "dispenser", "filtro", "cafetera"
    ]):
        return "hogar"

    # workspace / trabajo / estudio
    if any(word in title for word in [
        "escritorio", "silla", "ergonomica"
    ]):
        return "workspace"

    # movilidad / viaje
    if any(word in title for word in [
        "valija", "viaje", "neceser", "botella"
    ]):
        return "movilidad"

    return "otros"


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    print("\nArchivo Mercado Libre seleccionado leído correctamente.")
    print("Shape original:", df.shape)

    df["consumption_category"] = df["product_title"].apply(categorize_product)

    # Dataset final categorizado
    df_final = df[
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
            "consumption_category",
            "product_title",
        ]
    ].copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_final.to_csv(output_path, index=False, encoding="utf-8")

    print("\nMercado Libre categorizado:")
    print(df_final.head())

    print("\nFrecuencia por categoría:")
    print(df_final["consumption_category"].value_counts())

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()