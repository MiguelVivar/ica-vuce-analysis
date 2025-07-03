# src/utils/preprocessing.py
import pandas as pd

def preprocesar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y preprocesa el dataset"""
    print("\n🧹 Preprocesando datos...")
    df_clean = df.copy()
    df_clean.columns = df_clean.columns.str.strip().str.upper()
    df_clean['FECHA_SOLICITUD_CLEAN'] = pd.to_datetime(df_clean['FECHA SOLICITUD'], errors='coerce')
    df_clean['FECHA_EMISION_CLEAN'] = pd.to_datetime(df_clean['FECHA EMISION'], errors='coerce')
    df_clean['CULTIVO_CLEAN'] = df_clean['CULTIVO'].str.strip().str.upper()
    df_clean['DESCRIPCIÓN_CULTIVO_CLEAN'] = df_clean['DESCRIPCIÓN CULTIVO'].str.strip().str.upper()
    df_clean['PROVINCIA_CLEAN'] = df_clean['PROVINCIA'].str.strip().str.title()
    df_clean['DISTRITO_CLEAN'] = df_clean['DISTRITO'].str.strip().str.title()
    df_clean['PRODUCCION_ESTIMADA'] = df_clean['AREA CERTIFICAR (HA)'] * df_clean['RENDIMIENTO CERTIFICADO']
    print(f"✅ Preprocesamiento completado")
    print(f"- Registros después de limpieza: {len(df_clean)}")
    return df_clean
