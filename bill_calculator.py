BURG = "burger"
SANDW = "sandwich"
SPR = "sprite"
COKE = "coke"
MTN_DEW = "mountain dew"
FRY= "fries"
EXIT_STRING = "place order"


def function(order):
	total = 0
	i = 0
	a = 0 
	b = 0
	c = 0
	discount = 0
	while order[i] != EXIT_STRING:
		if BURG in order[i] or SANDW in order[i]:
			total += 5
			a += 1
		elif FRY in order[i]:
			total += 3
			b += 1
		elif order[i] == COKE or order[i] == MTN_DEW or order[i] == SPR:
			total += 2.50
			c += 1
		else:
			total += 4
		i += 1
	if a > 0 and b > 0 and c > 0:
		discount = (discount + 2) * min(a,b,c)
	return total - discount

if __name__ == '__main__':
	order = []
	my_input = 0
	while  my_input != EXIT_STRING:
		my_input = input("What would you like to order? ")
		order.append(my_input)
	print("The total bill is:",function(order))

	
