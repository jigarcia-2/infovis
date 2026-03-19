 # Documentación de los conjuntos de datos

Esta carpeta contiene los distintos conjuntos de datos generados durante el proceso de construcción del dataset integrado del proyecto  
**Comportamiento Digital y Patrones de Rutina Diaria**.

Los archivos aquí presentes corresponden a versiones intermedias en formato CSV que forman parte del flujo de transformación necesario para integrar múltiples fuentes de comportamiento digital personal.

El objetivo de este proceso es consolidar información proveniente de distintas plataformas en un único dataset estructurado, apto para análisis exploratorio y desarrollo de visualizaciones.

La unidad analítica adoptada para la integración de los cinco conjuntos de datos es la **fecha**, considerando el huso horario de Argentina.  
Esta decisión permite analizar patrones conductuales diarios y mantener coherencia temporal entre fuentes heterogéneas.

La organización de los datos respeta una lógica de transformación progresiva, donde cada carpeta representa una etapa específica del flujo de preparación del dataset final.

---
## Esquema conceptual de transformación de datos  

El procesamiento de los datos sigue una lógica progresiva de transformación:

raw → processed → normalized → selected → aggregated → final

Donde cada etapa representa una instancia de refinamiento estructural y analítico:

- **raw** → datos originales exportados desde las distintas plataformas  
- **processed** → parsing inicial y conversión a formato tabular  
- **normalized** → estandarización temporal y homogeneización estructural  
- **selected** → selección de variables relevantes para el análisis  
- **aggregated** → síntesis diaria por fuente de datos  
- **final** → dataset integrado analítico  

Adicionalmente, se generó un dataset derivado optimizado para visualización.

---

## Fuentes de datos originales  

El proyecto integra datos personales provenientes de múltiples plataformas digitales:

- **Apple Health (XML)**  
  Registros de actividad física y movilidad diaria.

- **Spotify Extended Streaming History (JSON)**  
  Historial detallado de reproducción musical.

- **Consumo de podcasts (JSON)**  
  Información sobre escucha de contenido hablado.

- **Mercado Libre (JSON anidado)**  
  Historial de compras online con estructura jerárquica.

- **Netflix (CSV)**  
  Historial de consumo audiovisual.

---

## Estructura de carpetas  

Cada carpeta corresponde a una etapa específica del proceso de transformación:

- `raw/` → datos originales sin procesar  
- `processed/` → datos convertidos a estructura tabular  
- `normalized/` → datos con estandarización temporal  
- `selected/` → subconjunto de variables analíticas  
- `aggregated/` → datasets diarios por fuente  
- `final/` → dataset integrado  
- `visualization/` → dataset derivado para visualización  

---

## Integración final  

El dataset analítico integrado se encuentra en:

`data/final/behavior_daily_final.xlsx`

Este archivo contiene la estructura consolidada resultante del proceso de integración de todas las fuentes.

---

## Dataset derivado para visualización  

Posteriormente a la integración, se realizó una etapa adicional de preparación orientada a la construcción de visualizaciones.

En esta fase se llevaron a cabo las siguientes transformaciones:

- simplificación de variables  
- redondeo de métricas continuas  
- renombrado de columnas  
- eliminación de campos no relevantes para la narrativa visual  

El dataset resultante es:

`data/final/behavior_daily_viz.xlsx`

Este archivo es el utilizado en las visualizaciones desarrolladas en el proyecto.

---
## Variables del dataset orientado a visualización  

El dataset derivado para visualización contiene variables agregadas a nivel diario, organizadas en distintas dimensiones analíticas:

### Dimensión temporal  
- `date`  
- `weekday`  
- `month`  
- `year`  

### Movilidad y actividad física  
- `steps`  
- `distance_km`  
- `calories`  

### Consumo digital  
- `music_minutes`  
- `podcast_minutes`  
- `netflix_minutes`  
- `netflix_interactions`  

### Categorizaciones principales de consumo  
- `music_main_type`  
- `music_main_origin`  
- `podcast_main_topic`  
- `netflix_main_topic`  

### Comportamiento de compra online  
- `ml_purchases`  
- `ml_main_category`  

Estas variables permiten representar de forma sintética distintas dimensiones del comportamiento digital cotidiano y facilitan la construcción de una narrativa visual integrada.

---

## Consideraciones de privacidad  

Los datos originales no se incluyen en el repositorio debido a que contienen información personal sensible.

El proyecto publica únicamente:

- datasets agregados a nivel diario  
- scripts de transformación de datos  
- documentación metodológica  
- resultados visuales derivados  