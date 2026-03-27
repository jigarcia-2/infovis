# Pipeline de datos — 

Esta carpeta contiene el flujo completo de procesamiento de datos utilizado para construir el dataset integrado del proyecto:

El objetivo  es transformar datos personales provenientes de múltiples plataformas digitales en un dataset estructurado a nivel diario, apto para análisis exploratorio y visualización.

---

## Flujo conceptual de transformación de datos

El procesamiento sigue una lógica progresiva de refinamiento estructural:

raw → processed → normalized → selected → aggregated → final  

Cada etapa representa una instancia específica del pipeline:

- **raw** → datos originales exportados desde las plataformas digitales  
- **processed** → parsing inicial y conversión a formato tabular  
- **normalized** → estandarización temporal y homogeneización estructural  
- **selected** → selección de variables relevantes para el análisis  
- **aggregated** → agregación diaria por fuente de datos  
- **final** → dataset integrado analítico  

Adicionalmente, se genera un dataset derivado optimizado para visualización.

---

## Fuentes de datos

El proyecto integra datos personales provenientes de distintas plataformas digitales:

- Apple Health → actividad física y movilidad diaria  
- Spotify → consumo musical  
- Podcasts → consumo de contenido hablado  
- Netflix → comportamiento audiovisual  
- Mercado Libre → comportamiento de compras online  

Todos los datos se agregan a nivel **diario**, utilizando el huso horario de Argentina como referencia temporal.

---

## Estructura de carpetas

Cada carpeta corresponde a una etapa del pipeline de procesamiento:

- `raw/` → datos originales sin procesar  
- `processed/` → datos transformados a formato tabular  
- `normalized/` → datos con estandarización temporal  
- `selected/` → variables analíticas seleccionadas  
- `aggregated/` → datasets diarios por fuente  
- `final/` → dataset integrado final  

---

## Datasets finales

Se generan dos datasets finales:

### Dataset analítico integrado  
`data/final/behavior_daily_final.(csv | xlsx)`

Contiene la integración completa de todas las fuentes de datos.

### Dataset derivado para visualización  
`data/final/behavior_daily_viz.(csv | xlsx)`

Incluye transformaciones adicionales orientadas a la narrativa visual:

- redondeo de métricas  
- simplificación de variables  
- renombrado de columnas  
- selección de variables relevantes para visualización  

---

## Variables principales del dataset de visualización

El dataset derivado contiene variables agregadas a nivel diario organizadas en distintas dimensiones:

**Dimensión temporal**
- date  
- weekday  
- month  
- year  

**Movilidad y actividad física**
- steps  
- distance_km  
- calorias  

**Consumo digital**
- music_minutes  
- podcast_minutes  
- netflix_minutes  
- netflix_interactions  

**Categorización de consumo**
- music_main_context  
- podcast_main_topic  
- netflix_content_topic  

**Comportamiento de compras**
- ml_purchases  
- ml_main_category  

---

## Privacidad

Los datos personales originales no se incluyen en el repositorio.

Se publican únicamente:

- datasets agregados a nivel diario  
- scripts de procesamiento reproducible  
- documentación metodológica  
- outputs analíticos y visuales  



