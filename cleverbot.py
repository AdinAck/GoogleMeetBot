# GoogleMeetBot
# By Adin Ackerman
# Cleverbot interface library

import cleverbotfree.cbfree
import sys
print("Initializing...")
cb = cleverbotfree.cbfree.Cleverbot()

def open():
    print("Establishing connection with Cleverbot...")
    try:
        cb.browser.get(cb.url)
        print("Done.")
    except:
        print("Failed, closing.")
        cb.browser.close()
        sys.exit()

def chat(userInput):
    try:
        cb.get_form()
    except:
        sys.exit()
    cb.send_input(userInput)
    bot = cb.get_response()
    a = []
    p = 0
    return bot

def close():
    cb.browser.close()
