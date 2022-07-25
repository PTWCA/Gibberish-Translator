# Copy selected text
# Clean it
# Paste it
import pyperclip
import time
from pynput.keyboard import Key, Controller
from convert import convert_gb
import pyautogui


def manage_clipboard(cmd:str):
    pyperclip.copy('')
    keyboard = Controller()
    
    keyboard.press(Key.ctrl.value)
    keyboard.press(cmd)
    keyboard.release(cmd)
    keyboard.release(Key.ctrl.value)
    
    time.sleep(0.1)
    return pyperclip.paste()
	
gibberish_text = manage_clipboard('c')
clean_text = convert_gb(gibberish_text)
copied_clean_text = pyperclip.copy(clean_text)
pyautogui.hotkey('ctrl','v')