from functions import *
from models import morristest, w, beta
import pickle
import matplotlib.pyplot as plt

RUNS = 20

k = 20

x = np.ones(k)

#print morristest(x/2)

# Initialization of the dictionary of EE's 
indices = xrange(0,20)
ees = {ind: np.array([]) for ind in indices}
for i in xrange(0, RUNS):
	Bstar, deltas, indices = generate_matrix(k, 4)
	steps = Bstar.shape[0]
	print '-------------------'
	print 'TRAJECTORY ' + str(i+1) + ' out of ' + str(RUNS)
	print '-------------------'
	for j in xrange(0, steps):
		plt.cla(); plt.clf()
		if j == 0:
			#print '\tStarting point'
			x = np.asarray(Bstar[j, :]).flatten()
			y = morristest(x)
		else:
			x = np.asarray(Bstar[j, :]).flatten()
			ynew = morristest(x)
			delta = deltas[j-1]
			index = indices[j-1]
			ee = (ynew-y)/delta
			ees[index] = np.append(ees[index], ee)
			#print '\tPoint ' + str(j) + '\t EE = ' + str(ee)
			#print '\t\tindex = ' + str(index)
			#print '\t\tdelta = ' + str(delta)
			y = ynew
	keys = ees.keys()
	for key in keys:
	    mu = np.mean(ees[key])
	    mustar = np.mean(np.absolute(ees[key]))
	    sigma = np.std(ees[key])
	    print str(key+1) + '\t' + str(mu) +  '\t' + str(mustar) + '\t' + str(sigma)
	#for j in xrange(0, steps):	
	#	plt.plot(np.mean(ees[j]), np.std(ees[j]))
	#	plt.draw()

pickle.dump(ees, open('ees.p', 'wb'))
