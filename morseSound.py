import os 
import time 

def makeSound(morseCode):
    for symbol in morseCode:
        if symbol == ".":
            try:
                os.system("afplay sounds/dot.mp3")
            except: 
                print("Could not play dot sound")
        elif symbol == "-":
            try:
                os.system("afplay sounds/dash.mp3")
            except: 
                print("Could not play dash sound")
        elif symbol == " ":
            time.sleep(0.18)
        elif symbol == "   ":
            time.sleep(0.42)
