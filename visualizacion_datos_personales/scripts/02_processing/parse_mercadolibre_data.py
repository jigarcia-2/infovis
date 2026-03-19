import pandas as pd
import ast
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

input_path = ROOT / "data" / "processed" / "historial_comprasML.csv"
output_path = ROOT / "data" / "processed" / "mercadolibre_final.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def parse_python_like_object(value):
    """
    Convierte un texto con formato similar a diccionario/lista de Python
    en un objeto real de Python.

    Reglas:
    - Si el valor ya es lista o diccionario, lo devuelve tal cual.
    - Si es texto, intenta convertirlo con ast.literal_eval.
    - Si es nulo o no se puede convertir, devuelve None.
    """
    if value is None:
        return None

    if isinstance(value, (list, dict)):
        return value

    if pd.isna(value):
        return None

    if isinstance(value, str):
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return None

    return value


def extract_first_order_title(order_items):
    """
    Extrae el título del primer producto dentro de la lista 'order_items'.
    Si no existe, devuelve None.
    """
    if isinstance(order_items, list) and len(order_items) > 0:
        first_item = order_items[0]
        if isinstance(first_item, dict):
            return first_item.get("title")
    return None


def extract_first_payment_info(payments):
    """
    Extrae información del primer pago dentro de la lista 'payments'.
    Devuelve un diccionario con variables útiles para el análisis.
    """
    result = {
        "installment_amount": None,
        "installments": None,
        "payment_method_id": None,
        "payment_type": None,
        "shipping_cost": None,
        "payment_status": None,
        "total_paid_amount": None,
        "payment_currency_id": None,
    }

    if isinstance(payments, list) and len(payments) > 0:
        first_payment = payments[0]
        if isinstance(first_payment, dict):
            result["installment_amount"] = first_payment.get("installment_amount")
            result["installments"] = first_payment.get("installments")
            result["payment_method_id"] = first_payment.get("payment_method_id")
            result["payment_type"] = first_payment.get("payment_type")
            result["shipping_cost"] = first_payment.get("shipping_cost")
            result["payment_status"] = first_payment.get("status")
            result["total_paid_amount"] = first_payment.get("total_paid_amount")
            result["payment_currency_id"] = first_payment.get("currency_id")

    return result


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    # 1. Lectura del archivo base
    df = pd.read_csv(input_path)

    print("\nArchivo leído correctamente.")
    print("Shape original:", df.shape)
    print("Columnas originales:", df.columns.tolist())

    if "purchase" not in df.columns:
        raise ValueError("No se encontró la columna 'purchase' en el archivo.")

    # 2. Convertir la columna purchase a diccionario real
    parsed_purchase = df["purchase"].apply(parse_python_like_object)

    # 3. Expandir primer nivel
    df_ml = pd.json_normalize(parsed_purchase)

    print("\nPrimer nivel normalizado.")
    print("Shape:", df_ml.shape)
    print("Columnas:")
    print(df_ml.columns.tolist())

    # 4. Extraer campos anidados útiles
    if "order_items" in df_ml.columns:
        df_ml["order_items"] = df_ml["order_items"].apply(parse_python_like_object)
        df_ml["product_title"] = df_ml["order_items"].apply(extract_first_order_title)

    if "payments" in df_ml.columns:
        df_ml["payments"] = df_ml["payments"].apply(parse_python_like_object)
        payment_info = df_ml["payments"].apply(extract_first_payment_info)
        payment_info_df = pd.DataFrame(payment_info.tolist())
        df_ml = pd.concat([df_ml, payment_info_df], axis=1)

    # 5. Transformación de fecha
    if "date_created" in df_ml.columns:
        df_ml["date_created"] = pd.to_datetime(df_ml["date_created"], errors="coerce")
        df_ml["purchase_date"] = df_ml["date_created"].dt.date
        df_ml["purchase_hour"] = df_ml["date_created"].dt.hour
        df_ml["purchase_weekday"] = df_ml["date_created"].dt.day_name()
        df_ml["purchase_month"] = df_ml["date_created"].dt.month

    # 6. Selección final de columnas útiles
    selected_columns = [
        "date_created",
        "purchase_date",
        "purchase_hour",
        "purchase_weekday",
        "purchase_month",
        "currency_id",
        "paid_amount",
        "status",
        "product_title",
        "installment_amount",
        "installments",
        "payment_method_id",
        "payment_type",
        "shipping_cost",
        "payment_status",
        "total_paid_amount",
        "payment_currency_id",
    ]

    existing_columns = [col for col in selected_columns if col in df_ml.columns]
    df_final = df_ml[existing_columns].copy()

    # 7. Guardado
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_final.to_csv(output_path, index=False, encoding="utf-8")

    # 8. Reporte
    print("\nDataset final de Mercado Libre:")
    print("Shape:", df_final.shape)

    print("\nColumnas finales:")
    print(df_final.columns.tolist())

    print("\nPrimeras filas:")
    print(df_final.head())

    print(f"\nArchivo guardado en: {output_path}")


if __name__ == "__main__":
    main()