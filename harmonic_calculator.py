
MUSICAL_NOTES = ['C','D\u266d','D','E\u266d','E','F','G\u266d','G','A\u266d','A','B\u266d','B']
#using constants to compare where to take half step and where to take full steps
FULL_STEP = [0,2,3]
FIFTH_STEP = 5
EXIT_STRING = "quit"

def translator(string):
	if "flat" in string:
		dummy = string.split()
		dummy[1] = "\u266d"
		result = "".join(dummy)
	else:
		return string
	return result

#Calculates index and returns -1 if input is not a musical note
def index_calc(string):
	for i in range(12):
		if string == MUSICAL_NOTES[i]:
			return i
	return -1

def scale_calc(string):
	string = translator(string)
	n = index_calc(string)
	i = 0
	scale_list = []
	if n == -1:
		output = "There is no starting note " + string
		return output
	else:
		while i < 8:
			scale_list.append(MUSICAL_NOTES[n])
			if i in FULL_STEP:
				n += 2
			elif i == FIFTH_STEP:
				n += 3
			else:
				n += 1
			if n > 11:
				n = n % 12
			i += 1
		return scale_list

if __name__ == '__main__':
	my_input = 0
	while my_input != EXIT_STRING:
		my_input = input("Enter a starting note (C, D flat): ")
		if my_input != EXIT_STRING:
			output = scale_calc(my_input)
			print(*output)


