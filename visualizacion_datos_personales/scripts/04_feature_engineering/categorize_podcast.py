import pandas as pd
from pathlib import Path

# =========================
# RUTAS ROBUSTAS
# =========================
ROOT = Path(__file__).resolve().parents[2]

input_path = ROOT / "data" / "normalized" / "podcast_normalized.csv"
output_path = ROOT / "data" / "selected" / "podcast_categorized.csv"
pending_output_path = ROOT / "data" / "selected" / "podcast_pending_titles.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def normalize_text(x):
    if pd.isna(x):
        return ""
    return str(x).lower().strip()


def categorize_podcast_type(podcast_name, episode_name):
    """
    Variable auxiliar interna para detectar contenidos de meditación/relajación.
    No se conserva en el dataset final.
    """
    podcast_name = normalize_text(podcast_name)
    episode_name = normalize_text(episode_name)
    text = f"{podcast_name} {episode_name}"

    meditation_keywords = [
        "relax",
        "sleep",
        "medit",
        "focus",
        "study",
        "ruido blanco",
        "white noise",
        "sonidos para dormir",
        "relajación",
        "respiración",
        "mindfulness",
        "kaixin project",
        "medita con",
        "meditaciones",
        "zen",
        "curso de milagros",
        "relajacion guiada",
        "relajación guiada",
        "innerity",
        "iq potenciado",
        "la verdad del ser",
    ]

    if any(word in text for word in meditation_keywords):
        return "meditacion_relajacion"

    return "programa"


def build_topic_mapping():
    return {
        "sala de espera": "salud",
        "barbano en hechos reales": "actualidad",
        "perros de la calle": "actualidad",
        "programa mia": "bienestar_desarrollo",
        "colorama": "otros",
        "espacio seguro": "bienestar_desarrollo",
        "el club de los dilemas": "actualidad",
        "santiago bilinkis – futuro en construcción": "bienestar_desarrollo",
        "las pibas dicen": "actualidad",
        "pasa a la acción con sofia contreras": "actualidad",
        "veto y fer, el podcast.": "actualidad",
        "the tim ferriss show": "cultural",
        "where should we begin? with esther perel": "bienestar_desarrollo",
        "lo que tú digas con alex fidalgo": "actualidad",
        "huberman lab": "bienestar_desarrollo",
        "dos pendejas de 50": "actualidad",
        "la cruda": "actualidad",
        "la fórmula podcast": "actualidad",
        "medita con baruc": "bienestar_desarrollo",
        "¿cómo carajo me relaciono?": "bienestar_desarrollo",
        "la crónica oscura": "actualidad",
        "billions club: the series": "cultural",
        "la fábrica podcast": "otros",
        "dr. la rosa": "salud",
        "noventa y contando": "otros",
        "mano a mano": "actualidad",
        "aterrados": "otros",
        "las damitas histeria": "actualidad",
        "mientras respires estás a tiempo": "bienestar_desarrollo",
        "thebooksound audio libros 🎧📚": "cultural",
        "más minas que mamás": "actualidad",
        "roca project": "otros",
        "relax": "otros",
        "meditacion y mindfulness - kaixin project -": "otros",
        "meditaciones para el alma": "otros",
        "a zen mind guided meditations": "otros",
        "meditaciones guiadas | sí medito": "otros",
        "explicación de un curso de milagros | el negro...": "cultural",
        "iq potenciado": "bienestar_desarrollo",
        "como si nadie escuchara": "actualidad",
        "ingeniería astral": "otros",
        "la verdad del ser": "bienestar_desarrollo",
        "relajación guiada": "otros",
        "meditaciones guiadas vivenciales | omnity medi...": "otros",
        "motivation by king the beasts": "bienestar_desarrollo",
        "innerity podcast": "bienestar_desarrollo",
    }


def categorize_podcast_topic(podcast_name, episode_name, topic_map):
    podcast_name_norm = normalize_text(podcast_name)
    episode_name_norm = normalize_text(episode_name)
    text = f"{podcast_name_norm} {episode_name_norm}"

    podcast_type = categorize_podcast_type(podcast_name, episode_name)

    if podcast_type == "meditacion_relajacion":
        return "otros"

    if podcast_name_norm in topic_map:
        return topic_map[podcast_name_norm]

    if any(word in text for word in [
        "corazón", "primeros auxilios", "salud", "médic", "medicina", "paciente", "doctor", "dr."
    ]):
        return "salud"

    if any(word in text for word in [
        "muerte", "crimen", "asesin", "secretos", "reales", "investigación", "caso", "noticia", "actualidad"
    ]):
        return "actualidad"

    if any(word in text for word in [
        "bienestar", "hábitos", "mente", "desarrollo", "emocional", "motivación", "relaciones"
    ]):
        return "bienestar_desarrollo"

    if any(word in text for word in [
        "historia", "cultura", "arte", "sociedad", "literatura", "libros"
    ]):
        return "cultural"

    return "otros"


def main():
    print(f"Proyecto root: {ROOT}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    df = pd.read_csv(input_path)

    topic_map = build_topic_mapping()

    df["podcast_topic"] = df.apply(
        lambda row: categorize_podcast_topic(
            row.get("podcastName"),
            row.get("episodeName"),
            topic_map
        ),
        axis=1
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print("\nFrecuencia por tema:")
    print(df["podcast_topic"].value_counts())

    pending = (
        df[df["podcast_topic"] == "otros"]["podcastName"]
        .value_counts()
        .reset_index()
    )
    pending.columns = ["podcastName", "plays"]
    pending.to_csv(pending_output_path, index=False, encoding="utf-8")

    print("\nTop pendientes:")
    print(pending.head(30))

    print(f"\nArchivo principal guardado en: {output_path}")
    print(f"Archivo de pendientes guardado en: {pending_output_path}")


if __name__ == "__main__":
    main()