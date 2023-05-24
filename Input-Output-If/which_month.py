"""
File : which_month.py
Date : 02/13/2023
"""

m = int(input("What month are we starting in? (Enter as an int between 1-12) "))
if m < 1 or m > 12:
    print("That is not a month within 1 and 12")
else:
    n = int(input("How many months into the future should we go? (Enter as an int) "))
    result = (m+n) % 12

    if result == 1:
        print("The month will be January.")
    elif result == 2:
        print("The month will be February.")
    elif result == 3:
        print("The month will be March.")
    elif result == 4:
        print("The month will be April.")
    elif result == 5:
        print("The month will be May.")
    elif result == 6:
        print("The month will be June.")
    elif result == 7:
        print("The month will be July.")
    elif result == 8:
        print("The result will be August.")
    elif result == 9:
        print("The result will be September.")
    elif result == 10:
        print("The result will be October.")
    elif result == 11:
        print("The result will be November.")
    else:
        print("The result will be December.")

