from Tkinter import Tk
import tkMessageBox
import time
from random import randint

# set timeout to 30 minutes
timer = 1800

alert_message = [
    "No water, no life. No blue, no green.",
    "Water is the driving force of all nature.",
    "If there is magic on this planet, it is contained in water.",
    "Drinking water is essential to a healthy lifestyle.",
    "The sound of water is worth more than all the poets' words.",
    "Water, taken in moderation, cannot hurt anybody."
]


def drink_now():
    # pop GUI will appear when the timer reaches out
    random_msg = alert_message[
        randint(0, len(alert_message)-1)]

    Tk().wm_withdraw()
    tkMessageBox.showinfo(
        title="Reminder",
        message=random_msg + "\n\nTake a Water and Drink now")

    return "drink_now is running well"


if __name__ == "__main__":
    while True:
        time.sleep(timer)
        drink_now()
