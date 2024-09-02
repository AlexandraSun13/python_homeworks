from selenium import webdriver
from time import sleep 
chrome = webdriver.Chrome()

chrome.get('http://uitestingplayground.com/dynamicid')
blue_button = chrome.find_element(
    "xpath", '//button[text()="Button with Dynamic ID"]').click()
sleep(5)
chrome.quit()


