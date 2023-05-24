"""
File : which_month_2.py
Date : 02/23/2023
"""

if __name__ == '__main__':

    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    start = int(input("What month are we starting in? "))
    if start < 1 or start > 12:
        print("That is not a month between 1 and 12.")
    else:
        future = int(input("How many months in the future should we go? "))
        result = (future + start) % 12
        if result == 0:
            result = 12
        print(months[result-1])
