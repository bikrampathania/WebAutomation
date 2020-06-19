#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:36:37 2020

@author: bikramje
"""

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
button4_xp_locator = "//button[@id='b4']"

# assign elements
input2_elem = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button4_xp_locator)

# manipulate elements
input2_elem.send_keys("Test text")
butn4_elem.click()

browser.quit()