class binaryNode:
	def __init__(self, data, lchild, rchild):
		self.data = data
		self.lchild = lchild
		self.rchild = rchild

	# def __iter__(self):
	# 	if self.lchild:
	# 		for node in self.lchild:
	# 			yield node
	# 	if self.rchild:
	# 		for node in self.rchild:
	# 			yield node
	# 	yield self


	def preorder_traversal(self):
		print self.data
		if self.lchild:
			self.lchild.preorder_traversal()
		if self.rchild:
			self.rchild.preorder_traversal()

	def __iter__(self):
		yield self
		if self.lchild:
			for node in self.lchild:
				yield node
		if self.rchild:
			for node in self.rchild:
				yield node

	def iterative_preorder_traversal(self):
		for node in self:
			print node.data


	def lowest_common_ancestor(self, node1, node2):

		pass
		# find node1 on tree
		# find node2 on tree
		# make a list of nodes visited by node1
		# make a list of nodes visited by node2
		# see where the lists diverge

# write a function to find the first nonrepeated character in a string.
def find_first_nonrepeated_character(string):
	"""Finds first non-repeated character in a string."""
	dictionary = dict.fromkeys(string, 0)
	for letter in string:
		dictionary[letter] += 1

	for letter in string:
		if dictionary[letter] == 1:
			return letter


print find_first_nonrepeated_character('total')


# remove specified characters from a string
def removeChars(string, remove):
	"""Remove specified characters from a string."""

	remove_dict = dict.fromkeys(remove, None)

	def generate_new_string(string, remove_dict):
		for letter in string:
			if letter not in remove_dict:
				yield letter
	new_string = generate_new_string(string, remove_dict)
	return ''.join([letter for letter in new_string])

removed_chars = removeChars('Battle of the Vowels: Hawaii vs Grozny', 'aeiou')
print removed_chars

# run time of this algorithm:
# length of string is n, length of remove is m
# for loop on line 69 is n
# lookup in dictionariees is O(1) amortized
# so let's say this is O(n)

# Write a function that reverses the words in a string.

def reverse_words(string):
	"""Reverses the words in a string."""
	word_list = string.split(' ')
	new_word_list = word_list[-1::-1]
	return ' '.join([word for word in new_word_list])

reversed_words = reverse_words("Do or do not, there is no try.")
print reversed_words

# 	def dfs(self, query):
# 		for node in self:
# 			if node.data == query:
# 				return node

# 	def bfs(self, query):
# 		queue = [self]
# 		while queue:
# 			node = queue.pop()
# 			if node.data == query:
# 				return node
# 			if node.lchild:
# 				queue.append(node.lchild)
# 			if node.rchild:
# 				queue.append(node.rchild)

# 	def height(self):
		
# 		if self.lchild:
# 			lheight = 1 + self.lchild.height()
# 		else:
# 			lheight = 1
# 		if self.rchild:
# 			rheight = 1 + self.rchild.height()
# 		else:
# 			rheight = 1
# 		return max(lheight, rheight)

# tree = binaryNode('lesbian',
# 					binaryNode('seagull', 
# 						binaryNode('flies', None, None),
# 						binaryNode('Miley', None, None),
# 					),
# 					binaryNode('booty',
# 						binaryNode('twerk', None, None),
# 						binaryNode('queeeeeeer', None, None)
# 					)
# 				)

# tree.iterative_preorder_traversal()
# print "BFS y'all"
# for node in tree.bfs('Miley'):
# 	print node.height()

# print "\nDFS fo sho"
# for node in tree.dfs('Miley'):
# 	print node.height()