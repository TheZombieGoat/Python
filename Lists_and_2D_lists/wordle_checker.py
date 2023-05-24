"""
File : wordle_checker.py
Date : 02/21/23
"""

if __name__ == '__main__':

     solution = input("Enter the solution word: ")
     guess = input("Enter the guess word: ")
     if len(guess) != len(solution) or len(guess) != 5:
          print("Character length does not match.")
     else:
         word = ["_","_","_","_","_"]
         for x in range(5):
              for y in range(5):
                   if x == y and guess[x] == solution[y]:
                        word[x] = "g"
                        break
                   elif guess[x] == solution[y]:
                        word[x] = "y"
                        break
                   elif guess[x] != solution[y]:
                        word[x] = "_"
         print(word)
