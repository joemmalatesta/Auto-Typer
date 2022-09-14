import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://typings.gg/")
# paragrpah = driver.find_element(By.ID, "text-display")

# words = (paragrpah.text.split())
# inputField = driver.find_element(By.ID, "input-field")


redo = driver.find_element(By.ID, "redo-button")



# Calculate Words Per Min
# 50 words in 15/60 seconds = 200 WPM
# if theres 50 words total, I need to take up a total of 15 seconds.
# 15/50 = .3 so I need .3 second break between to get 200 WPS
#Average to complete without any help is about .93s. Take that and divide it by 50 and subtract that from the sleep time

def autoType(WPM, typingTime = 0): #Type up to 400 WPM automatically.
    totalCharacters = 0


    paragrpah = driver.find_element(By.ID, "text-display")
    words = (paragrpah.text.split())
    inputField = driver.find_element(By.ID, "input-field")


    start = time.time()
    for word in words:
        for letter in word:
            inputField.send_keys(letter)
            totalCharacters += 1
            letterSleep = .015
            if typingTime != 0:
                letterSleep = typingTime - .015
            time.sleep(letterSleep)

        # time.sleep(math.calculateTime(WPM))
        inputField.send_keys(" ")
        totalCharacters += 1
    end = time.time()
    elapsed = end-start
    totalCharacters -= 1 #Last space is not required.
    timePerCharacter = elapsed/totalCharacters

    #Add elapsed, total characters, and time per character
    with open('timesheet.txt', 'a') as f:
        f.write(f'''Elapsed: {elapsed}
    Total Characters: {totalCharacters}
    Time Per Character: {timePerCharacter}
    ''')


    rightWing = driver.find_element(By.ID, "right-wing")
    results = rightWing.text.split()
    resultWPM = results[1]
    print(resultWPM)
    return timePerCharacter


typingTime = autoType(100) #First one calibrates how long each character takes.
redo.click()
autoType(100, typingTime)
#Turns out there is still a huge disparity of character typed per second, at least on my laptop.
time.sleep(5)
driver.quit()
