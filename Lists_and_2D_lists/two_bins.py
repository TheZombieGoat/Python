"""
File : two_bins.py
Date : 03/02/2023
"""

if __name__ == '__main__':
        A = []
        B = []
        cond = True
        while cond:
                string = input()
                if string == "quit":
                        cond = False
                else:
                        command = string.split()
                        if command[1] == "A":
                                if command[0].lower() == "display":
                                        print("Bin A Contents:",end = ' ')
                                        print(*A, sep = ',')
                                elif command[0].lower() == "add":
                                        A.append(command[2])
                                elif command[0] == "remove":
                                        if command[2] in A:
                                                A.remove(command[2])
                                        else:
                                                print(command[2],"does not exist in Bin A")
                                elif command[0].lower() == "transfer":
                                        if not A:
                                                print("Bin A is empty. Transfer cannot be executed.")
                                        else:
                                                B.append(A[0])
                                                A.pop(0)
                        elif command[1] == "B":
                                if command[0].lower() == "display":
                                        print("Bin B Contents:",end = ' ')
                                        print(*B, sep = ',')
                                elif command[0].lower() == "add":
                                        B.append(command[2])
                                elif command[0] == "remove":
                                        if command[2] in B:
                                                B.remove(command[2])
                                        else:
                                                print(command[2],"does not exist in Bin B")
                                elif command[0].lower() == "transfer":
                                        if not B:
                                                print("Bin B is empty. Transfer cannot be executed.")
                                        else:
                                                A.append(B[0])
                                                B.pop(0)
