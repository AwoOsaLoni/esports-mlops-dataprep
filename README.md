# 🎮 eSports Performance Data Preparation (MLOps)

Este proyecto aplica los procesos de la metodología **MLOps** y técnicas de limpieza de datos del libro *"Data Preparation for Machine Learning"* de Jason Brownlee.

## 📁 Estructura del Repositorio
- `data/raw/`: Dataset original con inconsistencias y valores nulos.
- `data/processed/`: Dataset curado tras aplicar limpieza estadística.
- `notebooks/`: Proceso detallado de exploración (Paso b) y limpieza (Paso c).

## 🛠️ Procesos Aplicados (Cap. 3 y 5)
1. **Identificación de Duplicados:** Eliminación de registros repetidos (Sección 5.8).
2. **Análisis de Varianza:** Remoción de columnas constantes o con información redundante (Sección 5.3).
3. **Imputación de Nulos:** Uso de mediana para variables numéricas (Capítulo 3).
4. **Validación de Rangos:** Corrección de valores atípicos (outliers) en desempeño.
