import pandas as pd
import joblib
import os

# 1. Cargar el modelo
model = joblib.load('models/random_forest_esports.pkl')

# 2. DEFINIR EL ORDEN OFICIAL (Basado en tu fit previo)
# Este es el orden exacto que exige el error
cols_ordenadas = [
    'hours_played_weekly', 
    'win_rate', 
    'kda_ratio', 
    'average_apm', 
    'tournaments_played'
]

# 3. Leer datos
df_input = pd.read_csv('input_data.csv')

# 4. ALINEACIÓN FORZADA (Esto es lo más importante)
# Reorganizamos el DataFrame para que las columnas sigan el orden de cols_ordenadas
try:
    X_test = df_input[cols_ordenadas]
    
    # 5. Predicción
    predicciones = model.predict(X_test)
    print("✅ Inferencia exitosa. Resultados:")
    print(predicciones)
    
except KeyError as e:
    print(f"❌ Error: El CSV no tiene la columna necesaria: {e}")