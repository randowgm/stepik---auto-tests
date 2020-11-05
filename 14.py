from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код
    
    # говорим Selenium проверять в течение 12 секунд
    
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    
    
    #ищем и решаем
    
    element1 = browser.find_element_by_css_selector("#input_value")
    x_element = element1.text
    print("value: ", x_element)
    x = x_element
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    
    
    # ок
    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()
    



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()