from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
  
link = "https://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    browser.switch_to.window(browser.window_handles[1])
    

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла