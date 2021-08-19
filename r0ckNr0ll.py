#r0ckNr0ll.py

import pyautogui
import time
from pyfiglet import Figlet

fnt = Figlet(font="thin")
print (fnt.renderText("r0ck'N'r0ll"))
time.sleep(3)

txt = input("What would you like to spam? ")


tmes = input("How many times do you want it to spam?: ")



rdy = input("Are you ready to r0ck'N'r0ll? (y/n, default=n): ")

if rdy == ("y"):
    print("r0ckin'N'r0lling!")
    print("***(Make sure your cursor is in the right text input. YOU HAVE 10 SECONDS!)***")

else:
    print("Quitting... Come back When you're ready!")
    time.sleep(3)
    quit()

time.sleep(10)
for i in range(int(tmes)):
    pyautogui.typewrite(txt)
    pyautogui.press("enter")
