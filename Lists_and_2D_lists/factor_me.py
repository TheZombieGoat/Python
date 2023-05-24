"""
File : factor_me.py
Date : 03/02/2023
"""

if __name__ == '__main__':
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        factors = []
        num = int(input("Enter a number to factor: "))
        cond = True
        i = 0
        while cond:
                while i < 15 and cond == True:
                        if num % primes[i] == 0:
                                factors.append(primes[i])
                                num /= primes[i]
                                i = -1
                        elif num == 1:
                                print("The factors are:",end = ' ')
                                print(*factors, sep= '*')
                                cond = False
                        elif num % primes[i] != 0 and i == 14:
                                if len(factors) > 0:
                                        print("The factors are:",end =' ')
                                        print(*factors, sep= '*')
                                elif not factors:
                                        print("We didn't find any factors.")
                                print("This part of the number couldn't be factored with primes less than 50:",int(num))
                                cond = False
                        i += 1
