# src/utils/analysis.py
import pandas as pd

def analisis_descriptivo(df: pd.DataFrame):
    """Realiza análisis descriptivo del dataset"""
    print("\n📈 Análisis Descriptivo")
    print("=" * 50)
    print("1. ESTADÍSTICAS GENERALES:")
    print(f"   - Total de certificaciones: {len(df):,}")
    print(f"   - Años cubiertos: {sorted(df['AÑO CERTIFICACION'].unique())}")
    print(f"   - Provincias: {len(df['PROVINCIA_CLEAN'].unique())}")
    print(f"   - Distritos: {len(df['DISTRITO_CLEAN'].unique())}")
    print(f"   - Cultivos únicos: {len(df['CULTIVO_CLEAN'].unique())}")
    print("\n2. PRODUCTOS PRINCIPALES:")
    productos_top = df['CULTIVO_CLEAN'].value_counts().head(10)
    for i, (producto, count) in enumerate(productos_top.items(), 1):
        print(f"   {i:2}. {producto}: {count:,} certificaciones")
    print("\n3. DISTRIBUCIÓN GEOGRÁFICA:")
    provincias_top = df['PROVINCIA_CLEAN'].value_counts()
    for provincia, count in provincias_top.items():
        print(f"   - {provincia}: {count:,} certificaciones")
    print("\n   Distritos más activos:")
    distritos_top = df['DISTRITO_CLEAN'].value_counts().head(10)
    for i, (distrito, count) in enumerate(distritos_top.items(), 1):
        print(f"   {i:2}. {distrito}: {count:,} certificaciones")
    print("\n4. ANÁLISIS TEMPORAL:")
    by_year = df['AÑO CERTIFICACION'].value_counts().sort_index()
    for year, count in by_year.items():
        print(f"   - {year}: {count:,} certificaciones")
    print("\n5. ÁREAS Y RENDIMIENTOS:")
    print(f"   - Área total certificada: {df['AREA CERTIFICAR (HA)'].sum():,.2f} hectáreas")
    print(f"   - Área promedio por certificación: {df['AREA CERTIFICAR (HA)'].mean():.2f} ha")
    print(f"   - Rendimiento promedio: {df['RENDIMIENTO CERTIFICADO'].mean():.2f} t/ha")
    print(f"   - Producción estimada total: {df['PRODUCCION_ESTIMADA'].sum():,.2f} toneladas")
    return {
        'productos_top': productos_top,
        'provincias_top': provincias_top,
        'distritos_top': distritos_top,
        'by_year': by_year
    }
