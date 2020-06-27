#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:37:12 2020

@author: bikramje
"""

from selenium import webdriver

from pages.POM_TrainingGroundPage_2 import TrainingGroundPage


# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
trng_page.button1.click()