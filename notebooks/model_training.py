import pandas as pd
from sklearn.model_selection import train_test_split
from skrebate import ReliefF
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Asegúrate de cargar el dataset que limpiamos en el paso anterior
df = pd.read_csv('esports_cleaned .v2.csv')

# 2. SELECCIÓN ÓPTIMA (Las que el modelo "no conocía" antes)
features_esports = [
    'hours_played_weekly', 
    'win_rate', 
    'kda_ratio', 
    'average_apm', 
    'tournaments_played'
]

X = df[features_esports]
y = df['monthly_revenue_usd']

# 3. Entrenar el nuevo modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Guardar los nuevos artefactos (Sobreescribiendo los viejos)
if not os.path.exists('models'): os.makedirs('models')
joblib.dump(model, 'models/random_forest_esports.pkl')
joblib.dump(features_esports, 'models/feature_names.pkl')

print("✅ Modelo regenerado con éxito con columnas de rendimiento de juego.")