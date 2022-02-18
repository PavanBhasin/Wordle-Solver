from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

actions = ActionChains(driver)
actions.click()
actions.send_keys('Guess\n')
actions.perform()

driver.close()


