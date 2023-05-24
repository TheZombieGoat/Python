"""
File : Py_coin.py
Date : 02/09/2023
"""

py_coin_value = float(input("How many dollars is a py-coin now? "))
item_name = input("What item do you want to convert to py-coins? ")
conversion_rate = float(input("How many dollars is the item you want to buy? "))
conversion_result = conversion_rate/py_coin_value

print("The value of a ",item_name," in pycoins is ",conversion_result)

