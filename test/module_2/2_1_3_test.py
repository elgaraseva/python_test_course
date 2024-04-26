import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
  
link = "http://suninjuly.github.io/selects1.html"

def summ(a, b):
    return str(int(a) + int(b))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sumNum = summ(x, y)
    
    selector = f'[value="{sumNum}"]'
    print(selector)

    browser.find_element(By.CLASS_NAME, "custom-select").click()
    browser.find_element(By.CSS_SELECTOR, selector).click()

    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла