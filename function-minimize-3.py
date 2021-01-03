from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x,a,b):
    print(a,b)
    return a*(x-1)*(x-1) - b

a_=4
b_=16
X = np.arange(-4,6,0.1)
plt.grid()
plt.plot(X,f(X,a_,b_),'.')
plt.title("a*(x-1)^2-b")
plt.xlabel('X')
plt.ylabel('f(x,a,b)')
plt.show()

# The default (Nelder Mead)
print(optimize.minimize(f, x0=100,args=(a_,b_)))
