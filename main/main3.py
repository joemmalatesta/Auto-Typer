import time
import letterTimeMath

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Initalize Selenium and static properties
expectedWPM = int(input("How fast do you want to type?"))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://typings.gg/")
redo = driver.find_element(By.ID, "redo-button")
inputField = driver.find_element(By.ID, "input-field")


def restart():
    redo.click()
    paragrpah = driver.find_element(By.ID, "text-display")
    words = (paragrpah.text.split())
    return words

def countCharacters():
    words = restart()
    totalCharacters = 0
    for word in words:
        for letter in word:
            totalCharacters += 1
        inputField.send_keys(" ")
        totalCharacters += 1
    return totalCharacters


def autoType():
    paragrpah = driver.find_element(By.ID, "text-display")
    words = (paragrpah.text.split())
    totalCharacters = countCharacters()
    
    letterTimeMath.calculateTime(totalCharacters)
    start = time.time()
    for word in words:
        for letter in word:
            inputField.send_keys(letter)
            time.sleep(letterSleep)
        inputField.send_keys(" ")
    end = time.time()
    #End bot, end timer.


    #Math for time per character and retreiving WPM.
    elapsed = end-start
    totalCharacters -= 1 #Last space is not required.
    timePerCharacter = elapsed/totalCharacters
    rightWing = driver.find_element(By.ID, "right-wing")
    results = rightWing.text.split()
    resultWPM = results[1]



    #Add elapsed, total characters, and time per character
    writeToMethod = 'w'
    if timesRan != 0:
        writeToMethod == 'a'
    with open('timesheet.txt', writeToMethod) as f:
        f.write(f'''Elapsed: {elapsed}
    Total Characters: {totalCharacters}
    Time Per Character: {timePerCharacter}
    Current WPM : {resultWPM}
    ''')

    timesRan += 1
    return int(resultWPM)




