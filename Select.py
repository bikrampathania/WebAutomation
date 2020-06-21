#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:43:27 2020

@author: bikramje
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select

browser =  webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

sel = browser.find_element_by_id("sel1")
my_select = Select(sel)

print([elem.text for elem in my_select.options])

# below will select BG in the drop-down. Don't use if localization is there
my_select.select_by_visible_text('Battlestar Galactica')

# below can be used for the same purpose if localization is there
my_select.select_by_index(0) # selects Bears

# select by value below; selects Beets
my_select.select_by_value('second')

# gets first selected item in the drop down
print(my_select.first_selected_option.text)