"""
File : make_an_x.py
Date : 02/23/23
"""

if __name__ == '__main__':
    n = int(input("What is the size of the X we want to draw? "))
    if n < 3:
        print("Size needs to have a minimum value of 3.")
    else:
        start = 0
        ends = n-1
        for col in range(0,n):
            for row in range(0,n):
                if row == start and start < ends:
                    print("*",end= ' ')
                elif row == ends and start < ends:
                    print("*")
                    break
                elif row == start and start >= ends:
                    print("*")
                    break
                elif row == ends and start >= ends:
                    print("*",end= ' ')
                else:
                    print(" ",end= ' ')
            start += 1
            ends -= 1
