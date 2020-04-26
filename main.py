# Google meet bot
# By Adin Ackerman
# https://github.com/AdinAck/AdinAck/tree/master/Google%20Meet%20Bot

# Installation instructions:
#   Run 'dependencies.bat' as administrator
#   Download and install Mozilla Firefox
#   Download 'geckodriver.exe' and place in PATH directory
#       https://github.com/mozilla/geckodriver
#   Download and install Tesseract to \Tesseract\ folder in relative directory
#       Windows 64-bit: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe

import time
import pyautogui
from textdistance import hamming
import cleverbot as c
import Tesseract as t

c.open()
p = input("Parameters: ")
if "verbose" in p: verbose = True
else: verbose = False
if "safe" in p: safe = True
else: safe = False
if "control" in p: control = True
else: control = False

input("Press enter to proceed...")
time.sleep(1)

if control:
    pyautogui.moveTo(1627, 992)
    time.sleep(.5)
    pyautogui.click()
    time.sleep(.5)
    pyautogui.moveTo(1800, 124)
    pyautogui.click()
    pyautogui.moveTo(1630, 1010)
    time.sleep(.5)
    pyautogui.click()

lastCaption = ["1234abcd"]
lastChat = ["1234abcd"]
output = "1234abcd"
triggers = ["adin","aiden","hayden","ayden","aden","aidan","eden", "aid in"]
filter = ["?", "love", "kill", "sweetie", "kiss", "die", "death", "sex", "cute", "cleverbot", "fuck", "shit", "scream"]
previousSend = ""

def sendReceive(send):
    global previousSend
    print("Read:",send.lower().replace("cleverbot", ""))
    if hamming.distance(send, previousSend) >= 4:
        while True:
            try:
                receive = c.chat(send.lower().replace("cleverbot", ""))
                previousSend = receive
                print("Sending:", receive)
                for word in filter:
                    if word in receive:
                        raise Exception("Abort sending,",word,"alerted filter.")
                pyautogui.write(receive.replace("cleverbot","Adin").lower()[:-1])
                if not safe:
                    pyautogui.press('enter')
                break
            except Exception as e:
                print(e)
                print("Retrying...")
def read(x1,y1,x2,y2):
    thing = t.imToString(x1,y1,x2,y2)
    thing = [list(i) for i in thing.split("\n")]
    a = []
    for string in thing:
        for i in range(len(string)):
            if "?" in string[i] or "!" in string[i]:
                string[i] = "."
            elif string[i] == "|":
                string[i] = "I"
        string = "".join(string)
        for i in range(len(triggers)):
            string = string.lower().replace(triggers[i],"cleverbot")
        a.extend(string.split(". "))
    return a

while True:
    # Read live captions
    thing = read(68, 864, 68+1090, 997+32)
    if verbose: print("Captions:",thing)
    for caption in thing:
        if min([hamming.distance(caption,i) for i in lastCaption]) >= 4:
            if "cleverbot" in caption.lower() and "." in caption.lower():
                if caption == "cleverbot.":
                    time.sleep(4)
                    thing3 = read(68, 997, 68+1090, 997+32)
                    caption = thing3[thing2.index(caption)+1]
                sendReceive(caption)
                lastCaption.append(caption)
    if len(lastCaption) > 30:
        lastCaption.pop(0)

    # Read chat
    thing2 = read(1613, 160, 1902, 1000)
    if verbose: print("Chat:",thing2)
    for chat in thing2:
        if min([hamming.distance(chat,i) for i in lastChat]) >= 4:
            if "cleverbot" in chat.lower():
                sendReceive(chat)
                output = chat
                lastChat.append(chat)
    if len(lastChat) > 30:
        lastChat.pop(0)
c.close()
