# given a 2-d rectangular matrix of boolean values, 
# write a function which returns whether or not the matrix is the same when rotated 180 degrees.

class Matrix(object):
	"""A simple Python matrix class with
	basic operations and operator overloading."""

	def __init__(self, m, n, init=True):
		if init:
			self.rows = [[0] * n for x in range(m)]
		else:
			self.rows = []
		self.m = m
		self.n = n

	def __getitem__(self, idx):
		return self.rows[idx]

	def __setitem__(self, idx, item):
		self.rows[idx] = item

	def __str__(self):
		s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
		return s + '\n'

	def __repr__(self):
		s = str(self.rows)
		rank = str(self.getRank())
		rep ="Matrix: \"%s\", rank: \"%s\"" % (s, rank)
		return rep

	def reset(self):
		"""Rest the matrix data """
		self.rows = [[] for x in range(self.m)]

	def transpose(self):
		"""Transpose the matrix. Changes the current matrix """

		self.m, self.n = self.n, self.m
		self.rows = [list(item) for item in zip(*self.rows)]

	def getTranspose(self):
		"""Return a transpose of the matrix without modifying the matrix itself."""

	def getRank(self):
		return (self.m, self.n)

	def __eq__(self, mat):
		"""Test equality """

		return (mat.rows == self.rows)
