import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 1. Присутствуют все питомцы.

def test_all_my_pets(go_to_my_pets):
    #Вводим явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # В pets записываем элементы карточек питомцев из таблицы
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    print(len(pets))

    # В kolvo записываем количество из левой колонки статистики пользователя
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')
    print(stat[0].text)
    kolvo = stat[0].text.split('\n')
    print(kolvo)
    kolvo = kolvo[1].split(': ')
    print(kolvo)
    kolvo = int(kolvo[1])

    #print(kolvo)
    #print(len(pets))
    #Проверяем, что количество в статистике совпадает с количеством питомцев в таблице
    assert kolvo == len(pets)
