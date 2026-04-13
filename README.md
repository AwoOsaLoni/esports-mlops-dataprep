eSports Revenue Prediction System 🎮📊

MLOps Pipeline: Lab III Finalizado - Maestría en Informática
Este proyecto implementa un sistema de orquestación de contenedores para el despliegue de un modelo de Machine Learning (Random Forest) enfocado en la predicción de ingresos mensuales para jugadores de eSports. El sistema está diseñado siguiendo principios de MLOps para garantizar la reproducibilidad y el aislamiento del entorno.

🚀 Arquitectura del Proyecto
El sistema utiliza una arquitectura basada en Docker, permitiendo que el modelo de inferencia se ejecute de forma independiente al sistema operativo "Host".

Stack Tecnológico
Lenguaje: Python 3.9

ML Framework: Scikit-learn (Random Forest Regressor)

Contenerización: Docker & Docker Compose

📁 Estructura de Archivos
Plaintext
.
├── models/
│   ├── random_forest_esports.pkl  # Artefacto del modelo entrenado
│   └── feature_names.pkl          # Metadatos del esquema de datos
├── notebooks/
│   └── esports_performance_data_preparation_(mlops).py      # Generacion y limpieza de los datos
|   └── model_training.py                                    # Entrenamiento y generacion de los modelos (.plk)
├── src/
│   └── predict_service.py         # Versión script para producción
├── Dockerfile                     # Receta de la imagen del contenedor
├── docker-compose.yml             # Orquestador de servicios
├── input_data.csv                 # Datos de entrada para predicción
├── requirements.txt               # Dependencias del sistema
└── README.md                      # Documentación del proyecto
🛠️ Configuración y Ejecución local
Requisitos Previos
Docker Desktop instalado y en ejecución.

VS Code con la extensión de Docker (recomendado).

Pasos para levantar el sistema
Preparar los datos: Asegúrese de que input_data.csv contenga las columnas requeridas (average_apm, hours_played_weekly, kda_ratio, tournaments_played, win_rate).

Construir y Ejecutar: Abra una terminal en la raíz del proyecto y ejecute:

Bash
docker-compose up --build
Finalización: El sistema realizará la inferencia, imprimirá los resultados en la terminal y el contenedor se detendrá automáticamente (Exit Code 0).

🧠 Implementación de MLOps
Validación de Esquema (Step 5 & 6)
El sistema incluye una capa de Feature Alignment. Se asegura de que los datos de entrada coincidan estrictamente en nombre y orden con los datos utilizados durante el entrenamiento (fit), mitigando el error de Training-Serving Skew.

Ciclo de Vida del Contenedor
Se configuró una política de restart: no en el orquestador para manejar el proceso como un Batch Job, optimizando el uso de recursos y permitiendo una integración continua limpia.

📈 Resultados de Inferencia
El modelo entrega un vector de predicciones en formato USD. Ejemplo de salida exitosa:
✅ Inferencia exitosa. Resultados: [4777.22, 5357.14, 5181.37]

👤 Autor
Silvio Rainel Garcia Rondón
Estudiante de Maestría en Informática y Tecnologías Computacionales
Universidad Autónoma de Aguascalientes
Aguascalientes, México - 2026
