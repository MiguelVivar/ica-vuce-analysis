# src/config.py
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
GRAFICOS_DIR = OUTPUT_DIR / "graficos"
RESUMENES_DIR = OUTPUT_DIR / "resumenes"

def crear_directorios():
    for dir_path in [OUTPUT_DIR, GRAFICOS_DIR, RESUMENES_DIR]:
        dir_path.mkdir(exist_ok=True)
