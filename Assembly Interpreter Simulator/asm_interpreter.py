"""
File name : asm_interpreter.py
Date : 04/14/2023 
"""
ram = []
program_memory = []
bool_list = [0,0] #first index is equal flag. second index is less than flag.
command_list = ["add","mul","sub","div","mod","mov","nop","ADD","SUB","MUL","DIV","MOD","MOV","NOP"]
conditional_command_list = ["jl","jg","jge","je","jle","jne","JL","JG","JGE","JE","JLE","JNE","jmp","JMP"]
EXIT = False

def init_ram(RAM_size):
        for _ in range(RAM_size):
                ram.append(0)

def my_any(l1,l2):
        if len(l2) > 1:
                for i in range(len(l1)):
                        if l1[i] == l2[0]:
                                return True
        return False

def extract(word):
        a = list(word)
        a.remove("[")
        a.remove("]")
        b = "".join(a)
        return int(b)

def compare(instructions,bools):        #A value of 1 means true while a value of 0 means false.
        if "[" in instructions[1]:
                v1 = ram[extract(instructions[1])]
        else:
                v1 = int(instructions[1])

        if "[" in instructions[2]:
                v2 = ram[extract(instructions[2])]
        else:
                v2 = int(instructions[2])

        if v1 < v2:
                bools = [0,1]
        elif v1 == v2:
                bools = [1,0]
        elif v1 > v2:
                bools = [0,0]

        return bools

def interrupt_commands(instructions):
        word = instructions[1].lower()
        new_arr = instructions
        if "[" in instructions[2]:
                value = extract(instructions[2])
        else:
                value = instructions[2]
        size = len(instructions)

        if word == "input":
                ask = int(input(">> "))
                ram[value] = ask
        elif word == "print":
                if "[" in instructions[2]:
                        print(ram[value])
                else:
                        new_arr.pop(0)
                        new_arr.pop(0)
                        print(*new_arr)

def basic_commands(instructions):
        word = instructions[0].lower()
        mov_bool = False
        if "[" in instructions[1]:
                destination = extract(instructions[1])
        else:
                destination = int(instructions[1])

        if "[" in instructions[2]:
                value_1 = ram[extract(instructions[2])]
                mov_bool = True
        else:
                value_1 = int(instructions[2])

        if len(instructions) > 3:
                if "[" in instructions[3]:
                        value_2 = ram[extract(instructions[3])]
                else:
                        value_2 = int(instructions[3])

        if word == "add":
                ram[destination] = value_1 + value_2
        elif word == "sub":
                ram[destination] = value_1 - value_2
        elif word == "mul":
                ram[destination] = value_1 * value_2
        elif word == "div":
                if value_2 != 0 or value_1 != 0:
                        ram[destination] = value_1 // value_2
                else:
                        print("Zero error")
        elif word == "mod":
                ram[destination] = value_1 % value_2
        elif word == "mov":
                if mov_bool:
                        ram[destination] = value_1
                else:
                        ram[destination] = value_1
        elif word == "nop":
                return

def conditional_command(instructions,index,bools):
        word = instructions[0].lower()
        if "[" in instructions:
                value = ram[extract(instructions[1])]
        else:
                value = int(instructions[1])

        if word == "jl" or word == "jle":
                if bools[1] == 1:
                        index = value
                else:
                        index = index + 1
        elif word == "je" or word == "jge" or word == "jle":
                if bools[0] == 1:
                        index = value
                else:
                        index = index + 1
        elif word == "jg" or word == "jge":
                if bools[0] == 0 and bools[1] == 0:
                        index = value
                else:
                        index = index + 1
        elif word == "jne":
                if bools[0] == 0:
                        index = value
                else:
                        index = index + 1
        elif word == "jmp":
                index = value
        return index

if __name__ == "__main__":
        req = input("What file do you want to assemble, and what size of RAM should we use ? ")
        f_name = req.split()[0]
        init_ram(int(req.split()[1]))
        file = open(f_name,"r")
        file_line = 1
        i = 0
        while file_line:
                file_line = file.readline()
                program_memory.append(file_line)

        while (i < len(program_memory) and EXIT == False):
                line = program_memory[i]
                line = line.split()
                if my_any(command_list,line):
                        basic_commands(line)
                        i = i+1
                elif "int" in line or "INT" in line:
                        interrupt_commands(line)
                        i = i+1
                elif "cmp" in line or "CMP" in line:
                        bool_list = compare(line,bool_list)
                        i = i+1
                elif my_any(conditional_command_list,line):
                        i = conditional_command(line,i,bool_list)
                elif "hlt" in line or "HLT" in line:
                        EXIT = True
        file.close()
