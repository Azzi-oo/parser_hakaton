import requests
from bs4 import BeautifulSoup
import csv
import time

# Функция для получения курсов валют и записи их в CSV файл
def scrape_sberbank_data():
    # URL веб-сайта Сбербанка
    url = "https://www.sberbank.ru"

    # Отправляем GET-запрос
    response = requests.get(url, verify=False)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для разбора страницы
        soup = BeautifulSoup(response.text, "html.parser")

        # Найдите и извлеките курсы валют
        usd_element = soup.find("div", class_="currency-plate--usd")
        eur_element = soup.find("div", class_="currency-plate--eur")

        if usd_element and eur_element:
            usd_rate = usd_element.find("div", class_="currency-plate--rate").text
            eur_rate = eur_element.find("div", class_="currency-plate--rate").text

            # Записываем данные в CSV файл
            with open("sberbank_data.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), "Sberbank", usd_rate, eur_rate])
        else:
            print("Не удалось найти элементы с курсами валют.")

    else:
        print("Ошибка при выполнении запроса.")


# Бесконечный цикл для автоматического обновления данных каждый час
while True:
    scrape_sberbank_data()
    # Обновляем данные каждый час
    time.sleep(3600)  # 3600 секунд = 1 час
