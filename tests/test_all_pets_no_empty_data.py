import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_have_full_data(go_to_my_pets):
    # Ввводим неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('frubber@mail.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('klonic91')

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = pytest.driver.find_elements(By.CLASS_NAME ,'card-img-top')
    names = pytest.driver.find_elements(By.CLASS_NAME ,'card-title')
    descriptions = pytest.driver.find_elements(By.CLASS_NAME ,'card-text')

    for i in range(len(names)):
        print('names', names[i].text)
        print('descriptions', descriptions[i].text)
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0