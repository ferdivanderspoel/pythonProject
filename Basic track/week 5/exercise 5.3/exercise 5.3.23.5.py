def add_vectors(u, v):
	"""
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
	newvec = [ ]
	for i in range(len(u)):
		newvec = newvec + [u[i] + v[i]]
	print(newvec)