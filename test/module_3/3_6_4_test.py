import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    @pytest.mark.parametrize('link', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_authorization(browser, link):
        browser.get(link)
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[href$="login"]'))
        )
        button.click()

        inputLogin = browser.find_element(By.NAME, "login")
        inputLogin.send_keys("loginUser")
        inputPassword = browser.find_element(By.NAME, "password")
        inputPassword.send_keys("passwordUser")
        buttonSubmit = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
        buttonSubmit.click()
        time.sleep(5)

        # if browser.find_element(By.CSS_SELECTOR, "textarea:disabled"):
        #    buttonAgain = browser.find_element(By.CLASS_NAME, "again-btn")
        #    buttonAgain.click()

        buttonSubmitSubmission = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission"))
        )
        inputAnswer = browser.find_element(By.CLASS_NAME, "ember-text-area")
        inputAnswer.send_keys(math.log(int(time.time())))
        time.sleep(2)
        buttonSubmitSubmission.click()

        feedBack = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
        assert feedBack == "Correct!", f"{feedBack} doesn't equal Correct!"

finally:
    time.sleep(10)