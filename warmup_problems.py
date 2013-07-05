def factorial(n):
	"""Returns n!"""
	if n <= 1:
		return n
	else:
		return n * factorial(n - 1)

print factorial(5)

# output a string in reverse
def reverse_string(string):
	"""takes a string as input, returns reversed string as output"""
	return string[-1::-1]

print reverse_string('pool')

reversed_string = []
def reverse_string_recursive(string):
	"""takes a string as input, outputs reversed string"""
	# base case is an empty string

	# pop letters off of string in reverse order until string is empty
	if len(string) == 0:
		return string
	else:
		
		return string[-1] + reverse_string_recursive(string[:-1])


def reverse_string(str):
	"""Takes a string, returns reversed string as output."""
	new_str = ""
	for i in range (0, len(str)):
		new_str += str[-1-i]

	print new_str
	return new_str


# reverse_string('')

listy_doo = ['p', 'o', 'o', 'l']

def reverse_list_recursively(list):
	"""Takes a list, returns list sorted in reverse order."""
	new_list = []
	def recursive(list):
		if len(list) > 0:
			new_list.append(list.pop())
			recursive(list)
		else:
			return
	recursive(list)
	return new_list

# print reverse_list_recursively(listy_doo)

# output fibonacci sequence up to letter n
def print_fibonacci(n):
	"""prints fibonacci sequence up to nth letter"""
	base = [0, 1]
	for i in range(0, n):
		base = (base[1], sum(base))
		print base[0]

	
def fibonacci(n):
	base = [0, 1]
	list = []
	for i in range(0, n):
		temp = base[1]
		base[1] = base[0] + base[1]
		base[0] = temp
		list.append(base[0])
	return list

print fibonacci(12)