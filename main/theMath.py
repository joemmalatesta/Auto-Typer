#Okay im splitting up the math portion here so It don't get so confusing...
#For this, I will always be using 50 words, but it should be able to transfer no matter how many words there are.
#  50 words /  (X/60) = WPM
#  3000 / X = WPM
# if WPM = 200, then 3000/X = 200 and X would be the seconds it's supposed to take



#Since adding time between each letter input, you can see that each character matters a lot towards the timing
#Need to figure out how much time I need for each Character.
#Time to type each character is about .0095 without any pause.

#200 wpm is .3 seconds pause - .0095 is good .015 pause per letter too



def calculateTime(WPM):
    wordsPerSecond = WPM / 60
    wordWaitTime = 1 / wordsPerSecond
    print(f"current wait time: {wordWaitTime}")
    return wordWaitTime
    #you can use (wordWaitTime / letterCount) - timePerCharacter