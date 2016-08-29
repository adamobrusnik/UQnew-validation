import numpy as np

def w(i, xi):
	if i in [3,5,7]:
		wi = 2*( 1.1*xi / (xi + 0.1) - 0.5 )
	else:
		wi = 2*( xi - 0.5 )
	return wi

def beta(i,j=None,l=None,s=None, verbose=False):

	if i == 0 or j == 0 or l == 0 or s == 0:
		raise ValueError('Zero value passed to beta, UNACCEPTABLE')
	

	if not (j or l or s):
		#print 'just i is on'
		if i in xrange(1, 11):
			beta = 20.0
		else:
			beta = np.random.normal(loc=0.0, scale=1.0)
	elif not (l or s):
		if i in xrange(1,7) and j in xrange(1,7):
			beta = -15.0
		else:
			beta = np.random.normal(loc=0.0, scale=1.0)
	elif not s:
		if i in xrange(1,6) and j in xrange(1,6) and l in xrange(1,6):
			beta = -10.0
		else:
			beta = 0.0
	elif i and j and l and s:
		if i in xrange(1,5) and j in xrange(1,5) and l in xrange(1,5) and s in xrange(1,5):
			beta = 5
		else:
			beta = 0
	else:
		raise ValueError('Beta calculation failed, at least "i" has to be defined')
	
	return beta

def morristest(x, verbose=False):
	beta0 = 1
	y = beta0

	for i in xrange(1, 21):
		if verbose:
			print 'Adding i = (' + str(i) + ') beta is ' + str(beta(i))
		y += beta(i)*w(i, x[i-1])
	for j in xrange(1,21):
		for i in xrange(1,j):
			if verbose:
				print 'Adding (i,j) = (' + str(i) + ',' + str(j) + ') beta is ' + str(beta(i,j))

			y += beta(i,j)*w(i, x[i-1])*w(j, x[j-1])
	for l in xrange(1,21):
		for j in xrange(1,l):
			for i in xrange(1,j):
				if verbose:
					print 'Adding (i,j,l) = (' + str(i) + ',' + str(j) + ','+str(l)+') beta is ' + str(beta(i,j,l))
				y += beta(i,j,l)*w(i, x[i-1])*w(j, x[j-1])*w(l, x[l-1])
	
	for s in xrange(1,21):
		for l in xrange(1,s):
			for j in xrange(1,l):
				for i in xrange(1,j):
					if verbose:
						print 'Adding (i,j,l,s) = (' + str(i) + ',' + str(j) + ','+str(l)+','+str(s)+') beta is ' + str(beta(i,j,l,s))
					y += beta(i,j,l,s)*w(i, x[i-1])*w(j, x[j-1])*w(l, x[l-1])*w(s, x[s-1])
				
	return y

def gtest(x):
	a = {}
	a[1] = 0.001
	a[2] = 89.9
	a[3] = 5.54
	a[4] = 42.10
	a[5] = 0.78
	a[6] = 1.26
	a[7] = 0.04
	a[8] = 0.79
	a[9] = 74.51
	a[10] = 4.32
	a[11] = 82.51
	a[12] = 41.62
	
	g = 1
	for i in xrange(1,13):	
		g = g * (np.abs(4*x[i-1] - 2) + a[i])/(1+a[i])

	return g 
