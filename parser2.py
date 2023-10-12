from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Инициализируем веб-драйвер (предполагается, что у вас установлен ChromeDriver)
driver = webdriver.Chrome()

# Открываем страницу с данными MICEX
driver.get("https://www.finam.ru/profile/mirovye-indeksy/micex/export/")

# Ждем немного, чтобы страница загрузилась
time.sleep(3)

# Выбираем период "5 лет"
period_select = Select(driver.find_element(By.ID, "issuer-profile-interval"))
period_select.select_by_value("5y")

# Жмем кнопку "Скачать"
download_button = driver.find_element(By.ID, "issuer-profile-export")
download_button.click()

# Ждем немного, чтобы файл загрузился
# time.sleep(20)

# Закрываем веб-драйвер
# driver.quit()
