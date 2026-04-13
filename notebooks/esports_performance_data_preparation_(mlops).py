import pandas as pd
import numpy as np
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

np.random.seed(42)

n_rows = 1000
games = ['League of Legends', 'Valorant', 'Dota 2', 'CS:GO', 'Apex Legends', 'LoL', 'valorant'] # Incluye duplicados inconsistentes
regions = ['NA', 'EUW', 'KR', 'LAN', 'BR', 'na', 'euw']

data = {
    'player_id': [f"PL_{1000 + i}" for i in range(n_rows)],
    'player_name': [f"ProPlayer_{i}" for i in range(n_rows)],
    'game_title': [random.choice(games) for _ in range(n_rows)],
    'region': [random.choice(regions) for _ in range(n_rows)],
    'age': np.random.randint(16, 35, n_rows),
    'hours_played_weekly': np.random.normal(50, 15, n_rows).round(1),
    'win_rate': np.random.uniform(0.4, 0.75, n_rows).round(2),
    'kda_ratio': np.random.uniform(1.5, 4.5, n_rows).round(2),
    'average_apm': np.random.normal(250, 50, n_rows).round(0), # Actions Per Minute
    'tournaments_played': np.random.randint(0, 50, n_rows),
    'followers_count': np.random.exponential(100000, n_rows).astype(int),
    'avg_viewers': np.random.normal(2000, 1500, n_rows).round(0),
    'sponsor_count': np.random.randint(0, 10, n_rows),
    'contract_years_left': np.random.randint(0, 5, n_rows),
    'monthly_revenue_usd': np.random.normal(5000, 2000, n_rows).round(2)
}

df = pd.DataFrame(data)

df.loc[df.sample(frac=0.05).index, 'followers_count'] = np.nan
df.loc[df.sample(frac=0.03).index, 'monthly_revenue_usd'] = np.nan

df.at[10, 'hours_played_weekly'] = 200 # Más horas de las que tiene la semana
df.at[25, 'win_rate'] = 5.5 # Porcentaje mayor a 1 (o 100)

df = pd.concat([df, df.iloc[[50, 150, 250]]], ignore_index=True)

df.to_csv('esports_pro_players_dataset.csv', index=False)
print("¡Archivo 'esports_pro_players_dataset.csv' generado con éxito!")

df = pd.read_csv('esports_pro_players_dataset.csv')

print("--- Información General ---")
print(df.info())

print("\n--- Estadísticas Descriptivas ---")
print(df.describe())

outliers_winrate = df[df['win_rate'] > 1.0]
print(f"Jugadores con Win Rate imposible: {len(outliers_winrate)}")

outliers_hours = df[df['hours_played_weekly'] > 168]
print(f"Jugadores con horas imposibles: {len(outliers_hours)}")

print(f"Valores nulos por columna:\n{df.isnull().sum()}")
print(f"\nCantidad de registros duplicados: {df.duplicated().sum()}")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(df['monthly_revenue_usd'], kde=True, color='teal')
plt.title('Distribución de Ingresos Mensuales')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='followers_count', y='monthly_revenue_usd', hue='region')
plt.title('Relación: Seguidores vs Ingresos')
plt.show()

median_followers = df['followers_count'].median()
df['followers_count'] = df['followers_count'].fillna(median_followers)

mean_revenue = df['monthly_revenue_usd'].mean()
df['monthly_revenue_usd'] = df['monthly_revenue_usd'].fillna(mean_revenue)

game_mapping = {
    'LoL': 'League of Legends',
    'valorant': 'Valorant'
}
df['game_title'] = df['game_title'].replace(game_mapping)

df['region'] = df['region'].str.upper().str.strip()

df.loc[df['win_rate'] > 1.0, 'win_rate'] = 0.5 # Asignamos un valor neutro o el máximo lógico

df.loc[df['hours_played_weekly'] > 168, 'hours_played_weekly'] = 168

df = df.drop_duplicates()

df = df.reset_index(drop=True)

df.to_csv('esports_cleaned.csv', index=False)
print("¡Limpieza completada! El dataset está listo para el análisis.")

X = df.drop(['player_id', 'player_name', 'monthly_revenue_usd'], axis=1)
y = df['monthly_revenue_usd']

X_train_temp, X_test, y_train_temp, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_temp, y_train_temp, test_size=0.176, random_state=42 # 0.176 de 0.85 es aprox 0.15
)

print(f"Registros totales: {len(df)}")
print(f"Entrenamiento: {len(X_train)}")
print(f"Validación: {len(X_val)}")
print(f"Prueba: {len(X_test)}")

df = pd.read_csv('esports_pro_players_dataset.csv')

print(f"Duplicados encontrados: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)

counts = df.nunique()
to_del = [i for i, v in counts.items() if v == 1]
df.drop(columns=to_del, inplace=True)
print(f"Columnas eliminadas por ser constantes: {to_del}")

df['followers_count'] = df['followers_count'].fillna(df['followers_count'].median())
df['monthly_revenue_usd'] = df['monthly_revenue_usd'].fillna(df['monthly_revenue_usd'].mean())

df.to_csv('esports_cleaned .v2.csv', index=False)
