
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet, BayesianRidge, PassiveAggressiveRegressor
)
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from tqdm.auto import tqdm
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



# Número de muestras
n = 2000

# Parámetros físicos realistas
P_in = np.random.uniform(5, 8, n)  # Presión de entrada (atm)
T_in = np.random.uniform(-200, -180, n)  # Temperatura de entrada (°C)

# Relación entre presión, temperatura y caudal de alimentación
flow_rate = 500 + 20 * (P_in - 6.5) - 1.5 * (T_in + 190) + np.random.normal(0, 5, n)  # kg/h

# Consumo energético basado en flujo y temperatura
energy_consumed = 100 + 0.8 * flow_rate + 0.2 * (T_in + 190) + np.random.normal(0, 5, n)  # kWh

# Simulación de eficiencias de separación
efficiency = np.clip(0.85 + 0.005 * (P_in - 6.5) - 0.002 * (T_in + 190), 0.80, 0.90)  # %

# Composición de salida con relaciones físicas
N2_out = np.clip(99.8 + 0.02 * (P_in - 6.5) - 0.01 * (T_in + 190) + np.random.normal(0, 0.02, n), 99.75, 99.95)
O2_out = np.clip(99.5 + 0.03 * (P_in - 6.5) - 0.015 * (T_in + 190) + np.random.normal(0, 0.03, n), 99.40, 99.60)
Ar_out = np.clip(95 + 0.04 * (P_in - 6.5) - 0.02 * (T_in + 190) + np.random.normal(0, 0.05, n), 94.5, 99.5)

# Crear DataFrame
df = pd.DataFrame({
    'P_in (atm)': P_in,
    'T_in (°C)': T_in,
    'Flow Rate (kg/h)': flow_rate,
    'Energy Consumed (kWh)': energy_consumed,
    'Efficiency': efficiency,
    'N2_out (%)': N2_out,
    'O2_out (%)': O2_out,
    'Ar_out (%)': Ar_out
})

# Guardar a CSV
df.to_csv("better_air_separation_data_2000.csv", index=False)

# Mostrar las primeras filas
print(df.head())


df = pd.read_csv("/home/titansax/simulations/better_air_separation_data_2000.csv");

# Load columns

df.head()

# Colum names array

df.columns

# Check data types

df.info()

# Check null values
    
df.isnull().sum()

# Check number of unique values

df.nunique()

# Eliminar filas con valores nulos
df = df.dropna()

# Verificar si hay valores atípicos
print(df.describe(percentiles=[0.01, 0.99]))

# Variables de entrada y salida
X = df[['P_in (atm)', 'T_in (°C)', 'Flow Rate (kg/h)', 'Energy Consumed (kWh)', 'Efficiency']]
Y = df[['N2_out (%)', 'O2_out (%)', 'Ar_out (%)']]

# División en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, Y_train)

# Evaluar modelo
Y_pred = modelo_rf.predict(X_test)
score = r2_score(Y_test, Y_pred)
print(f"Random Forest Precisión R²: {score:.4f}")

# Exportar modelo
joblib.dump(modelo_rf, "random_forest_model.pkl")
print("Modelo Random Forest guardado como 'random_forest_model.pkl'")
