import numpy as np

def generate_matrix(
	k, 
	p=4
	):
	"""
	Generates the design matrix for a trajectory and two vectors which are needed for exploring the trajectory
	
	Args:
	k : int
		Number of model parameters
	p : int (defaults to 4)
		Number of levels
	
	Returns:
	Bstar : (k+1) x k numpy matrix 
		The design matrix for a trajectory
	deltas : k-dim numpy array
		an array of deltas (either +delta or -delta, depending on whether xi is being increased or decreased)
	positions : k-dim numpy array
		a vector of indices, which are being increased/decreased
	
	Note: deltas and positions are k-dim vectors, not (k+1)-dim because they are not defined for the first run (starting point)

	Raises:
	ValueError
		When more than one changes in "x" are detected between two steps
	"""
	m = k+1
	delta = float(p)/(2*(float(p)-1))
	#delta = 1/(2*(float(p)-1))

	# First, let us choose B as a lower triangular matrix
	B = np.tril(np.ones((m, k)), -1)

	# Then let D* be a k-dim diagonal matrix with +1 or -1 on the diagonal (with equal probabilities)
	Dstar_diagonal = np.random.choice([-1, 1], size=k)
	Dstar = np.zeros((k,k))
	np.fill_diagonal(Dstar, Dstar_diagonal)

	# Let J_{m,k} be the m-by-k matrix of 1's
	Jmk = np.ones((m,k))

	test = 0.5 * ( np.dot ( (2*B - Jmk) , Dstar ) + Jmk )


	# Let x* be a randomly chosen "base value" of x, for which each element is randomly assigned from {0, ..., 1-delta}
	# remember that high is exclusive, hence +1
	xstar = np.random.randint(low=0, high=(1-delta)*(p-1)+1, size=k)/float(p-1)

	# We create an identity matrix
	Pstar = np.eye(k)
	# And now we shuffle it (double transpose because shuffle() shuffles the rows)
	np.random.shuffle(Pstar.T)
	Pstar = Pstar.T

	# part 1 is the matrix with base value at each row
	part1 = np.dot(np.matrix(Jmk[:,0]).T , np.matrix(xstar))
	# part2 are the increments
	part2 = 0.5 * delta * ( np.dot ( (2*B - Jmk) , Dstar ) + Jmk )
	#Bstar = np.dot(part1+part2 , Pstar)
	Bstar = np.dot(part1+part2 , Pstar)

	# we calculate deltamat, which is a matrix describing the incremental/decremental changes between successive rows
	deltamat = delta * np.dot(Dstar, Pstar)
	deltas = np.array([])
	indices = np.array([])
	for i in xrange(0, k):
		nz = np.nonzero(deltamat[i,:])
		if len(nz) == 1:
			indices = np.append(indices, nz[0])
			deltas = np.append(deltas, deltamat[i,nz[0]])
		else:
			raise ValueError('ERROR: The program detected more than one change in the "x" vector between two successive steps.')
	#print Bstar
	#print deltas
	#print indices
	#print deltamat
	return Bstar, deltas, indices
