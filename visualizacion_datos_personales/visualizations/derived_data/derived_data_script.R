# ============================================
# DERIVED DATA SCRIPT
# Genera datasets optimizados para visualización final
# Exporta cada dataset en CSV + XLSX
# ============================================

library(dplyr)
library(readr)
library(lubridate)
library(tidyr)
library(openxlsx)

# ============================================
# PATHS
# ============================================

INPUT_FILE <- "../../data/final/behavior_daily_viz.csv"
OUTPUT_DIR <- "."

if (!dir.exists(OUTPUT_DIR)) {
  dir.create(OUTPUT_DIR, recursive = TRUE)
}

# ============================================
# FUNCIÓN EXPORTACIÓN
# ============================================

export_all <- function(data, name, output_dir) {
  write_csv(data, file.path(output_dir, paste0(name, ".csv")))
  write.xlsx(data, file.path(output_dir, paste0(name, ".xlsx")), overwrite = TRUE)
  cat("✔ Dataset exportado:", name, "\n")
}

# ============================================
# CARGA DE DATOS
# ============================================

df <- read_csv(INPUT_FILE, show_col_types = FALSE)

cat("Dataset cargado correctamente\n")
cat("Número de filas:", nrow(df), "\n")
cat("Número de columnas:", ncol(df), "\n")

# ============================================
# TRANSFORMACIONES BÁSICAS
# ============================================

month_labels_en <- c(
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
)

df <- df %>%
  mutate(
    date = as.Date(date),
    weekday = factor(
      weekday,
      levels = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    ),
    month_num = month(date),
    month_label = factor(
      month_labels_en[month_num],
      levels = month_labels_en
    ),
    year = year(date)
  )

# ============================================
# DATASET 1 — FLOURISH
# LÍNEAS MENSUALES NORMALIZADAS
# ============================================

viz1_flourish_normalized <- df %>%
  group_by(year, month_num, month_label) %>%
  summarise(
    distance_km = mean(distance_km, na.rm = TRUE),
    netflix_minutes = mean(netflix_minutes, na.rm = TRUE),
    music_minutes = mean(music_minutes, na.rm = TRUE),
    podcast_minutes = mean(podcast_minutes, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    distance_norm_max = distance_km / max(distance_km, na.rm = TRUE),
    netflix_norm_max = netflix_minutes / max(netflix_minutes, na.rm = TRUE),
    music_norm_max = music_minutes / max(music_minutes, na.rm = TRUE),
    podcast_norm_max = podcast_minutes / max(podcast_minutes, na.rm = TRUE)
  ) %>%
  mutate(
    month_label = as.character(month_label),
    distance_km = round(distance_km, 2),
    netflix_minutes = round(netflix_minutes, 0),
    music_minutes = round(music_minutes, 0),
    podcast_minutes = round(podcast_minutes, 0),
    distance_norm_max = round(distance_norm_max, 2),
    netflix_norm_max = round(netflix_norm_max, 2),
    music_norm_max = round(music_norm_max, 2),
    podcast_norm_max = round(podcast_norm_max, 2)
  ) %>%
  arrange(year, month_num)

export_all(viz1_flourish_normalized, "viz1_flourish_normalized", OUTPUT_DIR)

# ============================================
# DATASET 2 — DATAWRAPPER
# SCATTER DE CORRELACIONES
# 84 puntos = 12 meses x 7 weekdays
# ============================================

viz2_datawrapper_scatter <- df %>%
  group_by(year, month_num, month_label, weekday) %>%
  summarise(
    netflix_minutes = mean(netflix_minutes, na.rm = TRUE),
    ml_purchases_total = sum(ml_purchases, na.rm = TRUE),
    music_minutes = mean(music_minutes, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    month_label = as.character(month_label),
    netflix_minutes = round(netflix_minutes, 0),
    music_minutes = round(music_minutes, 0),
    ml_purchases_total = round(ml_purchases_total, 0)
  ) %>%
  arrange(month_num, weekday)

export_all(viz2_datawrapper_scatter, "viz2_datawrapper_scatter", OUTPUT_DIR)

# ============================================
# DATASET 3 — RAWGRAPHS
# COORDENADAS PARALELAS
# PERFIL SEMANAL PROMEDIO
# ============================================

viz3_rawgraphs_parallel <- df %>%
  group_by(weekday) %>%
  summarise(
    netflix_minutes = mean(netflix_minutes, na.rm = TRUE),
    ml_purchases_total = sum(ml_purchases, na.rm = TRUE),
    music_minutes = mean(music_minutes, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    netflix_minutes = round(netflix_minutes, 0),
    music_minutes = round(music_minutes, 0),
    ml_purchases_total = round(ml_purchases_total, 0)
  )

export_all(viz3_rawgraphs_parallel, "viz3_rawgraphs_parallel", OUTPUT_DIR)

# ============================================
# DATASET 4 — TABLEAU
# HEATMAP WEEKDAY × NETFLIX TOPIC
# ============================================

viz4_tableau_topic_heatmap <- df %>%
  filter(
    !is.na(netflix_content_topic),
    netflix_content_topic != "sin_netflix"
  ) %>%
  group_by(weekday, netflix_content_topic) %>%
  summarise(
    dias = n(),
    netflix_minutes = mean(netflix_minutes, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    dias = round(dias, 0),
    netflix_minutes = round(netflix_minutes, 0)
  ) %>%
  arrange(weekday, desc(dias))

export_all(viz4_tableau_topic_heatmap, "viz4_tableau_topic_heatmap", OUTPUT_DIR)

# ============================================
cat("========================================\n")
cat("DERIVED DATA GENERATION COMPLETED\n")
cat("CSV + XLSX GENERADOS\n")
cat("========================================\n")

