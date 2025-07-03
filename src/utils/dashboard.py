# src/utils/dashboard.py
from datetime import datetime
from pathlib import Path

def crear_dashboard_html(df, stats, output_dir):
    """Crea un dashboard HTML interactivo"""
    html_content = f"""
    <!DOCTYPE html>
    <html lang=\"es\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Dashboard - Análisis Producción Ica</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; text-align: center; }}
            .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }}
            .stat-card {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }}
            .stat-number {{ font-size: 2.5em; font-weight: bold; color: #667eea; margin-bottom: 10px; }}
            .stat-label {{ color: #666; font-size: 1.1em; }}
            .charts-section {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }}
            .chart-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 20px; }}
            .insights {{ background: #e8f4f8; padding: 20px; border-radius: 10px; margin-top: 20px; }}
            .insights h3 {{ color: #2c5aa0; margin-top: 0; }}
        </style>
    </head>
    <body>
        <div class=\"header\">
            <h1>📊 Dashboard de Análisis</h1>
            <h2>Producción Agroindustrial - Región Ica</h2>
            <p>Certificaciones VUCE 2023-2025 | Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        </div>
        <div class=\"stats-grid\">
            <div class=\"stat-card\"><div class=\"stat-number\">{len(df):,}</div><div class=\"stat-label\">Total Certificaciones</div></div>
            <div class=\"stat-card\"><div class=\"stat-number\">{len(df['CULTIVO_CLEAN'].unique())}</div><div class=\"stat-label\">Cultivos Únicos</div></div>
            <div class=\"stat-card\"><div class=\"stat-number\">{len(df['DISTRITO_CLEAN'].unique())}</div><div class=\"stat-label\">Distritos</div></div>
            <div class=\"stat-card\"><div class=\"stat-number\">{df['AREA CERTIFICAR (HA)'].sum():,.0f}</div><div class=\"stat-label\">Hectáreas Certificadas</div></div>
            <div class=\"stat-card\"><div class=\"stat-number\">{df['PRODUCCION_ESTIMADA'].sum():,.0f}</div><div class=\"stat-label\">Toneladas Estimadas</div></div>
            <div class=\"stat-card\"><div class=\"stat-number\">{df['RENDIMIENTO CERTIFICADO'].mean():.1f}</div><div class=\"stat-label\">Rendimiento Promedio (t/ha)</div></div>
        </div>
        <div class=\"charts-section\">
            <h2>📈 Análisis Visual</h2>
            <div class=\"chart-grid\">
                <div><h3>Productos Principales</h3><iframe src=\"graficos/top_productos.html\" width=\"100%\" height=\"400\" frameborder=\"0\"></iframe></div>
                <div><h3>Distribución Temporal</h3><iframe src=\"graficos/distribucion_temporal.html\" width=\"100%\" height=\"400\" frameborder=\"0\"></iframe></div>
                <div><h3>Distribución Geográfica</h3><iframe src=\"graficos/distribucion_geografica.html\" width=\"100%\" height=\"400\" frameborder=\"0\"></iframe></div>
                <div><h3>Área vs Rendimiento</h3><iframe src=\"graficos/area_vs_rendimiento.html\" width=\"100%\" height=\"400\" frameborder=\"0\"></iframe></div>
            </div>
            <div style=\"margin-top: 30px;\"><h3>Mapa de Calor: Distritos vs Cultivos</h3><iframe src=\"graficos/heatmap_distrito_producto.html\" width=\"100%\" height=\"600\" frameborder=\"0\"></iframe></div>
        </div>
        <div class=\"insights\">
            <h3>🔍 Insights Clave</h3>
            <ul>
                <li><strong>Cultivo Líder:</strong> {stats['productos_top'].index[0]} con {stats['productos_top'].iloc[0]:,} certificaciones</li>
                <li><strong>Distrito Más Activo:</strong> {stats['distritos_top'].index[0]} con {stats['distritos_top'].iloc[0]:,} certificaciones</li>
                <li><strong>Año de Mayor Actividad:</strong> {stats['by_year'].idxmax()} con {stats['by_year'].max():,} certificaciones</li>
                <li><strong>Área Promedio:</strong> {df['AREA CERTIFICAR (HA)'].mean():.2f} hectáreas por certificación</li>
                <li><strong>Concentración:</strong> Los top 3 cultivos representan el {(stats['productos_top'].head(3).sum() / len(df) * 100):.1f}% del total</li>
            </ul>
        </div>
        <div style=\"text-align: center; margin-top: 30px; color: #666;\"><p>Dashboard generado automáticamente | Datos: VUCE - SENASA</p></div>
    </body>
    </html>
    """
    with open(output_dir / "dashboard.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ Dashboard creado: {output_dir / 'dashboard.html'}")
