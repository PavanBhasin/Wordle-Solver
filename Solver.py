from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

#Opens browser after running code
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

#Actions allows the program to type and click the screen without specifying elements
actions = ActionChains(driver)
actions.click()
actions.send_keys('Guess\n')
actions.perform()

#driver.close()

#value = tile.get_attribute("evaluation")
#print(value)
#inner_texts = [my_elem.get_attribute("outerHTML") for my_elem in driver.execute_script("""return document.querySelector('game-app').shadowRoot.querySelector('game-row').shadowRoot.querySelectorAll('game-tile[letter]')""")]
#for inner_text in inner_texts:
 #   print(inner_text)

#test = [my_elem.get_attribute("outerHTML") for my_elem in driver.execute_script("""return document.querySelector('game-app').shadowRoot.querySelector('game-row').shadowRoot.querySelector('game-tile[letter]')""")]
#print(test)

#Wait for guess to register or element cannot be located
driver.implicitly_wait(10)

#Iterate through nested shadowRoots to get access to tile attributes
str = 'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(1)").shadowRoot.querySelector("div")'
elem = driver.execute_script(str)
print(elem.get_attribute("data-state"))