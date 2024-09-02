from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
chrome = webdriver.Chrome()

chrome.get('http://uitestingplayground.com/classattr')
blue_button = chrome.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button.click()
sleep(5)
chrome.switch_to.alert.accept()
chrome.quit()

