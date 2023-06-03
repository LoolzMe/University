import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


def coefW(rho, T, h, alpha, ph, p1):
    return rho * 8.31 * T * h * alpha / (18 * 10**(-3) * (ph - p1))

def coef(rho, T, h, alpha, ph, p1, p0):
    return rho * 8.31 * T * h * alpha / (18 * 10**(-3) * p0 * np.log((p0 - p1) / (p0 - ph)))



alpha = 0.0008 * 10**(-3)
da = 0.0001 * 10**(-3)

T = np.array([289.7,289.7,289.6,289.4,289.4,289.3,289.2,289.2,289.1,289.1])
dT = 0.1

h = np.array([1.40,1.64,1.88,2.00,2.12,2.20,2.24,2.28,2.32,2.40]) * 10**(-3) 
dh = 0.04 * 10**(-3)

p0 = 134122
dp0 = 133

ph = 1817
p1 = 1126
dp1 = 59

print(len(T[:3]))

for t, k in zip(T[:3], h[:3]):
    print(coef(10**(3), t, k, alpha, ph, p1, p0))
    print(errorFunc(coef, [10**(3), t, k, alpha, ph, p1, p0], [0, dT, dh, da, 0, dp1, dp0]))




