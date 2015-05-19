import random
import string

def shakespeare(target):
	""" This function takes a target string made up of letters and spaces, and
		sees how long it takes for the function to generate the same string of
		text using random.choice on the set of all lowercase letters.
	"""

	target = target.lower() # a little text processing
	my_text = [] # make my text a list so it is mutable
	letters = string.ascii_lowercase + ' '  # all lowercase letters plus space.

	# generate the first attempt at shakespeare
	for i in range(len(target)):
		my_text.append(random.choice(letters))
		# we generate a list once, then check & change the items in the list
		# one by one. this works out because we eventually join the elements.

	attempts = 1

	for i in range(len(target)):
		while target[i] != my_text[i]:
			my_text[i] = random.choice(letters)
			attempts += 1
		
	print("Target text: " + target)
	print("Generated text: " + ''.join(my_text))
	print("This took %s tries." % attempts)

