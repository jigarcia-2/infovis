import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

input_path = ROOT / "data" / "normalized" / "netflix_normalized.csv"
output_path = ROOT / "data" / "selected" / "netflix_categorized.csv"
pending_output_path = ROOT / "data" / "selected" / "netflix_pending_titles.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 160)


def normalize_text(x):
    if pd.isna(x):
        return ""
    return str(x).lower().strip()


def is_trailer_title(title):
    """
    Detecta si el registro corresponde a trailer / clip / avance.
    """
    title_norm = normalize_text(title)

    trailer_keywords = [
        "clip",
        "tráiler",
        "trailer",
        "avance",
        "hook",
    ]

    return int(any(word in title_norm for word in trailer_keywords))


def build_topic_mapping():
    """
    Diccionario experto por título / franquicia.
    """
    return {
        # CRIMEN / THRILLER
        "undercover": "crimen_thriller",
        "operación éxtasis": "crimen_thriller",
        "el marginal": "crimen_thriller",
        "homeland": "crimen_thriller",
        "entrevías": "crimen_thriller",
        "el turista": "crimen_thriller",
        "el refugio atómico": "crimen_thriller",
        "el juego del calamar": "crimen_thriller",
        "la viuda negra": "crimen_thriller",
        "francotirador": "crimen_thriller",
        "dept. q": "crimen_thriller",
        "operativo: lioness": "crimen_thriller",
        "atrapados": "crimen_thriller",
        "breaking bad": "crimen_thriller",
        "law & order": "crimen_thriller",
        "the blacklist": "crimen_thriller",
        "better call saul": "crimen_thriller",
        "el novato": "crimen_thriller",
        "la chica de nieve": "crimen_thriller",
        "cementerio": "crimen_thriller",
        "antracita": "crimen_thriller",
        "fuera de la ley": "crimen_thriller",
        "agente nocturno": "crimen_thriller",
        "departure": "crimen_thriller",
        "vuelo 716": "crimen_thriller",
        "bandidos": "crimen_thriller",
        "cuco de cristal": "crimen_thriller",
        "camino del derecho": "crimen_thriller",
        "marcella": "crimen_thriller",
        "indomable": "crimen_thriller",
        "rehén": "crimen_thriller",
        "quédate cerca": "crimen_thriller",
        "lupin": "crimen_thriller",
        "un hombre infiltrado": "crimen_thriller",
        "la dama de los muertos": "crimen_thriller",
        "la bestia en mí": "crimen_thriller",
        "killing eve": "crimen_thriller",
        "sneaky pete": "crimen_thriller",
        "the serpent": "crimen_thriller",
        "la agente encubierta": "crimen_thriller",
        "los gringo hunters": "crimen_thriller",
        "black rabbit": "crimen_thriller",
        "en el barro": "crimen_thriller",

        # DRAMA EMOCIONAL
        "ginny y georgia": "drama_emocional",
        "mi año en oxford": "drama_emocional",
        "nadie quiere esto": "drama_emocional",
        "sol negro": "drama_emocional",
        "mala influencia": "drama_emocional",
        "valle salvaje": "drama_emocional",
        "las cosas por limpiar": "drama_emocional",
        "algo embarazada": "drama_emocional",
        "volver a florecer": "drama_emocional",
        "gracias, ¿el siguiente": "drama_emocional",
        "nuevo rico": "drama_emocional",
        "la huésped": "drama_emocional",
        "legado": "drama_emocional",
        "encuentro explosivo": "drama_emocional",
        "mar de fondo": "drama_emocional",
        "una nueva jugada": "drama_emocional",
        "lost": "drama_emocional",
        "cassandra": "drama_emocional",
        "valeria": "drama_emocional",
        "héroes de guardia": "drama_emocional",
        "el silencio": "drama_emocional",
        "un lugar para soñar": "drama_emocional",
        "respira": "drama_emocional",
        "el peso del talento": "drama_emocional",
        "the fundamentals of caring": "drama_emocional",

        # SALUD
        "dr. house": "salud",
        "house": "salud",
        "héroes de guardia": "salud",
        "respira": "salud",

        # CULTURAL / HISTÓRICO
        "the chosen": "cultural_historico",
        "merlina": "cultural_historico",
        "designated survivor": "cultural_historico",
        "el eternauta": "cultural_historico",
        "el gatopardo": "cultural_historico",
        "ad vitam": "cultural_historico",
        "la emperatriz": "cultural_historico",
        "manual para señoritas": "cultural_historico",
        "el jardinero": "cultural_historico",
        "vinagre de manzana": "cultural_historico",
        "la casa guinness": "cultural_historico",
        "olymo": "cultural_historico",
        "olympo": "cultural_historico",
        "rita": "cultural_historico",
        "animal": "cultural_historico",
        "frankenstein": "cultural_historico",
        "la diplomática": "cultural_historico",
        "el último baile": "cultural_historico",

        # COMEDIA
        "envidiosa": "comedia",
        "chicas buenas": "comedia",
        "ghosts": "comedia",
        "bella y las bestias": "comedia",
        "younger": "comedia",
        "machos alfa": "comedia",
        "emily en parís": "comedia",
        "emily in paris": "comedia",
        "fantasmas": "comedia",
        "muertos s.l.": "comedia",
        "yo no soy mendoza": "comedia",
        "el niñero": "comedia",
        "división palermo": "comedia",
        "shameless": "comedia",
        "young sheldon": "comedia",
        "la odisea de los giles": "comedia",
        "fubar": "comedia",

        # CIENCIA FICCIÓN
        "stranger things": "ciencia_ficcion",
        "startup": "ciencia_ficcion",
        "día cero": "ciencia_ficcion",
        "sense8": "ciencia_ficcion",

        # ajustes finales
        "the crown": "cultural_historico",
        "dulces magnolias": "drama_emocional",
        "american murder": "crimen_thriller",
        "la serpiente": "crimen_thriller",
        "fidelidad": "drama_emocional",
        "you": "crimen_thriller",
    }


