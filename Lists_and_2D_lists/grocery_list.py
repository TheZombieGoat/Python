"""
File : grocery_list.py
Date : 02/28/2023
"""

if __name__ == '__main__':

    required_items = ["eggs","bread","butter","milk"]
    grocery_list = []
    condition = True
    while condition:
        item = input("What do you pick up in the store? (quit to exit) ")
        if item.lower() == "quit":
            condition = False
        elif item.lower() == "eggs":
            required_items.remove("eggs")
        elif item.lower() == "bread":
            required_items.remove("bread")
        elif item.lower() == "butter":
            required_items.remove("butter")
        elif item.lower() == "milk":
            required_items.remove("milk")
        if item.lower() != "quit":
            grocery_list.append(item.lower())
    if not required_items:
        print("\nYou got everything you needed !!!")
        print("You bought",*grocery_list, sep = ',')
    else:
        print("\nYou still need",*required_items, sep = ',')
        print("You bought",*grocery_list, sep = ',')

