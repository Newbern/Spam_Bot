import pyautogui as pink
from time import sleep
import os

# Repeats the Program
def Spam(txt, rep, tim):
    sleep(tim)
    for _ in range(rep):
        pink.write(txt)
        sleep(0.2)
        pink.press('Enter')

# Loop
while True:
    # Text to be input
    text = input("What would you like to say?: ")

    # How many times you want to spam
    repeat = int(input("How Many times would you like to Repeat this?: "))

    # Seconds needed before Spamming begins
    time = int(input("How long of duration?: "))

    Spam(text, repeat, time)

    # Clears screen
    os.system('cls')
