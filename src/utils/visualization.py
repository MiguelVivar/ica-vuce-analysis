# src/utils/visualization.py
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

def crear_visualizaciones(df: pd.DataFrame, stats: dict, graficos_dir: Path):
    """Crea visualizaciones clave del análisis"""
    print("\n📊 Creando visualizaciones...")
    fig_productos = px.bar(
        x=stats['productos_top'].head(10).values,
        y=stats['productos_top'].head(10).index,
        orientation='h',
        title="Top 10 Cultivos por Número de Certificaciones",
        labels={'x': 'Número de Certificaciones', 'y': 'Cultivo'},
        color=stats['productos_top'].head(10).values,
        color_continuous_scale='viridis'
    )
    fig_productos.update_layout(height=600, showlegend=False)
    fig_productos.write_html(graficos_dir / "top_productos.html")
    fig_temporal = px.bar(
        x=stats['by_year'].index,
        y=stats['by_year'].values,
        title="Certificaciones por Año",
        labels={'x': 'Año', 'y': 'Número de Certificaciones'},
        color=stats['by_year'].values,
        color_continuous_scale='blues'
    )
    fig_temporal.write_html(graficos_dir / "distribucion_temporal.html")
    district_product = df.groupby(['DISTRITO_CLEAN', 'CULTIVO_CLEAN']).size().reset_index(name='count')
    top_districts = stats['distritos_top'].head(10).index
    top_products = stats['productos_top'].head(10).index
    heatmap_data = district_product[
        (district_product['DISTRITO_CLEAN'].isin(top_districts)) &
        (district_product['CULTIVO_CLEAN'].isin(top_products))
    ]
    pivot_data = heatmap_data.pivot(index='DISTRITO_CLEAN', columns='CULTIVO_CLEAN', values='count').fillna(0)
    fig_heatmap = px.imshow(
        pivot_data.values,
        x=pivot_data.columns,
        y=pivot_data.index,
        title="Mapa de Calor: Certificaciones por Distrito y Cultivo",
        color_continuous_scale='YlOrRd',
        aspect='auto'
    )
    fig_heatmap.update_layout(height=600)
    fig_heatmap.write_html(graficos_dir / "heatmap_distrito_producto.html")
    fig_areas = go.Figure()
    fig_areas.add_trace(go.Scatter(
        x=df['AREA CERTIFICAR (HA)'],
        y=df['RENDIMIENTO CERTIFICADO'],
        mode='markers',
        marker=dict(
            size=8,
            color=df['PRODUCCION_ESTIMADA'],
            colorscale='viridis',
            showscale=True,
            colorbar=dict(title="Producción Estimada (t)")
        ),
        text=df['CULTIVO_CLEAN'],
        hovertemplate='<b>%{text}</b><br>Área: %{x:.2f} ha<br>Rendimiento: %{y:.2f} t/ha<br>Producción: %{marker.color:.2f} t<extra></extra>',
        name='Certificaciones'
    ))
    fig_areas.update_layout(
        title="Relación entre Área Certificada y Rendimiento",
        xaxis_title="Área Certificada (hectáreas)",
        yaxis_title="Rendimiento Certificado (t/ha)",
        height=600
    )
    fig_areas.write_html(graficos_dir / "area_vs_rendimiento.html")
    provincia_stats = df.groupby('PROVINCIA_CLEAN').agg({
        'AREA CERTIFICAR (HA)': 'sum',
        'PRODUCCION_ESTIMADA': 'sum',
        'CULTIVO_CLEAN': 'count'
    }).reset_index()
    provincia_stats.columns = ['Provincia', 'Area_Total', 'Produccion_Total', 'Num_Certificaciones']
    fig_geografia = px.bar(
        provincia_stats,
        x='Provincia',
        y='Num_Certificaciones',
        title="Certificaciones por Provincia",
        color='Produccion_Total',
        hover_data=['Area_Total', 'Produccion_Total'],
        color_continuous_scale='viridis'
    )
    fig_geografia.write_html(graficos_dir / "distribucion_geografica.html")
    print(f"✅ Visualizaciones guardadas en {graficos_dir}")
