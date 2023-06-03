import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots



h = np.array([6.0,6.8,3.6,4.2,6.7,5.7,2.0], dtype=float)
t = np.array([140, 136, 227, 200, 140, 171, 372], dtype=float)
dt = 3


V = 1.43 * 10 ** (-3)
dV = 0.143 * 10 **(-3)
h *= 10 ** (-2)
dh = 10 ** (-3)
g= 9.8
rho = 1000
r = 0.6 * 10**(-3)
S = np.pi * r**2

l = 10 **(-1)

p = h * g * rho
dp = dh * g * rho

# print(p)
# print(dp)
v = V / (S * t)
dv = dV / (S * t) - V*dt / (S * t**2) # ???
#print(v)
#print(dv)

rho_air = 1.225


pis = rho_air * v ** 2 / 2
#print(pis)


def coef(P, t, V):
    return S * r**2 * P * t / (8*l*V)


err = errorFunc(coef, [p, t, V], [dp, dt, dV])
means = coef(p, t, V)


nu = np.array([2.92977461e-05 ,3.22554234e-05 ,2.85025216e-05, 2.92977461e-05 ,3.27158165e-05, 3.39958490e-05, 2.59494323e-05])

print(rho_air * v * r / (nu))


print(Student.combineErrors(means, err, [1]*len(err)))


from typing import Tuple, List
Bin = Tuple[float, float, int]

def combine(a: Bin, b: Bin) -> Bin:
    a_avg, a_err, n_a = a
    b_avg, b_err, n_b = b
    n = n_a + n_b

    s_avg = ((n_a / n) * a_avg) + ((n_b / n) * b_avg)

    N = n ** 2 - n
    N_a = n_a ** 2 - n_a
    N_b = n_b ** 2 - n_b

    s_err = np.sqrt((N_a / N) * (a_err ** 2)
             + (N_b / N) * (b_err ** 2)
             + (n_a * n_b * (a_avg - b_avg) ** 2) / (n * N)
             )

    return (s_avg, s_err, n)



