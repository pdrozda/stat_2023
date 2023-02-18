import numpy as np
import sklearn.linear_model as sl


# mamy 3 zmienne objaśniające x1,x2,x3 i zmienną objaśnianą y
x = [[1, 2, 3], [5, 1, 5], [15, 2, 7], [25, 5, 5], [35, 11, 13], [45, 15, 12], [55, 34, 45], [60, 35, 12]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

# y = a1* x1 + a2*x2 + a3*x3 + b
x = np.array(x)
y = np.array(y)
print(x)
print(y)
model_regresji = sl.LinearRegression()
model_regresji.fit(x, y)
print('Wartość wyrazu wolnego:', model_regresji.intercept_)
print('Wartości współczynników przy x1, x2, x3:', model_regresji.coef_)
# y = 0.47*x1 + 0.21*x2 + 0.03*x3 + 5.05
R_sq = model_regresji.score(x, y)
print('Współczynnik determinacji:', R_sq)
y_prognoza = model_regresji.predict(x)
print(y_prognoza.round(2))

y_prognoza_1 = model_regresji.predict([[4, 8, 20]])
print(y_prognoza_1.round(2))

from sklearn.ensemble import RandomForestRegressor
model_regresji_rf = RandomForestRegressor()
model_regresji_rf.fit(x, y)
print('Istotność poszczególnych zmiennych x1, x2, x3',model_regresji_rf.feature_importances_)
R_sq_rf = model_regresji_rf.score(x, y)
print('Współczynnik determinacji:', R_sq_rf)
y_prognoza_rf = model_regresji_rf.predict(x)
print('Prognozy Random Forest', y_prognoza_rf.round(2))

from sklearn.svm import LinearSVR
model_regresji_svr = LinearSVR()
model_regresji_svr.fit(x, y)
print('współczynniki modelu:', model_regresji_svr.coef_)
R_sq_svr = model_regresji_svr.score(x, y)
print('Współczynnik determinacji:', R_sq_svr)
y_prognoza_svr = model_regresji_svr.predict(x)
print(y_prognoza_svr)