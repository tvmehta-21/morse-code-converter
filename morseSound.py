import os 
import time 

def makeSound(morseCode, speed=2.0):
    """
    Play morse code sounds with adjustable speed.
    
    Args:
        morseCode (str): The morse code string to play
        speed (float): Speed multiplier (1.0 = normal, 2.0 = 2x faster, 0.5 = 2x slower)
    """
    # Base timing values
    letter_gap = 0.18 / speed
    word_gap = 0.42 / speed
    
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
            time.sleep(letter_gap)
        elif symbol == "   ":
            time.sleep(word_gap) 
