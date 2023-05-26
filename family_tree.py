"""
File : family_tree.py
Date : 05/5/2023
"""

#creating constants
NAME = "NAME"
MOTHER = "MOTHER"
FATHER = "FATHER"
CHILDREN = "CHILDREN"
NONE = "None-Listed"
EXIT = "exit"

"""creates person node. takes a dictionary and string as parameters. (data = name) """
def create_person(tree,data):
	if data in tree:
		print("Person already exists.")
	else:
		new_person = {NAME: data, MOTHER: NONE, FATHER: NONE, CHILDREN: []}
		tree[data] = new_person
		print(data,"has been created.")

"""takes dict parameter and three string parameters and sets parent of person. Example for setting mother = set_parent(dict_name,person_name,parent's name, MOTHER)""" 
def set_parent(tree,person_name,parent_name,which_parent):
    if person_name in tree and parent_name in tree:
        if tree[person_name][FATHER] == parent_name or tree[person_name][MOTHER] == parent_name:
            print("Mother and father cannot be same person.")
        elif person_name == parent_name and which_parent == MOTHER:
            print("Person cannot be their own mother.")
        elif person_name == parent_name and which_parent == FATHER:
            print("Person cannot be their own father.")
        elif tree[parent_name][MOTHER] == person_name or tree[parent_name][FATHER] == person_name:
            print("Person cannot be the mother or father of own parent.")
        elif tree[person_name][which_parent] == NONE:
            tree[person_name][which_parent] = parent_name
            tree[parent_name][CHILDREN].append(person_name)
        else:
            if which_parent == MOTHER:
                print("Mother already exists")
            elif which_parent == FATHER:
                print("Father already exists")
    else:
        print("Person does not exist.")

"""helper function for is_ancestor and is_descendant. takes int parameter n and returns string."""
def generation_gap(n):
	if n == 1:
		return "grand"
	elif n == 2:
		return "great-grand-"
	else:
		s = ""
		for _ in range(n-1):
			s = s + "great-"
		s = s + "grand-"
		return s

"""
checks if one is ancestor of another. Parameter generation tracks how far apart they are in terms of generation and always starts at 0. 
Original is name of original person to whom we search the relation with.
"""
def is_ancestor(tree,ancestor_name,person_name,original,generation):
	if original not in tree or ancestor_name not in tree:
		print("Person does not exist.")
		return
	if tree[person_name][MOTHER] == NONE and tree[person_name][FATHER] == NONE:
		if generation == 0:
				print(ancestor_name,"is not an ancestor of",person_name)
		return False
	elif tree[person_name][MOTHER] == ancestor_name:
		if generation == 0:
			print(ancestor_name,"is the mother of",original+".")
		else:
			s = generation_gap(generation)+"mother"
			print(ancestor_name,"is the",s,"of",original+".")
		return True
	elif tree[person_name][FATHER] == ancestor_name:
		if generation == 0:
			print(ancestor_name,"is the father of",original+".")
		else:
			s = generation_gap(generation)+"father"
			print(ancestor_name,"is the",s,"of",original+".")
		return True
	if tree[person_name][MOTHER] != NONE and is_ancestor(tree,ancestor_name,tree[person_name][MOTHER],original,generation+1) == True:
		return True
	if tree[person_name][FATHER] != NONE and is_ancestor(tree,ancestor_name,tree[person_name][FATHER],original,generation+1) == True:
		return True
	if generation == 0:
		print(ancestor_name,"is not an ancestor of",person_name)

def is_descendant(tree,ancestor_name,person_name,original,generation):
	if original not in tree or ancestor_name not in tree:
		print("Person does not exist.")
		return
	if tree[person_name][MOTHER] == NONE and tree[person_name][FATHER] == NONE:
		if generation == 0:
			print(original,"is not a descendant of",ancestor_name)
		return False
	elif tree[person_name][MOTHER] == ancestor_name or tree[person_name][FATHER] == ancestor_name:
		print(original,"is a descendant of",ancestor_name)
		return True

	if tree[person_name][MOTHER] != NONE and is_descendant(tree,ancestor_name,tree[person_name][MOTHER],original,generation+1) == True:
		return True
	if tree[person_name][FATHER] != NONE and is_descendant(tree,ancestor_name,tree[person_name][FATHER],original,generation+1) == True:
		return True
	if generation == 0:
		print(original,"is not a descendant of",ancestor_name)

"""takes tree and name as parameters and display person's data""" 
def display_person(tree,person_name):
	if person_name in tree:
		print(person_name)
		print("     Mother:",tree[person_name][MOTHER]+", Father:",tree[person_name][FATHER])
		l1 = tree[person_name][CHILDREN]
		print("     Children: ", end="")
		print(*l1, sep= ", ")
	else: 
		print("Person does not exist.")

"""displays everyone's info in family tree"""
def display_people(tree):
	if tree:
		for keys in tree:
			display_person(tree,keys)
	else:
		print("Family tree is empty.")

"""Saves family tree in a file from which it can be later loaded in. Accepts name of file (string) as parameter."""
def save_file(tree,file_name):
	file = open(file_name,"w")
	#traversing dictionary
	for key in tree.keys():
		for values in tree[key].keys():
			if values == CHILDREN:
				arr = tree[key][values] 
				for i in range(len(arr)):
					file.write(str(arr[i]))
					file.write(" ")
			else:
				file.write(str(tree[key][values]))
			#making a gap between the data so can be read as list later on
			file.write(" ")
		#creates newline
		file.write('\n')
	file.close()

"""loads saved files"""
def load_file(tree,file_name):
	file = open(file_name,"r")
	#traversing file
	for file_line in file:
		#index 0 is name. 1 is Mother. 2 is Father. 3 is for Children list.
		if file_line[0] in tree:
			print(file_line[0],"already exists.")
		else:
			file_line = file_line.split()
			tree[file_line[0]] = {NAME: file_line[0], MOTHER: file_line[1], FATHER: file_line[2], CHILDREN: []}
			if len(file_line) > 4:
				#Final index is '\n'. So Children list is file_line list starting from index 3 and excluding final index.
				tree[file_line[0]][CHILDREN] = file_line[3:len(file_line)]
	file.close()

"""runs loop and acts as command line. takes dictionary as parameter"""
def command_line_loop(tree):
	command_string = "initialize"
	while True:
		command_string = input(">> ")
		# line[0] is the command. following indexes are always names.
		line = command_string.split()
		if line[0].lower() == "create":
			create_person(tree,line[1])
		elif line[0].lower() == "set-mother":
			set_parent(tree,line[1],line[2],"MOTHER")
		elif line[0].lower() == "set-father":
			set_parent(tree,line[1],line[2],"FATHER")
		elif line[0].lower() == "display-person":
			display_person(tree,line[1])
		elif line[0].lower() == "display-people":
			display_people(tree)
		elif line[0].lower() == "is-ancestor":
			is_ancestor(tree,line[1],line[2],line[2],0)
		elif line[0].lower() == "is-descendant":
			is_descendant(tree,line[2],line[1],line[1],0)
		elif line[0].lower() == "save":
			save_file(tree,line[1])
			print("File saved.")
		elif line[0].lower() == "load":
			load_file(tree,line[1])
			print("File",line[1],"has been loaded successfully.")	
		elif line[0].lower() == EXIT:
			return
		else:
			print("Invalid Command.")

if __name__ == '__main__':
	family_tree = {}
	command_line_loop(family_tree)
