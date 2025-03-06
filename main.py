import tkinter as tk
import pyautogui
import sys
import threading
import keyboard



global hotkey
hotkey = "ctrl+q"

def clicks_get():
    global clicksAmount
    clicksAmount = clicksAmount_var.get()
    print(clicksAmount)

def toggleON():
    pyautogui.click(clicks=clicksAmount)

def listen_hotkey():
    keyboard.wait(hotkey)
    # clicks_get()
    toggleON()
    listen_hotkey()



root = tk.Tk()
root.title("EzClick")
root.geometry("500x500")
root.resizable(width=False, height=False)

clicksAmount_var = tk.IntVar()


enterClicks_Label = tk.Label(root,text="Enter amount of clicks").pack()
enterClicks_Entry = tk.Entry(root, textvariable=clicksAmount_var).pack()
enterClicks_Submit = tk.Button(root,text="Submit", command=clicks_get).pack()

enterHotkey_Label = tk.Label(root, text=f"Your hotkey is: {hotkey} ").pack()


exitButton = tk.Button(root, text="Exit", command=sys.exit).pack()

thread = threading.Thread(target=listen_hotkey, daemon=True)
thread.start()

root.mainloop()