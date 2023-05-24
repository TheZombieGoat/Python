"""
File: geom_average.py
Date: 02/09/2023
 """

first_num = float(input("Tell me the first number: "))
sec_num  = float(input("Tell me the second number: "))
third_num = float(input("Tell me the third number: "))
fourth_num = float(input("Tell me the fourth number: "))
fifth_num = float(input("Tell me the fifth number: "))
sixth_num = float(input("Tell me the sixth number: "))
result = (first_num * sec_num * third_num * fourth_num * fifth_num * sixth_num)**(1/6)

print("The geometric average is",result)
