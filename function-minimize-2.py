from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return pow(x[0]-1,2)+pow(x[1]-2,2)

X1 = np.arange(-3,3,0.1)
X2 = np.arange(-3,3,0.1)

# plt.plot(X1,f(X1,2),'.')
# plt.title("(x1-1)^2 + (x2-2)^2 -> X2=2")
# plt.xlabel("X1")
# plt.grid()
# plt.show()

# plt.plot(X2,f(1,X2),'.')
# plt.title("(x1-1)^2 + (x2-2)^2 -> X1=1")
# plt.xlabel("X2")
# plt.grid()
# plt.show()

# The default (Nelder Mead)
print(optimize.minimize(f, x0=[100,100]))
