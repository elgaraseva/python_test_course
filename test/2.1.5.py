import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "#input_value").text
    x = x_element.text
    y = calc(x)

    link = browser.find_element(By.LINK_TEXT, text)
    link.click()
    
    input1 = browser.find_element(By.ID, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value=robots]")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла