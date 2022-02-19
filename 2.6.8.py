from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_field = browser.find_element_by_name("firstname")
    name_field.send_keys("Name")

    surname_field = browser.find_element_by_name("lastname")
    surname_field.send_keys("Lastname")

    email_field = browser.find_element_by_name("email")
    email_field.send_keys("email@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_css_selector("input#file")
    element.send_keys(file_path)
    
    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()

finally:
    time.sleep(4)
    browser.quit()


