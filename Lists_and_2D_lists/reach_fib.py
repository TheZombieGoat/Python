"""
File: reach_fib.py
Date: 02/28/2023
"""



if __name__ == '__main__':
        n = int(input("What number should we exceed? "))
        fib = 1
        fib2 = 2
        i = 3
        cond = True
        if n == 0 or n == 1:
                print("F0 = 1 which is greater than or equal to",n)
        elif n == 2:
                print("F2 = 2 which is greater than or equal to 2")
        else:
                while cond:
                        fib += fib2
                        fib2 += fib
                        if fib >= n:
                                print("F",i,"=",fib,"which is greater than or equal to",n)
                                cond = False
                        elif fib2 >= n:
                                print("F",i+1,"=",fib2,"which is greater than or equal to",n)
                                cond = False
                        i += 2
