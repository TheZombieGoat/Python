"""
File : list_merge.py
Date : 02/23/2023
"""

if __name__ == '__main__':
    list_1 = []
    list_2 = []
    merged_list = []
    i = 0
    j = 0
    list_size = int(input("How many elements do you want in each list? "))
    for x in range(list_size):
        element = input("What do you want to put in the first list? ")
        list_1.append(element)
    for y in range(list_size):
        element = input("What do you want to put in the second list? ")
        list_2.append(element)
    for z in range(list_size):
        merged_list.append(list_1[i])
        i += 1
        merged_list.append(list_2[j])
        j += 1
    print("The first list is: ",list_1)
    print("The second list is: ",list_2)
    print("The merged list is: )",merged_list)

