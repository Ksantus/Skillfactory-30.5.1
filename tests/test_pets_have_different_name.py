import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 4. У всех питомцев разные имена.

def test_all_pets_have_different_names(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   # Вычленяем имя, возраст, и породу
   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   #print(pets_name)
   # n- счетчик повторяющихся имен, если n == 0 то повторяющихся имен нет.
   n = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         n += 1
   assert n == 0
   print(n)
   print(pets_name)