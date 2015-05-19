import random
import string

def shakespeare(target):

	# set our target and our range of letters
	target = target.lower() # a little text processing
	my_text = [] # make my text a dictionary so it is mutable
	letters = string.ascii_lowercase + ' '

	# generate the first attempt at shakespeare
	for i in range(len(target)):
		my_text.append(random.choice(letters))

	attempts = 1

	for i in range(len(target)):
		while target[i] != my_text[i]:
			my_text[i] = random.choice(letters)
			attempts += 1
		
	print("Target text: " + target)
	print("Generated text: " + ''.join(my_text))
	print("This took %s tries." % attempts)

