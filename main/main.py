import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://typings.gg/")
paragrpah = driver.find_element(By.ID, "text-display")

words = (paragrpah.text.split())
inputField = driver.find_element(By.ID, "input-field")

# Calculate Words Per Min
# 50 words in 15/60 seconds = 200 WPM
# if theres 50 words total, I need to take up a total of 15 seconds.
# 15/50 = .3 so I need .3 second break between to get 200 WPS
#Average to complete without any help is about .93s. Take that and divide it by 50 and subtract that from the sleep time


def autoType(WPM): #Type up to 400 WPM automatically.
    start = time.time()
    if WPM > 400:
        print("I can only run up to 400 WPM...")
        return
    for word in words:
        # inputField.send_keys(word)
        for letter in word:
            start2 = time.time()
            inputField.send_keys(letter)
            time.sleep(.015) #Constant
            end2 = time.time()
            elapsed2 = end2-start2
            print(elapsed2)
        # time.sleep(math.calculateTime(WPM))
        inputField.send_keys(" ")
    end = time.time()
    elapsed = end-start
    print(elapsed)
autoType(100)
time.sleep(5)
driver.quit()
