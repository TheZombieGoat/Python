"""
File : find_a_plus.py
Date : 03/08/2023
"""


import random

def generate_grid(m, n, seed = 0):
   if seed:
      random.seed(seed)
   return [[random.choice(['.', '*']) for _ in range(n)] for _ in range(m)]

def display_grid(the_grid):
   for row in the_grid:
      print(' '.join(row))

def is_plus_there(the_grid):
   x = len(the_grid[0])
   y = len(the_grid)
   for col in range(1,x-1):
      for row in range(1,y-1):
         if the_grid[row][col] == "*":
            if the_grid[row+1][col] == "*" and the_grid[row][col+1] == "*" and the_grid[row][col-1] == "*" and the_grid[row-1][col] == "*":
               return True
   return False

if __name__ == '__main__':
   numbers = input('Enter the dimensions (and optionally the seed): ').split()
   x = int(numbers[0])
   y = int(numbers[1])
   the_seed = int(numbers[2])
   a_grid = generate_grid(x, y, the_seed)
   display_grid(a_grid)
   print(is_plus_there(a_grid) is not False)

