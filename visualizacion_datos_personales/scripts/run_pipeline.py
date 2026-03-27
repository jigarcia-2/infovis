from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

PIPELINE_STEPS = [
    "scripts/01_ingestion/load_data.py",
    "scripts/02_processing/parse_mercadolibre_data.py",
    "scripts/02_processing/normalize_time_all.py",
    "scripts/03_selection/select_health_columns.py",
    "scripts/03_selection/select_relevant_columns.py",
    "scripts/04_feature_engineering/categorize_mercadolibre.py",
    "scripts/04_feature_engineering/script_categorize_music.py",
    "scripts/04_feature_engineering/categorize_podcast.py",
    "scripts/04_feature_engineering/categorize_netflix.py",
    "scripts/05_integration/aggregate_health_daily.py",
    "scripts/05_integration/aggregate_music_daily.py",
    "scripts/05_integration/aggregate_podcast_daily.py",
    "scripts/05_integration/aggregate_netflix_daily.py",
    "scripts/05_integration/aggregate_ml_daily.py",
    "scripts/05_integration/merge_all_datasets.py",
    "scripts/06_visualization.py/create_behavior_daily_viz.py",
]


def run_step(script_relative_path):
    script_path = ROOT / script_relative_path

    print("\n" + "=" * 70)
    print(f"Running: {script_relative_path}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=ROOT
    )

    if result.returncode != 0:
        print(f"\nError while running: {script_relative_path}")
        sys.exit(result.returncode)


def main():
    print(f"Project root: {ROOT}")
    print("Starting full pipeline...")

    for step in PIPELINE_STEPS:
        run_step(step)

    print("\n" + "=" * 70)
    print("Pipeline finished successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()