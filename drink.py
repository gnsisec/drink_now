from Tkinter import Tk
import tkMessageBox
import time

# set timeout to 30 minutes
timer = 1800


def drink_now():
    # pop GUI will appear when the timer reaches out
    Tk().wm_withdraw()
    tkMessageBox.showinfo(title="Reminder", message="Time To Drink Now!")
    return "drink_now is running well"


if __name__ == "__main__":
    while True:
        time.sleep(timer)
        drink_now()
