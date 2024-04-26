from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
def inputRequiredFields():
    inputFirstName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    inputFirstName.send_keys("Ivan")
    inputLastName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    inputLastName.send_keys("Petrov")
    inputEmail = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    inputEmail.send_keys("test@test.com")


class TestAbs(unittest.TestCase):
    def test_failed(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            inputFirstName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
            inputFirstName.send_keys("Ivan")
            inputLastName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
            inputLastName.send_keys("Petrov")
            inputEmail = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
            inputEmail.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            time.sleep(1)
            browser.quit()

    def test_passed(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            inputFirstName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
            inputFirstName.send_keys("Ivan")
            inputLastName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
            inputLastName.send_keys("Petrov")
            inputEmail = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
            inputEmail.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button")
            button.click()

            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            time.sleep(1)
            browser.quit()

if __name__ == "__main__":
    unittest.main()