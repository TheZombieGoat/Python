"""
FILE : leap_year.py
DATE : 02/13/2023
"""

year = int(input("Enter a year: "))

if year%4 != 0:
    print("It is not a leap year.")
elif year%100 == 0 and year%400 != 0:
    print("It is not a leap year")
else:
    print("It is a leap year")