def categorize_content_topic(title, topic_map):
    """
    Clasifica la temática principal del contenido.
    """
    title_norm = normalize_text(title)

    for key, value in topic_map.items():
        if key in title_norm:
            return value

    if any(word in title_norm for word in [
        "crimen", "polic", "narco", "muerte", "asesin", "thriller",
        "operación", "éxtasis", "undercover", "cárcel", "delito",
        "secta", "detective", "investigación", "fugitivo", "rehén",
        "encubiert", "sospech", "criminal"
    ]):
        return "crimen_thriller"

    if any(word in title_norm for word in [
        "hospital", "doctor", "médico", "medicina", "paciente", "cirugía", "house"
    ]):
        return "salud"

    if any(word in title_norm for word in [
        "drama", "amor", "familia", "vida", "corazón", "pareja",
        "madre", "padre", "hija", "hijo", "embarazada", "maternidad"
    ]):
        return "drama_emocional"

    if any(word in title_norm for word in [
        "historia", "reina", "rey", "imperio", "guerra",
        "época", "siglo", "histórico", "jesús", "política",
        "presidente", "literatura", "clásico", "diplom"
    ]):
        return "cultural_historico"

    if any(word in title_norm for word in [
        "comedia", "humor", "divert", "sitcom"
    ]):
        return "comedia"

    if any(word in title_norm for word in [
        "alien", "espacio", "futuro", "robot", "ciencia ficción",
        "distop", "paralelo", "sobrenatural", "apocalipsis"
    ]):
        return "ciencia_ficcion"

    return "otros"


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    topic_map = build_topic_mapping()

    df["is_trailer"] = df["Title"].apply(is_trailer_title)
    df["content_topic"] = df["Title"].apply(lambda x: categorize_content_topic(x, topic_map))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("\nFrecuencia por tema:")
    print(df["content_topic"].value_counts())

    print("\nFrecuencia de trailers:")
    print(df["is_trailer"].value_counts())

    pending = (
        df[df["content_topic"] == "otros"]["Title"]
        .value_counts()
        .reset_index()
    )
    pending.columns = ["Title", "views"]
    pending.to_csv(pending_output_path, index=False, encoding="utf-8")

    print("\nTop pendientes:")
    print(pending.head(30))

    print(f"\nArchivo principal guardado en: {output_path}")
    print(f"Archivo de pendientes guardado en: {pending_output_path}")


if __name__ == "__main__":
    main()