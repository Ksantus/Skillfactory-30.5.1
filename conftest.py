import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\selenium\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield
   pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('frubber@mail.ru')

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('klonic91')

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   time.sleep(2)

   # Нажимаем на кнопку Мои питомцы
   pytest.driver.find_element(By.CSS_SELECTOR,'button.navbar-toggler').click()
   pytest.driver.find_element(By.LINK_TEXT,'Мои питомцы').click()
   time.sleep(2)