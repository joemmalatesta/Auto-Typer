
import time
from unittest import result
import theMath
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
timesRan = 0


def autoType(wordSleep = 0):
    #Initalize test, specific properties.
    paragrpah = driver.find_element(By.ID, "text-display")
    words = (paragrpah.text.split())



    #Begin bot, start timer
    start = time.time()
    for word in words:
        inputField.send_keys(word)
        # for letter in word:
        #     inputField.send_keys(letter)
        #     time.sleep(.015 - letterSleep)
        # time.sleep(wordSleep - (.015*len(word)))
        inputField.send_keys(" ")
        time.sleep(wordSleep)
    end = time.time()
    #End bot, end timer.


    #Math for time per character and retreiving WPM.
    elapsed = end-start
    timePerWord = elapsed/50
    rightWing = driver.find_element(By.ID, "right-wing")
    results = rightWing.text.split()
    resultWPM = results[1]



    #Add elapsed, total characters, and time per character
    writeToMethod = 'w'
    if timesRan != 0:
        writeToMethod = 'a'
    with open('timesheet.txt', writeToMethod) as f:
        f.write(f'''Elapsed: {elapsed}
    Words: 50
    Time Per Word: {timePerWord}
    Current WPM : {resultWPM}
    Run # : {timesRan}
    ''')


    return int(resultWPM), timePerWord



#Calibrate
rawTimePerWord = autoType()[1]
redo.click()
# Inital Run
wordSleep = theMath.calculateTime(expectedWPM)
wordSleep -= rawTimePerWord
resultWPM = autoType(wordSleep)[0]

#Run until you get it right
while resultWPM != expectedWPM:
    timesRan += 1
    redo.click()
    if resultWPM > expectedWPM:
        wordSleep *= 1.0001
    elif resultWPM < expectedWPM:
        wordSleep /= 1.0001
    print(resultWPM, expectedWPM, wordSleep)
    resultWPM = autoType(wordSleep)[0]

time.sleep(5)
print(f"holy hell, it worked. it took you {timesRan} runs to calibrate your stinky machine. The wait time between each word was {wordSleep}.")