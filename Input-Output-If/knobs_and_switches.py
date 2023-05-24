"""
File : knobs_and_switches.py
Date : 02/13/2023
"""

knob_1 = int(input("What is the position of the first knob? (Enter 1-12) "))
if knob_1 < 1 or knob_1 > 12:
    print("Knob 1 needs to be set to 1 - 12")
knob_2 = int(input("What is the position of the second knob? (Enter 1-12) "))
if knob_2 < 1 or knob_2 > 12:
    print("Knob 2 needs to be set to 1 - 12")

switch_pos = input("What is the position of the switch? (Enter up or down) ")
if switch_pos.lower() != "up" and switch_pos.lower() != "down":
    print("Switch position needs to be set either up or down.")
else:
    if knob_1 % 2 == 0 and knob_2 % 2 == 1 and switch_pos.lower() == "up":
        print("The door opens, you get all the loot.")
    elif switch_pos.lower() == "down":
        if knob_1 % 2 == 1 and knob_2 % 2 == 1:
            print("The door clanks but does not open, try again.")
        elif knob_1 % 2 == 0 and knob_2 % 2 == 0:
            print("The door clanks but does not open, try again.")
        else:
            print("The handle doesn't budge.")

