# src/utils/reports.py
import pandas as pd
import json
from pathlib import Path

def generar_reportes(df: pd.DataFrame, stats: dict, resumenes_dir: Path):
    """Genera reportes de resumen en diferentes formatos"""
    print("\n📋 Generando reportes...")
    with pd.ExcelWriter(resumenes_dir / "reporte_general.xlsx", engine='xlsxwriter') as writer:
        resumen = pd.DataFrame({
            'Métrica': [
                'Total Certificaciones',
                'Años Cubiertos',
                'Provincias',
                'Distritos',
                'Cultivos Únicos',
                'Área Total (ha)',
                'Producción Estimada (t)',
                'Rendimiento Promedio (t/ha)'
            ],
            'Valor': [
                len(df),
                f"{df['AÑO CERTIFICACION'].min()}-{df['AÑO CERTIFICACION'].max()}",
                len(df['PROVINCIA_CLEAN'].unique()),
                len(df['DISTRITO_CLEAN'].unique()),
                len(df['CULTIVO_CLEAN'].unique()),
                f"{df['AREA CERTIFICAR (HA)'].sum():,.2f}",
                f"{df['PRODUCCION_ESTIMADA'].sum():,.2f}",
                f"{df['RENDIMIENTO CERTIFICADO'].mean():.2f}"
            ]
        })
        resumen.to_excel(writer, sheet_name='Resumen_Ejecutivo', index=False)
        stats['productos_top'].to_excel(writer, sheet_name='Top_Productos')
        stats['distritos_top'].to_excel(writer, sheet_name='Top_Distritos')
        stats['by_year'].to_excel(writer, sheet_name='Por_Año')
    for provincia in df['PROVINCIA_CLEAN'].unique():
        if pd.isna(provincia):
            continue
        df_prov = df[df['PROVINCIA_CLEAN'] == provincia]
        reporte_provincia = {
            'provincia': provincia,
            'total_certificaciones': len(df_prov),
            'area_total': df_prov['AREA CERTIFICAR (HA)'].sum(),
            'produccion_estimada': df_prov['PRODUCCION_ESTIMADA'].sum(),
            'principales_cultivos': df_prov['CULTIVO_CLEAN'].value_counts().head(5).to_dict(),
            'distritos': df_prov['DISTRITO_CLEAN'].value_counts().to_dict(),
            'rendimiento_promedio': df_prov['RENDIMIENTO CERTIFICADO'].mean()
        }
        filename = f"reporte_{provincia.lower().replace(' ', '_')}.json"
        with open(resumenes_dir / filename, 'w', encoding='utf-8') as f:
            json.dump(reporte_provincia, f, indent=2, ensure_ascii=False, default=str)
    print(f"✅ Reportes guardados en {resumenes_dir}")
