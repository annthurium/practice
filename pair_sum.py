# given an integer array, output all pairs that sum up to a specific value k

def pairSum(array, k):
	"""Output list of all pairs that sum to a specific value, k."""
	if len(array) < 2:
		return
	# do a single pass over the array to check if it's in the set of seen numbers
	seen = set()
	output = set()
	for num in array:
		target = k - num
		if target not in seen:
			seen.add(num)
		else:
			output.add( (min(num, target), max(num, target)) )
	print '\n'.join( map (str, list(output)))


pairSum([1, 2, 3, 4, 5, 0], 5)