# src/utils/data_loader.py
import pandas as pd
from pathlib import Path

def cargar_datos(data_dir: Path) -> pd.DataFrame:
    """Carga y realiza preprocesamiento inicial del dataset"""
    print("🔄 Cargando datos...")
    df = pd.read_csv(data_dir / "lugar_produccion_ica.csv", encoding='latin-1')
    print(f"✅ Dataset cargado: {df.shape[0]} registros, {df.shape[1]} columnas")
    print(f"\n📊 Información básica del dataset:")
    print(f"- Período: {df['AÑO CERTIFICACION'].min()} - {df['AÑO CERTIFICACION'].max()}")
    print(f"- Departamento: {df['DEPARTAMENTO'].unique()}")
    print(f"- Columnas disponibles: {list(df.columns)}")
    return df
