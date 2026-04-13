import pandas as pd
import joblib
import os

model = joblib.load('models/random_forest_esports.pkl')

cols_ordenadas = [
    'hours_played_weekly', 
    'win_rate', 
    'kda_ratio', 
    'average_apm', 
    'tournaments_played'
]

df_input = pd.read_csv('input_data.csv')

try:
    X_test = df_input[cols_ordenadas]
    
    predicciones = model.predict(X_test)
    print("✅ Inferencia exitosa. Resultados:")
    print(predicciones)
    
except KeyError as e:
    print(f"❌ Error: El CSV no tiene la columna necesaria: {e}")
