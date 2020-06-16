'''
Automating text input and button click on a webpage
'''

from selenium import webdriver # import selenium webdriver
browser = webdriver.Chrome() # executing Chrome webdriver

browser.get('https://techstepacademy.com/training-ground') # get desired webpage

input_element = browser.find_element_by_css_selector('input[id="ipt1"]') # select text element
input_element.send_keys('My First Automation') # pass keyboard input into text input element

button_element = browser.find_element_by_css_selector('input[name="butn1"]') # select button element
button_element.click() # click the button