from WordleSolver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

#Opens browser after running code
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

#Actions allows the program to type and click the screen without specifying elements
actions = ActionChains(driver)
actions.click()
actions.send_keys('sucks\n')
actions.perform()

#print(driver.find_element_by_css_selector('game-app::shadow, game-theme-manager'))
#test = 'game-app::shadow game-theme-manager::shadow game-row::shadow game-tile'
#test.get_attribute('evaluation')

#Iterate through nested shadowRoots to get access to tile attributes
str = 'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(1)")'
elem = driver.execute_script(str)
print(elem.get_attribute('evaluation'))