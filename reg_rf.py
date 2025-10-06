import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv(r"data\merged.csv")

df = df[(df["flow"] >= 0) & (df["level"] >= 0) & (df["flow"] <= 200)]

df["flow_norm"] = (df["flow"] - df["flow"].min()) / (df["flow"].max() - df["flow"].min())
df["level_norm"] = (df["level"] - df["level"].min()) / (df["level"].max() - df["level"].min())

X = df[["level_norm"]]
y = df["flow_norm"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

pred = rf.predict(X_test)

r2 = r2_score(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("R2:", round(r2, 4))
print("RMSE:", round(rmse, 4))
