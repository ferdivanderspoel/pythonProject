def dot_product(u, v):
	"""
	>>> dot_product([1, 1], [1, 1])
	2
	>>> dot_product([1, 2], [1, 4])
	9
	>>> dot_product([1, 2, 1], [1, 4, 3])
	12
	"""
	for i in range(len(u)):
		prod = (u[i] * v[i]) + (u[i] * v[i])
	return prod