
a = []
b = []
my_input = 0

while my_input != "quit":
	my_input = input(">>>")
	new_input = my_input.split()

	if new_input[0].lower() == "add":
		if new_input[1] == "A":
			a.append(new_input[2])
		elif new_input[1] == "B":
			b.append(new_input[2])

	if new_input[0].lower() == "display":
		if new_input[1] == "A":
			print(">>>",*a)
		elif new_input[1] == "B":
			print(">>>",*b)

	if new_input[0].lower() == "transfer":
		if new_input[1] == "A":
			if len(a) > 0:
				b.append(a[0])
				a.pop(0)
			else:
				print(">>>Bin A is empty.")
		elif new_input[1] == "B":
			if len(b) > 0:
				a.append(b[0])
				b.pop(0)
			else:
				print(">>>Bin B is empty.")

	if new_input[0].lower() == "remove":
		if new_input[1] == "A":
			if new_input[2] in a:
				a.remove(new_input[2])
			else:
				print(">>>Does not exist.")
		elif new_input[1] == "B":
			if new_input[2] in b:
				b.remove(new_input[2])
			else:
				print(">>>Does not exist.")