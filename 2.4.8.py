from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    book_button = browser.find_element_by_id("book")
    value = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button.click()

    x = browser.find_element_by_id("input_value")
    x_text = x.text
    y = calc(x_text)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


    