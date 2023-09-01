from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    sub = browser.find_element(By.CSS_SELECTOR, "div > [type =submit]")
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.execute_script("return arguments[0].scrollIntoView(true);", sub)
    result = str((math.log(abs(12*math.sin(x)))))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)
    sub.click()
finally:
    time.sleep(60)
    browser.quit()