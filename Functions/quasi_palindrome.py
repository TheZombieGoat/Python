"""
File:         quasi_pal.py
Date:         03/10/2023
"""

EXIT_STRING = "quit"

def quasi_palindrome(word, errors):
    count = 0
    i = 0
    word = word.lower()
    while i < len(word) // 2:
        if word[i] != word[-(i+1)]:
            count += 1
        i += 1
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
