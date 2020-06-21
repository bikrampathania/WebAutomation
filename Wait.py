#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:58:07 2020

@author: bikramje
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present


browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

print("I have arrived!")

WebDriverWait(browser, 10).until(alert_is_present())
# Click button on the page
print("An alert appeared!")
