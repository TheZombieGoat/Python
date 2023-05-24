"""
File : slice_of_pi.py
Date : 02/21/23
"""

if __name__ == '__main__':
    l = int(input("Enter a positive integer L: "))
    if l <= 0:
        print("That is not a positive integer.")
    else:
        result = 0
        for n in range(l+1):
            formula = ((-1)**n)/(2*n + 1)
            result += formula
        print("The sum up to L =",l,"of the Leibniz formula is:\n",result)
        print("This gives our approximation of pi as",result*4)
