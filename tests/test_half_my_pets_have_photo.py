import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 2. Хотя бы у половины питомцев есть фото.


def test_half_my_pets_have_photo(go_to_my_pets):
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # В kolvo записываем количество из левой колонки статистики пользователя
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    kolvo = stat[0].text.split('\n')
    kolvo = kolvo[1].split(' ')
    kolvo = int(kolvo[1])

    # Находим половину от количества питомцев
    half = kolvo // 2

    # Находим количество питомцев с фотографией
    kolvo_with_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            kolvo_with_photos += 1
    #print(kolvo_with_photos)
    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert kolvo_with_photos >= half
