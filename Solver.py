from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re

def letterStatus(i):
 
    absentLetters = ['.'] * 5
    presentLetters = ['.'] * 5
    correctLetters = ['.'] * 5

    for x in range(1,6):
        str = f'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child({i})").shadowRoot.querySelector("div > game-tile:nth-child({x})")' 
        tile = driver.execute_script(str)

        if tile.get_attribute('evaluation') == 'correct':
            correctLetters[x-1] = tile.get_attribute('letter')
        elif tile.get_attribute('evaluation') == 'present': 
            presentLetters[x-1] = tile.get_attribute('letter')
        else:
            absentLetters[x-1] = tile.get_attribute('letter')

    guess = correctLetters[0] + correctLetters[1] + correctLetters[2] + correctLetters[3] + correctLetters[4]
    
    switch = presentLetters[0] + presentLetters[1] + presentLetters[2] + presentLetters[3] + presentLetters[4]

    modifyList(guess, absentLetters, presentLetters)

def modifyList(guess, absentLetters, presentLetters):
    global wordList
    for word in wordList[:]:
        if word[0] == absentLetters[0]:
            wordList.remove(word)
        elif word[1] == absentLetters[1]:
            wordList.remove(word)
        elif word[2] == absentLetters[2]:
            wordList.remove(word)
        elif word[3] == absentLetters[3]:
            wordList.remove(word)
        elif word[4] == absentLetters[4]:
            wordList.remove(word)
    print(wordList)

    regex = re.compile(guess)
    wordList = [word for word in wordList if re.match(regex, word)]
    print(wordList)

    wordList = [word for word in wordList if all(letter in word for letter in presentLetters if letter != '.')]
    
    print(wordList)

    for word in wordList[:]:
        if word[0] == presentLetters[0]:
            wordList.remove(word)
        elif word[1] == presentLetters[1]:
            wordList.remove(word)
        elif word[2] == presentLetters[2]:
            wordList.remove(word)
        elif word[3] == presentLetters[3]:
            wordList.remove(word)
        elif word[4] == presentLetters[4]:
            wordList.remove(word)
    print(wordList)

#Opens browser after running code
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

#Actions allows the program to type and click the screen without specifying elements
actions = ActionChains(driver)
actions.click()
actions.send_keys('rates\n')
actions.perform()

correctWords = set()
presentWords = set()
absentWords = set()

letterStatus(1)
