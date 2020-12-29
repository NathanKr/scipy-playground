from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x*x

X = np.arange(-3,3,0.1)
plt.plot(X,f(X),'.')
plt.title("x^2")
plt.show()

# The default (Nelder Mead)
print(optimize.minimize(f, x0=100))
