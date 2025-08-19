import sys 
import time 
from pynput import mouse, keyboard
from pynput.keyboard import Key
from pynput.mouse import Button 

letter_gap=1.5


morse_text=""
last_input_time=None

def maybe_add_spacing(now:float) -> None: 
    global morse_text, last_input_time
    if last_input_time is None:
        return 
    gap=now-last_input_time
    if gap<=letter_gap:
        if morse_text.endswith(" ")==False:
            morse_text=morse_text.rstrip()+" "
    elif gap>=letter_gap:
        if morse_text.endswith("   ")==False:
            morse_text=morse_text.rstrip()+"   "

def on_click(x,y,button,pressed):
    global morse_text, last_input_time
    if pressed==False: 
        return
    now=time.time()
    maybe_add_spacing(now)
    if button==Button.left: 
        morse_text+="-"
    elif button==Button.right: 
        morse_text+="."
    last_input_time=now

def on_key_press(key):
    global morse_text, last_input_time
    now = time.time()
    if key==Key.esc:
        print('\nQuit')
        return False 
    elif key==Key.backspace:
        if morse_text:
            morse_text=morse_text[:-1]
    elif key==Key.enter:
        return False
    elif key==Key.left:
        # Left arrow key as alternative for dash
        maybe_add_spacing(now)
        morse_text+="-"
        last_input_time=now
    elif key==Key.right:
        # Right arrow key as alternative for dot
        maybe_add_spacing(now)
        morse_text+="."
        last_input_time=now 

def run_telegraph():
    global morse_text
    morse_text = ""  # Reset morse text for new session
    
    print("Morse Telegraph Rules:")
    print("Left click OR Left arrow key = dash (-)")
    print("Right click OR Right arrow key = dot (.)")
    print("- A Pause <= 1.5s creates a space between letters and a pause >= 1.5s creates a new word")
    print("- Backspace = undo last character")
    print("- Enter = submit the morse code")
    print("- ESC = quit")

    m_listener=mouse.Listener(on_click=on_click)
    k_listener=keyboard.Listener(on_press=on_key_press)
    m_listener.start()
    k_listener.start()

    # Block until Enter/Esc stops the keyboard listener
    k_listener.join()
    m_listener.stop()
    m_listener.join()
    
    return morse_text.strip()
