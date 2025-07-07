import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 3. У всех питомцев есть имя, возраст и порода.

def test_all_pets_have_full_data(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   # Проверяем, что у всех питомцев есть имя, возраст и порода
   for i in range(len(pet_data)):
      pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_pet = pet.split(' ')
      result = len(split_pet)
      assert result == 3















