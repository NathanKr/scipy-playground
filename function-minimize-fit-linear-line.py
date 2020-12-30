import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


m=10

# here we actually have a graph with h_teta=teta1*x 
X = np.arange(m)
np.random.seed(42) #use to get the same results every run
rnd = np.random.rand(m)
Y = 2 + np.arange(m)*0.5 + rnd # actually we have h = teta1*x where teta1 is actually 0.5 


def cost_function(Teta):
    H = Teta[0]+X * Teta[1]
    E = Y - H
    cost = np.dot(E,E)/(2*m)
    return cost


res = optimize.minimize(cost_function, x0=[0,0])
teta0=res.x[0]
teta1=res.x[1]

H = teta0+teta1 * X
plt.plot(X, Y,'o',X,H)
plt.title('fit linear line with optimize.minimize')
plt.show()




