import json
from pathlib import Path

# =========================
# RUTA ROBUSTA
# =========================
ROOT = Path(__file__).resolve().parents[2]
file_path = ROOT / "data" / "raw" / "historial_comprasML.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("\nPrimer registro del JSON:")
print(data[0])