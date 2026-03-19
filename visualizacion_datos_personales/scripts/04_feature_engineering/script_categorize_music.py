import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

input_path = ROOT / "data" / "normalized" / "music_normalized.csv"
output_path = ROOT / "data" / "selected" / "music_categorized.csv"
pending_output_path = ROOT / "data" / "selected" / "music_pending_artists.csv"


def normalize_text(x):
    if pd.isna(x):
        return ""
    return str(x).lower().strip()


def classify_music_profile(artist):
    """
    Clasifica el tipo general de escucha musical:
    - instrumental
    - clasica
    - artista
    """
    artist = normalize_text(artist)

    instrumental_keywords = [
        "lofi",
        "healing",
        "sleep",
        "meditation",
        "relax",
        "study",
        "focus",
        "academy",
        "musicoterapia",
        "frecuencia",
        "432hz",
        "432 hz",
        "manifest",
        "entrainment",
        "spiritual",
        "trabajo en casa",
        "maestros chill",
        "music travel love",
        "jack vuterin",
        "mc_team",
        "sat-chit",
        "plamina",
        "musicoterapiateam",
        "frecuencia alquímica",
        "bored driver",
        "musica para estudiar",
    ]

    classical_keywords = [
        "mozart",
        "beethoven",
        "bach",
        "vivaldi",
        "chopin",
        "debussy",
        "tchaikovsky",
        "schubert",
        "liszt",
        "brahms",
        "handel",
        "haydn",
        "rachmaninoff",
        "prokofiev",
        "stravinsky",
        "verdi",
        "puccini",
        "rossini",
        "classical",
        "clasica",
        "classics",
    ]

    if artist == "":
        return "instrumental"

    if any(word in artist for word in classical_keywords):
        return "clasica"

    if any(word in artist for word in instrumental_keywords):
        return "instrumental"

    return "artista"


def build_origin_mapping():
    return {
        # argentina
        "wos": "argentina",
        "el zar": "argentina",
        "conociendo rusia": "argentina",
        "spinetta": "argentina",
        "cerati": "argentina",
        "soda stereo": "argentina",
        "airbag": "argentina",
        "miranda!": "argentina",
        "charly garcia": "argentina",
        "fito paez": "argentina",
        "silvestre y la naranja": "argentina",
        "gauchito club": "argentina",
        "zoe gotusso": "argentina",
        "ainda": "argentina",
        "luck ra": "argentina",
        "babasonicos": "argentina",
        "tan bionica": "argentina",
        "roman el original": "argentina",
        "maria becerra": "argentina",
        "bizarrap": "argentina",
        "big one": "argentina",
        "roze oficial": "argentina",
        "bandalos chinos": "argentina",
        "marcela morelo": "argentina",
        "oliver kozlov": "argentina",
        "venados": "argentina",
        "fede carrizo": "argentina",
        "rayos láser": "argentina",
        "mar filippi": "argentina",
        "vahio": "argentina",
        "miguel jauregui": "argentina",
        "juan ingaramo": "argentina",
        "kiwi": "argentina",
        "el mató a un policía motorizado": "argentina",
        "el plan de la mariposa": "argentina",
        "usted señalamelo": "argentina",
        "emmanuel horvilleur": "argentina",
        "emanero": "argentina",
        "nafta": "argentina",
        "ca7riel & paco amoroso": "argentina",
        "indios": "argentina",
        "los nota lokos": "argentina",
        "el kuelgue": "argentina",
        "diego torres": "argentina",
        "ke personajes": "argentina",
        "la t y la m": "argentina",
        "nathy peluso": "argentina",
        "abel pintos": "argentina",
        "louta": "argentina",
        "isla de caras": "argentina",
        "cruzando el charco": "argentina",
        "dillom": "argentina",
        "sir hope": "argentina",

        # usa / anglo
        "taylor swift": "usa",
        "billie eilish": "usa",
        "lana del rey": "usa",
        "ariana grande": "usa",
        "beyonce": "usa",
        "the weeknd": "usa",
        "lady gaga": "usa",
        "boyce avenue": "usa",
        "backstreet boys": "usa",
        "justin bieber": "usa",
        "black eyed peas": "usa",
        "britney spears": "usa",
        "bm": "usa",
        "imagine dragons": "usa",
        "marshmello": "usa",
        "teddy swims": "usa",
        "blink-182": "usa",
        "post malone": "usa",
        "katy perry": "usa",
        "rihanna": "usa",
        "benson boone": "usa",
        "queen": "usa",
        "sam smith": "usa",
        "snow patrol": "usa",
        "james blunt": "usa",
        "dido": "usa",
        "enrique iglesias": "usa",
        "luis fonsi": "usa",

        # europa
        "maneskin": "europa",
        "stromae": "europa",
        "dua lipa": "europa",
        "adele": "europa",
        "coldplay": "europa",
        "david guetta": "europa",
        "jacob banks": "europa",
        "modern talking": "europa",
        "jorge drexler": "europa",
        "l'impératrice": "europa",
        "hugel": "europa",

        # latinoamérica
        "karol g": "latinoamerica",
        "shakira": "latinoamerica",
        "bad bunny": "latinoamerica",
        "feid": "latinoamerica",
        "camilo": "latinoamerica",
        "morat": "latinoamerica",
        "bacilos": "latinoamerica",
        "lagos": "latinoamerica",
        "blaiz fayah": "latinoamerica",
        "emiliano bruguera": "latinoamerica",
        "ricardo montaner": "latinoamerica",
        "reik": "latinoamerica",
        "marama": "latinoamerica",
        "no te va gustar": "latinoamerica",
        "sebastian yatra": "latinoamerica",
        "elena rose": "latinoamerica",
        "luis miguel": "latinoamerica",
        "mon laferte": "latinoamerica",
        "la quinta estacion": "latinoamerica",
        "elsa y elmar": "latinoamerica",
        "sin bandera": "latinoamerica",
        "paulina rubio": "latinoamerica",
        "los ángeles azules": "latinoamerica",
        "carlos baute": "latinoamerica",
        "pinky sd": "latinoamerica",
        "mestiza": "latinoamerica",
    }


def assign_music_context(artist, origin_map):
    """
    Variable final para visualización:
    - instrumental
    - clasica
    - sin_musica
    - no_determinado
    - o país/región
    """
    artist_norm = normalize_text(artist)
    music_profile = classify_music_profile(artist)

    if artist_norm == "":
        return "sin_musica"

    if music_profile == "instrumental":
        return "instrumental"

    if music_profile == "clasica":
        return "clasica"

    return origin_map.get(artist_norm, "no_determinado")


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output principal: {output_path}")
    print(f"Output pendientes: {pending_output_path}")

    df = pd.read_csv(input_path)

    origin_map = build_origin_mapping()

    df["artist_norm"] = df["artistName"].apply(normalize_text)
    df["music_context"] = df["artistName"].apply(
        lambda x: assign_music_context(x, origin_map)
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("\nFrecuencia por music_context:")
    print(df["music_context"].value_counts())

    pending = (
        df[df["music_context"] == "no_determinado"]["artistName"]
        .value_counts()
        .reset_index()
    )
    pending.columns = ["artistName", "plays"]
    pending.to_csv(pending_output_path, index=False, encoding="utf-8")

    print("\nTop pendientes:")
    print(pending.head(50))
    print(f"\nArchivo principal guardado en: {output_path}")
    print(f"Archivo de pendientes guardado en: {pending_output_path}")


if __name__ == "__main__":
    main()