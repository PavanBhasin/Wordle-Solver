from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re

first = second = third = fourth = fifth = "."

def letterStatus(i):
    global first, second, third, fourth, fifth
    for x in range(1,6):
        str = f'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child({i})").shadowRoot.querySelector("div > game-tile:nth-child({x})")' 
        tile = driver.execute_script(str)
        if tile.get_attribute('evaluation') == 'correct':
            correctLetters.add(tile.get_attribute('letter'))
            if x == 1:
                first = tile.get_attribute('letter')
            elif x == 2:
                second = tile.get_attribute('letter')
            elif x == 3: 
                third = tile.get_attribute('letter')
            elif x == 4:
                fourth = tile.get_attribute('letter')
            elif x == 5:
                fifth = tile.get_attribute('letter')

        elif tile.get_attribute('evaluation') == 'present':
            presentLetters.add(tile.get_attribute('letter')) 
        else:
            absentLetters.add(tile.get_attribute('letter'))

    guess = first + second + third + fourth + fifth

    return guess

#Opens browser after running code
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

#Actions allows the program to type and click the screen without specifying elements
actions = ActionChains(driver)
actions.click()
actions.send_keys('tacho\n')
actions.perform()

correctLetters = set()
presentLetters = set()
absentLetters = set()

correctWords = set()
presentWords = set()
absentWords = set()

guess = letterStatus(1)
wordList = [word for word in wordList if all(letter not in word for letter in absentLetters)]

regex = re.compile(guess)
wordList = [word for word in wordList if re.match(regex, word)]
print(wordList)
