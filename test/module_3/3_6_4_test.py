from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://stepik.org/lesson/236895/step/1"

try:
    def test_authorization(browser):
        browser.get(link)
        button = browser.find_element(By.ID, "ember457")
        button.click()

        inputLogin = browser.find_element(By.NAME, "login")
        inputLogin.send_keys("el.garaseva@gmail.com")
        inputPassword = browser.find_element(By.NAME, "password")
        inputPassword.send_keys("25sudimen395vr")
        buttonSubmit = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
        buttonSubmit.click()

        WebDriverWait(browser, 12).until(EC.invisibility_of_element(By.ID, "ember708"))
finally:
    time.sleep(30)