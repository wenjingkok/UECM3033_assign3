import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

a = 1.0
b = 0.2
y = [0.1, 1.0]
t = np.linspace(0, 5, 100)

def deriv(y, t, a, b):
    y0, y1 = y
    dydt = [a*y0-a*y0*y1, -b*y1 + b*y0*y1]
    return dydt

solution = odeint(deriv, y, t, args=(a, b))

plt.figure(figsize=(8,8))
plt.plot(t, solution[:, 0], 'b', label='y0(t)')
plt.plot(t, solution[:, 1], 'r', label='y1(t)')
plt.grid()
plt.title('Graph of y0 and y1 against t')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(loc='best')
plt.savefig('GraphAgainstT.jpg')

plt.figure(figsize=(8,8))
plt.plot(solution[:, 0], solution[:, 1])
plt.grid()
plt.title('Graph of y0 against y1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.legend(loc='best')
plt.savefig('GraphY0Y1.jpg')