import numpy as np
from pyod.models.cblof import CBLOF
from pyod.models.pca import PCA
from pyod.utils.data import generate_data

# Генерация синтетических данных для примера
X_train, X_test, y_train, y_test = generate_data(n_train=200, n_test=100, n_features=5, contamination=0.1, random_state=42)

# Метод CBLOF
clf_cblof = CBLOF()
clf_cblof.fit(X_train)
y_test_pred_cblof = clf_cblof.predict(X_test)

# Метод PCA
clf_pca = PCA()
clf_pca.fit(X_train)
y_test_pred_pca = clf_pca.predict(X_test)

# Вывод результатов
print("Результаты метода CBLOF:")
print(y_test_pred_cblof)

print("\nРезультаты метода PCA:")
print(y_test_pred_pca)
