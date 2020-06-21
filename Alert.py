#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:42:01 2020

@author: bikramje
"""

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

button1 = browser.find_element_by_css_selector("button[id='b1']")
button1.click()

alert = Alert(browser)
if alert.text == 'You clickedButton1.':
    print(alert.text)
alert.accept()