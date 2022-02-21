from Wordlist import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re

firstC = firstP = firstA = secondC = secondP = secondA = thirdC = thirdP = thirdA = fourthC = fourthP = fourthA = fifthC = fifthP = fifthA = "."
absentLetters = set()
presentLetters = set()

def letterStatus(i):
    global firstC, firstP, firstA, secondC, secondP, secondA, thirdC, thirdP, thirdA, fourthC, fourthP, fourthA, fifthC, fifthP, fifthA, absentLetters, presentLetters
    for x in range(1,6):
        str = f'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child({i})").shadowRoot.querySelector("div > game-tile:nth-child({x})")' 
        tile = driver.execute_script(str)
        if tile.get_attribute('evaluation') == 'correct':
            if x == 1:
                firstC = tile.get_attribute('letter')
            elif x == 2:
                secondC = tile.get_attribute('letter')
            elif x == 3: 
                thirdC = tile.get_attribute('letter')
            elif x == 4:
                fourthC = tile.get_attribute('letter')
            elif x == 5:
                fifthC = tile.get_attribute('letter')

        elif tile.get_attribute('evaluation') == 'present': 
            presentLetters.add(tile.get_attribute('letter'))
            if x == 1:
                firstP = tile.get_attribute('letter')
            elif x == 2:
                secondP = tile.get_attribute('letter')
            elif x == 3: 
                thirdP = tile.get_attribute('letter')
            elif x == 4:
                fourthP = tile.get_attribute('letter')
            elif x == 5:
                fifthP = tile.get_attribute('letter')
        else:
            absentLetters.add(tile.get_attribute('letter'))
            if x == 1:
                firstA = tile.get_attribute('letter')
            elif x == 2:
                secondA = tile.get_attribute('letter')
            elif x == 3: 
                thirdA = tile.get_attribute('letter')
            elif x == 4:
                fourthA = tile.get_attribute('letter')
            elif x == 5:
                fifthA = tile.get_attribute('letter')

    guess = firstC + secondC + thirdC + fourthC + fifthC
    switch = firstP + secondP + thirdP + fourthP + fifthP

    return guess, switch, absentLetters, presentLetters

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

guess, switch, absentLetters, presentLetters = letterStatus(1)

#wordList = [word for word in wordList if all(letter not in word for letter in absentLetters)]

for word in wordList[:]:
    if word[0] == firstA:
        wordList.remove(word)
    elif word[1] == secondA:
        wordList.remove(word)
    elif word[2] == thirdA:
        wordList.remove(word)
    elif word[3] == fourthA:
        wordList.remove(word)
    elif word[4] == fifthA:
        wordList.remove(word)

regex = re.compile(guess)
wordList = [word for word in wordList if re.match(regex, word)]

wordList = [word for word in wordList if all(letter in word for letter in presentLetters)]

reg = re.compile(switch)

for word in wordList[:]:
    if word[0] == firstP:
        wordList.remove(word)
    elif word[1] == secondP:
        wordList.remove(word)
    elif word[2] == thirdP:
        wordList.remove(word)
    elif word[3] == fourthP:
        wordList.remove(word)
    elif word[4] == fifthP:
        wordList.remove(word)

thirdP = '.'
actions.pause(4)
actions.send_keys('treed\n')
actions.perform()

guess, switch, absentLetters, presentLetters = letterStatus(2)

for word in wordList[:]:
    if word[0] == firstA:
        wordList.remove(word)
    elif word[1] == secondA:
        wordList.remove(word)
    elif word[2] == thirdA:
        wordList.remove(word)
    elif word[3] == fourthA:
        wordList.remove(word)
    elif word[4] == fifthA:
        wordList.remove(word)

regex = re.compile(guess)
wordList = [word for word in wordList if re.match(regex, word)]

wordList = [word for word in wordList if all(letter in word for letter in presentLetters)]

reg = re.compile(switch)

for word in wordList[:]:
    if word[0] == firstP:
        wordList.remove(word)
    elif word[1] == secondP:
        wordList.remove(word)
    elif word[2] == thirdP:
        wordList.remove(word)
    elif word[3] == fourthP:
        wordList.remove(word)
    elif word[4] == fifthP:
        wordList.remove(word)
print(wordList)
