# Infovis - Visualización de Datos — Exploraciones y Proyecto Personal

Repositorio desarrollado en el marco de la **Maestría en Ciencia de Datos**,  
materia **Visualización de Datos** (Prof. Ariel Aizemberg).

Contiene:

- exploraciones en herramientas de visualización  
- desarrollo de un proyecto personal de integración de datos digitales  
- pipeline reproducible de procesamiento y generación de datasets visuales

Herramientas exploradas:

RAWGraphs · Flourish · DataWrapper 

---

## Visualización online de herramientas exploradas

👉 https://jigarcia-2.github.io/infovis/

---

## Estructura del repositorio
```text
.
INFOVIS/
│
├── index.html
├── README.md
│
├── exploraciones/
│   ├── datawrapper.html
│   ├── flourish.html
│   └── horizon_chart.svg
│
└── visualizacion_datos_personales/
    │
    ├── .gitignore
    ├── index.html
    │
    ├── data/
    │   ├── README.md 
    │   ├── raw/
    │   ├── processed/
    │   ├── selected/
    │   ├── normalized/
    │   ├── aggregated/
    │   └── final/
    │
    ├── scripts/
    │   ├── 01_ingestion/
    │   ├── 02_processing/
    │   ├── 03_selection/
    │   ├── 04_feature_engineering/
    │   ├── 05_integration/
    │   ├── 06_visualization.py
    │   ├── utils_checks/
    │   └── run_pipeline.py
    │
    └── visualizations/
        ├── charts/
        │   ├── datawrapper.html
        │   ├── flourish.html
        │   ├── rawgraphs_parallel.html
        │   ├── Parallel_coordinates_plot.svg
        │   ├── tableau1.html
        │   └── tableau1.twb
        │
        └── derived_data/
            ├── derived_data_script.R
            ├── viz1_flourish_normalized.csv
            ├── viz1_flourish_normalized.xlsx
            ├── viz2_datawrapper_scatter.csv
            ├── viz2_datawrapper_scatter.xlsx
            ├── viz3_rawgraphs_parallel.csv
            ├── viz3_rawgraphs_parallel.xlsx
            ├── viz4_tableau_topic_heatmap.csv
            └── viz4_tableau_topic_heatmap.xlsx
```

## Proyecto principal : Comportamiento digital y patrones de rutina diaria
### ¿Qué dicen mis datos sobre mí?

El proyecto  de visualizacion de datos personales  integra rastros digitales cotidianos  (Apple Health, Spotify, Netflix, Mercado Libre) para explorar patrones de rutina, movilidad y consumo digital a lo largo del 2025.

Pipeline: ingestión → procesamiento → integración → visualización.

El enfoque es **exploratorio, narrativo y reproducible**.

---
## Visualizaciones desarrolladas

| Herramienta | Tipo | Pregunta |
|---|---|---|
| Tableau | Bubble Heatmap | ¿Qué géneros de Netflix dominaron cada día de mi semana? |
| Flourish | Line Chart | ¿Cómo influyó mi movilidad en el consumo digital? |
| RAWGraphs | Parallel Coordinates | ¿Qué días combinan más compras, más música y más Netflix? |
| Datawrapper | Scatter Plot | ¿Cuando aumenta la música, disminuye Netflix? |

---

## Visualización online del proyecto principal


 👉 https://jigarcia-2.github.io/infovis/visualizacion_datos_personales/

---

## Privacidad

Los datos originales no se publican por contener información personal.

El repositorio incluye:

- pipeline reproducible  
- datasets agregados  
- visualizaciones finales  

---

**Jimena Taciana García**  
Médica · Maestría en Ciencia de Datos
