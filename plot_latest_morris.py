import numpy as np
import pickle
import matplotlib.pyplot as plt

ees = pickle.load( open( "ees.p", "rb" ) )

keys = ees.keys()
xs = []
mus = []
sigmas = []
fig,ax = plt.subplots()
for key in keys:
    mu = np.mean(ees[key])
    mustar = np.mean(np.absolute(ees[key]))
    sigma = np.std(ees[key])
    xs.append(int(key+1))
    mus.append(float(mu))
    sigmas.append(float(sigma))
    ax.text(mu, sigma, str(key+1))
    plt.plot(mu, sigma, 'rs')
    print str(key+1) + '\t' + str(mu) +  '\t' + str(mustar) + '\t' + str(sigma)
    
plt.show()
