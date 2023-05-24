"""
File : will_it_float.py
Date : 02/13/2023
"""

object_name = input("What object are we putting in the water today? ")
weight = float(input("What is the weight of the object? "))
volume = float(input("What is the volume of the object? "))

if weight <= 0 or  volume <= 0:
    print("Value of weight or volume cannot be less than or equal to 0 !")

density = weight/volume

if density < 1000:
    print(object_name,"will float.")
elif density == 1000:
    print(object_name,"has neutral buoyancy.")
else:
    print(object_name,"will sink")

