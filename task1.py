import numpy as np
import sympy as sy
from numpy.polynomial import legendre
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    #Default interval for leggauss is [-1, 1]
    x, w = legendre.leggauss(n)
    #Translate the x value to new interval [a, b]
    t = 0.5 * (x * (b - a) + (b + a))
    ans = sum(w * f(t)) * 0.5 * (b - a)
    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
