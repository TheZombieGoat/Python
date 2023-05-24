"""
File:         quasi_pal.py
Date:         03/10/2023
"""

EXIT_STRING = "quit"

def quasi_palindrome(word, errors):
    size = len(word)
    half_size = int(len(word)/2)
    if size % 2 == 1:
        half_size += 1
    list1 = list(word.lower())
    count = 0
    j = size-1
    for i in range(half_size):
        if list1[i] != list1[j]:
            count += 1
        j -= 1
    if count <= errors:
        return True
    return False


if __name__ == '__main__':

    word = input("What word do you want to check? ")
    errors = int(input("How many errors do you want to check? "))
    while word != EXIT_STRING:
        if quasi_palindrome(word,errors):
            print("It was a "+str(errors)+"-quasi-palindrome !")
        else:
            print("It was not a "+str(errors)+"-quasi-palindrome !")
        word = input("What word do you want to check? ")
        if word != EXIT_STRING:
            errors = int(input("How many errors do you want to check? "))
