import pandas as pd
from sklearn.model_selection import train_test_split
from skrebate import ReliefF
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

df = pd.read_csv('esports_cleaned .v2.csv')

features_esports = [
    'hours_played_weekly', 
    'win_rate', 
    'kda_ratio', 
    'average_apm', 
    'tournaments_played'
]

X = df[features_esports]
y = df['monthly_revenue_usd']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

if not os.path.exists('models'): os.makedirs('models')
joblib.dump(model, 'models/random_forest_esports.pkl')
joblib.dump(features_esports, 'models/feature_names.pkl')

print("✅ Modelo generado con éxito con columnas de rendimiento de juego.")
