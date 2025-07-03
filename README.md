# 🌱 Análisis de Producción Agroindustrial - Región de Ica (Perú)

[![Python](https://img.shields.io/badge/Python-3.13.5+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15+-red.svg)](https://plotly.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

## 📋 Descripción del Proyecto

Este proyecto realiza un **análisis exploratorio y modelado predictivo** completo del dataset de certificaciones de productos agrícolas de la región de Ica (Perú), utilizando datos de la **Ventanilla Única de Comercio Exterior (VUCE)** - SENASA.

### 🎯 Objetivos

- **Análisis Exploratorio**: Identificar tendencias, patrones y características de la producción agroindustrial
- **Modelado Predictivo**: Desarrollar modelos para estimar rendimientos y clasificar productores
- **Insights Estratégicos**: Generar recomendaciones para políticas públicas y desarrollo regional
- **Dashboard Interactivo**: Visualizaciones profesionales para toma de decisiones

### 📊 Principales Hallazgos (Datos Reales)

- **Certificaciones totales analizadas**: 183 (2024)
- **Distribución por provincia:**
  - Chincha: 66 certificaciones
  - Ica: 64 certificaciones
  - Pisco: 44 certificaciones
  - Palpa: 6 certificaciones
  - Nazca: 3 certificaciones
- **Áreas certificadas (ha):**
  - Ica: 1,720.26
  - Chincha: 915.63
  - Pisco: 1,029.88
  - Palpa: 161.91
  - Nazca: 69.36
- **Producción estimada (ton):**
  - Ica: 82,564.63
  - Chincha: 56,391.85
  - Pisco: 61,389.62
  - Palpa: 5,396.39
  - Nazca: 883.32
- **Rendimiento promedio (ton/ha):**
  - Chincha: 112.52
  - Ica: 58.15
  - Pisco: 55.33
  - Palpa: 30.80
  - Nazca: 10.82
- **Principales cultivos:**
  - Chincha: Mandarina, Arándano, Palta
  - Ica: Arándano, Mandarina, Pecana, Espárrago
  - Pisco: Mandarina, Arándano, Espárrago, Limón Tahití
  - Palpa: Mandarina, Palta
  - Nazca: Espárrago, Pecana
- **Distritos con mayor actividad:**
  - Chincha: El Carmen, Chincha Baja, Alto Larán
  - Ica: Salas, Santiago, La Tinguiña
  - Pisco: Paracas, Independencia, Humay
  - Palpa: Palpa, Llipata
  - Nazca: Vista Alegre
- **Predominio empresarial:** 85%+ productores jurídicos
- **Estacionalidad marcada:** Picos en mayo-junio

## 🗂️ Estructura del Proyecto

```
ica-produce-analysis/
│
├── 📁 data/
│   └── lugar_produccion_ica.csv          # Dataset principal
│
├── 📁 notebooks/
│   ├── 01_EDA_nuevo.ipynb                # Análisis Exploratorio completo
│   └── 02_modelado.ipynb                 # Modelado predictivo y ML
│
├── 📁 outputs/
│   ├── 📁 graficos/                      # Visualizaciones interactivas
│   ├── 📁 resumenes/                     # Reportes y estadísticas
│   ├── 📁 models/                        # Modelos entrenados
│   └── dashboard.html                    # Dashboard principal
│
├── 📁 src/
│   ├── processing.py                     # Funciones de procesamiento
│   └── utils.py                         # Utilidades generales
│
├── main.py                              # Script principal de análisis
├── requirements.txt                     # Dependencias del proyecto
└── README.md                           # Este archivo
```

## Nueva estructura Clean Code

El proyecto ha sido reestructurado para seguir una organización modular y mantenible. El código fuente ahora se encuentra en la carpeta `src/` y se divide en módulos según su funcionalidad:

```
├── src/
│   ├── config.py
│   ├── main.py
│   └── utils/
│       ├── data_loader.py
│       ├── preprocessing.py
│       ├── analysis.py
│       ├── visualization.py
│       ├── reports.py
│       └── dashboard.py
```

- Ejecuta el análisis con:
  ```bash
  python -m src.main
  ```
- Los datos de entrada van en `data/` y los resultados en `outputs/`.

## 📥 Fuente del Dataset

El dataset principal fue obtenido de:
[Datos Abiertos del Gobierno del Perú](https://datosabiertos.gob.pe/dataset/lugar-de-producci%C3%B3n-en-la-regi%C3%B3n-de-ica)

## 🚀 Instalación y Uso

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd ica-produce-analysis
```

### 2. Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar Análisis

```bash
# Ejecutar análisis completo
python main.py

# O usar notebooks interactivos
jupyter notebook notebooks/01_EDA_nuevo.ipynb
```

### 5. Ver Resultados

- **Dashboard Principal**: `outputs/dashboard.html`
- **Visualizaciones**: Carpeta `outputs/graficos/`
- **Reportes**: Carpeta `outputs/resumenes/`

## 📊 Análisis Desarrollados

### 1. 📈 Análisis Exploratorio de Datos (EDA)

- **Distribución geográfica** por provincia y distrito
- **Tendencias temporales** y estacionalidad
- **Top productos** más certificados
- **Análisis de rendimiento** por cultivo
- **Segmentación** por tipo de productor

### 2. 🤖 Modelado Predictivo

- **Regresión Lineal/Random Forest**: Predicción de rendimientos
- **Clustering K-Means**: Segmentación de productores (4 clusters)
- **PCA**: Reducción de dimensionalidad y análisis de componentes
- **Clasificación**: Predicción de tipo de productor

### 3. 📊 Visualizaciones Interactivas

- **Gráficos Plotly**: Interactivos y profesionales
- **Mapas de calor**: Distribución temporal y geográfica
- **Dashboard HTML**: Resumen ejecutivo integrado
- **Scatter plots**: Análisis de correlaciones

## 🔍 Tecnologías Utilizadas

### Core Data Science
- **Python 3.13.5**: Lenguaje principal
- **Pandas**: Manipulación de datos
- **NumPy**: Computación numérica
- **Matplotlib/Seaborn**: Visualización estática

### Machine Learning
- **Scikit-learn**: Algoritmos de ML
- **Joblib**: Serialización de modelos
- **StandardScaler**: Normalización de datos

### Visualización Avanzada
- **Plotly**: Gráficos interactivos
- **Plotly Express**: API simplificada
- **Kaleido**: Exportación de gráficos

### Notebooks y Desarrollo
- **Jupyter**: Notebooks interactivos
- **IPywidgets**: Widgets interactivos

## 📋 Resultados Principales

### 🎯 Modelo de Regresión
- **R² Score**: 0.85+ (Variable según algoritmo)
- **Variables importantes**: Área, cultivo, provincia, distrito
- **RMSE**: Optimizado para predicción de rendimientos

### � Clustering de Productores
- **4 Clusters identificados**:
  - **Cluster 0**: Productores Pequeños
  - **Cluster 1**: Productores Eficientes
  - **Cluster 2**: Productores Grandes
  - **Cluster 3**: Productores Diversificados

### 📊 Clasificación
- **Accuracy**: 90%+ en predicción de tipo de productor
- **Variables clave**: Área total, diversidad de cultivos, rendimiento

## 💡 Insights Estratégicos

### 🌾 Producción
1. **Arándano** domina las certificaciones (cultivo estrella)
2. **Pisco** lidera en número de certificaciones por provincia
3. **Estacionalidad marcada** con picos en mayo-junio
4. **Alta concentración** geográfica en pocos distritos

### 👨‍🌾 Productores
1. **Predominio empresarial**: 85%+ productores jurídicos
2. **4 tipologías** claras de productores identificadas
3. **Oportunidad** de apoyo a pequeños productores
4. **Diversificación** variable según tamaño

### 📈 Recomendaciones
1. **Fortalecer** cadena productiva del arándano
2. **Apoyar** desarrollo de pequeños productores
3. **Expandir** certificación en distritos menos participativos
4. **Optimizar** procesos en época de alta demanda
5. **Promover** diversificación en productores grandes

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor: @MiguelVivar

**Analista de Datos Especializado en Agroindustria Peruana**

- 🔬 Enfoque en economía regional y comercio exterior
- 📊 Experiencia en análisis de datos agrícolas y agroindustriales
- 🌱 Especialista en producción agrícola de la región Ica
- 📍 Basado en Perú
- 💼 Contacto: [LinkedIn](https://www.linkedin.com/in/miguel-vivar-farfan/) | [Email](mailto:miguelvivarfarfan@gmail.com)

---

**⭐ Si este proyecto te resulta útil, ¡considera darle una estrella y compartirlo!**

---

### 📢 ¡Tu contribución es bienvenida!
¿Tienes ideas, mejoras o detectaste algún error? No dudes en abrir un issue o un pull request. Juntos podemos potenciar el análisis de la agroindustria peruana.

