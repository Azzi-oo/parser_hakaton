import pandas as pd
# import matplotlib.pyplot as plt


data = {
    'DATE': ['2023-10-01', '2023-10-02', '2023-10-03'],
    'OPEN': [100.0, 101.0, 102.0],
    'HIGH': [105.0, 106.0, 104.0],
    'LOW': [99.0, 100.0, 101.0],
    'CLOSE': [103.0, 104.0, 102.0],
    'VOLUME': [10000, 12000, 9000]
}

df = pd.DataFrame(data)

# Сохранение данных в CSV-файл
df.to_csv('stock_data.csv', index=False)
# Загрузка данных акций из CSV-файла (замените 'stock_data.csv' на ваш файл)
df = pd.read_csv('stock_data.csv')
df = df.drop('DATE', axis=1)

# Вывод основных статистических данных
print("Основные статистические данные:")
print(df.describe())

# Вывод корреляции между столбцами
print("\nКорреляция между столбцами:")
print(df.corr())

# Визуализация цен закрытия (CLOSE)
# plt.figure(figsize=(12, 6))
# plt.plot(df['DATE'], df['CLOSE'], label='Цена закрытия', color='blue')
# plt.xlabel('Дата')
# plt.ylabel('Цена закрытия')
# plt.title('График цен закрытия акций')
# plt.legend()
# plt.show()

# Дополнительное задание: вывод данных акций с отклонением более 100
deviation_threshold = 100
high_deviation_stocks = df[df['CLOSE'] - df['CLOSE'].mean() > deviation_threshold]
print("\nАкции с отклонением цены закрытия более {} единиц:".format(deviation_threshold))
print(high_deviation_stocks)
