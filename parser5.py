import pandas as pd
import json

# Чтение данных из JSON-файла
with open('bank_client_requests.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

# Преобразование данных в DataFrame
df = pd.DataFrame(data)

# Вывод структуры данных
print(df)

# Пример запроса данных (например, запрос всех клиентов, у которых возраст больше 30 лет)
result = df[df['age'] > 30]
print(result)
