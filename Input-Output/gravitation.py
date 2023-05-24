"""
File: Gravitation.py
Date: 02/09/2023
"""

G = float(6.6743 * 10 ** (-11))
print("Enter the following numbers in a scientific notation where the \nfirst input is the number and the second is the power for the scientific notation")

m1 = float(input("Enter the mass of the first object(without exponent): "))
expo1 =  float(input("Enter the exponent of the first object's mass: "))
W1 = float(m1 * 10 ** (expo1))
m2 = float(input("Enter the mass of the second object(without exponent): "))
expo2 = float(input("Enter the exponent of the second object's mass: "))
W2 = float(m2 * 10 ** (expo2))
distance = float(input("What is the distance between the two objects (without exponent)? "))

distance_expo = float(input("Enter the exponent of the distance: "))
dist_res = float(distance * 10 ** (distance_expo))
result = (G * W1 * W2)/(dist_res**2)


print("The distance between these objects is ",result)
