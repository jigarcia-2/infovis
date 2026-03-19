# Comportamiento Digital y Patrones de Rutina Diaria  

Proyecto personal desarrollado en el marco de la materia **Visualización de Datos**, perteneciente a la Maestría en Ciencia de Datos (ITBA).

## Descripción del proyecto  

Este proyecto explora datos digitales personales generados durante el año 2025 con el propósito de transformarlos en una narrativa visual orientada a la identificación de patrones de comportamiento cotidiano.

A partir de fuentes digitales autogeneradas provenientes de plataformas online y sensores integrados en dispositivos móviles, se construyó un dataset analítico que permite observar distintas dimensiones de la vida diaria.

Las áreas analizadas incluyen:

- patrones de movilidad cotidiana  
- consumo de contenido digital de ocio  
- hábitos de compra en plataformas de comercio electrónico  

---

## Hipótesis exploratoria  

El análisis se orienta a explorar:

- la posible existencia de perfiles conductuales diarios recurrentes  
- la relación entre patrones de movilidad y consumo de contenido digital  
- la presencia de dinámicas temporales en los hábitos de compra online  

El objetivo es identificar posibles asociaciones y regularidades en el comportamiento cotidiano a partir de datos autogenerados.

---
## Enfoque metodológico  

El proyecto articula:

- el flujo clásico de trabajo en Ciencia de Datos  
- el proceso de visualización de datos propuesto por **Ben Fry**  

El dataset fue diseñado con un enfoque orientado a la visualización como herramienta narrativa y de interpretación. 

---
## Flujo de trabajo implementado para la generacion del dataset 

El desarrollo del proyecto incluyó las siguientes etapas:

1. Ingesta de archivos originales en múltiples formatos (XML, JSON, CSV)  
2. Transformación de estructuras jerárquicas a formato tabular  
3. Exploración inicial de variables  
4. Selección de variables relevantes  
5. Limpieza y normalización temporal  
6. Feature engineering y categorización de contenidos  
7. Agregación diaria por fuente de datos  
8. Integración final en un dataset consolidado  
9. Construcción de un dataset derivado optimizado para visualización  

El detalle del proceso de construcción del dataset se encuentra documentado en la carpeta: **data/** (README.md).

---
## Fuentes de datos  

El dataset se construye a partir de múltiples plataformas digitales personales, cada una asociada a distintas dimensiones del comportamiento cotidiano:

- **Apple Health** → métricas de movilidad diaria  
- **Spotify** → hábitos de escucha musical  
- **Podcasts** → consumo de contenido hablado  
- **Netflix** → consumo audiovisual  
- **Mercado Libre** → comportamiento de compra online  

Estas fuentes presentan diferentes niveles de granularidad, estructura y frecuencia de registro, lo que requirió procesos de integración y transformación previos al análisis.

El dataset integrado contiene información agregada a nivel diario proveniente de todas las fuentes.

---

## Dataset final  

Se generan dos versiones del dataset:

### Dataset analítico (pipeline completo)  

`data/final/behavior_daily_final.xlsx`

Corresponde al resultado completo del proceso de integración de datos.

### Dataset optimizado para visualización  

`data/final/behavior_daily_viz.xlsx`

Esta versión deriva del dataset analítico e incluye:

- transformación de variables a escalas interpretables  
- normalización de unidades (km, minutos, calorías)  
- redondeo de métricas continuas  
- selección de variables relevantes para la narrativa visual  

Este dataset es el utilizado para la construcción de las visualizaciones del proyecto.

---

## Visualización del proyecto  

Las visualizaciones desarrolladas se integran en:

**https://jigarcia-2.github.io/infovis/**  

Actualmente, el repositorio presenta una visualización construida con **Tableau**, correspondiente a la primera etapa del desarrollo visual del proyecto.

Se prevé la incorporación progresiva de visualizaciones adicionales utilizando distintas herramientas de visualización de datos, entre ellas:

- RAWGraphs  
- Flourish  
- DataWrapper  
- Tableau  
- Power BI  

Estas herramientas forman parte del proceso de exploración metodológica y aprendizaje en visualización de datos.

---
## Estructura del proyecto  
```text
.
proyecto_visualizacion/
│
├── data/
│ ├── raw/ # datos originales (no públicos)
│ ├── processed/ # parsing inicial
│ ├── normalized/ # normalización temporal
│ ├── selected/ # selección de variables
│ ├── aggregated/ # agregación diaria por fuente
│ └── final/ # dataset finales (analítico y visual)
│
├── scripts/
│ ├── 01_ingestion/
│ ├── 02_processing/
│ ├── 03_selection/
│ ├── 04_feature_engineering/
│ ├── 05_integration/
│ ├── 06_visualization/
│ └── utils_checks/
│
├── visualizations/ # gráficos (en desarrollo)
│
├── .gitignore # exclusión de datos sensibles y archivos intermedios
│
└── README.md
``` 
## Consideraciones de privacidad  

Los datos originales no se comparten debido a que contienen información personal sensible.

El repositorio incluye únicamente:

- código del pipeline  
- documentación metodológica  
- dataset agregado a nivel diario  
- resultados visuales derivados  

=======

