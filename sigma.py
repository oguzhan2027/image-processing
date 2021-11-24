import numpy as np
import matplotlib.pyplot as plt
def gaussian(x,mu,sig):
    return np.exp(-np.power(x -mu,2.)/(2*np.power(sig,2)))

x_values= np.linspace(-5,5,35)
for mu ,sig in [(-1,1),(0,2),(2,3)]:
    plt.plot(x_values, gaussian(x_values,mu,sig))

plt.show()