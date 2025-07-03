# src/main.py
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import DATA_DIR, OUTPUT_DIR, GRAFICOS_DIR, RESUMENES_DIR, crear_directorios
from src.utils.data_loader import cargar_datos
from src.utils.preprocessing import preprocesar_datos
from src.utils.analysis import analisis_descriptivo
from src.utils.visualization import crear_visualizaciones
from src.utils.reports import generar_reportes
from src.utils.dashboard import crear_dashboard_html

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
warnings.filterwarnings('ignore')

def main():
    print("🚀 INICIANDO ANÁLISIS DE PRODUCCIÓN AGROINDUSTRIAL - ICA")
    print("=" * 60)
    try:
        crear_directorios()
        df = cargar_datos(DATA_DIR)
        df_clean = preprocesar_datos(df)
        stats = analisis_descriptivo(df_clean)
        crear_visualizaciones(df_clean, stats, GRAFICOS_DIR)
        generar_reportes(df_clean, stats, RESUMENES_DIR)
        crear_dashboard_html(df_clean, stats, OUTPUT_DIR)
        print("\n" + "=" * 60)
        print("🎉 ANÁLISIS COMPLETADO EXITOSAMENTE")
        print(f"📁 Archivos generados en: {OUTPUT_DIR}")
        print("📊 Dashboard disponible en: outputs/dashboard.html")
        print("📈 Gráficos en: outputs/graficos/")
        print("📋 Reportes en: outputs/resumenes/")
    except Exception as e:
        print(f"❌ Error durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
