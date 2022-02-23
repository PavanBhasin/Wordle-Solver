import random
from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re

def evaluateLetters(i):
    
    wordGuess = random.choice(wordList)

    wordList.remove(wordGuess)

    #Actions allows the program to type and click the screen without specifying elements
    actions = ActionChains(driver)
    actions.click()
    actions.pause(4)
    actions.send_keys(wordGuess + '\n')
    actions.perform()

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

    #Combine all elements in correctLetters to be used by regex
    guess = "".join(correctLetters)
    
    #Check if Wordle was solved
    if '.' not in guess:
        return True

    modifyList(guess, absentLetters, presentLetters, correctLetters)

def modifyList(guess, absentLetters, presentLetters, correctLetters):
    global wordList
    
    wordList = [word for word in wordList if all(letter not in word for letter in absentLetters if letter not in correctLetters if letter not in presentLetters)]
    regex = re.compile(guess)
    wordList = [word for word in wordList if re.match(regex, word)]
    wordList = [word for word in wordList if all(letter in word for letter in presentLetters if letter != '.')]

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
            
#Opens browser after running code
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')

for x in range(1,7):
    flag = evaluateLetters(x)
    if flag == True:
        break
