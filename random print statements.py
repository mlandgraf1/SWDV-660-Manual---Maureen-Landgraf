from random import random

number = random()

if number < 0.35:
    print("Time for the Stanley Cup Finals!")
elif number > 0.65:
    print("Let's go Blues!")
elif number < 0.65 and number > 0.35:
    print("Win the Stanley Cup!")
