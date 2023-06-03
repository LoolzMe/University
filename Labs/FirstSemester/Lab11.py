import numpy as np
from Derivative import  errorFunc
import Student
import Plots




h = 50 * 10 ** (-2)
M = 62.4 * 10 ** (-3)

def ratioM(m, M):
    return np.sqrt(M / m)

m = np.array(
    [12.0,
    5.5,
    6.5,
    8.5,
    10.0], dtype=float
)
m = m * 10 ** (-3)

dm = 0.1 * 10 ** (-3)

ratio_m = np.array([2.3,3.4,3.1,2.7,2.5], dtype=float)

t = np.array([1045,1552,1478,1253,1179], dtype=float)
t = t * 10 ** (-3)

error_t = np.array([2,5,11,4,3], dtype=float) * 10 ** (-3)
error_r = np.zeros((len(m), ))


x = ratio_m
y = t

for i in range(len(m)):
    error_r[i] = errorFunc(ratioM, [m[i], M], [dm, dm])


betas = Plots.plotODR(x, y, error_r, error_t)
Plots.plotPoints(x, y, error_r, error_t)
Plots.show("Orthogonal Distance Regression with errors", "square of ratio: sqrt(M/m)"
            , "time: t, s")

def gravitational(alpha, h):
    return 4 * np.power(h, 1) / np.power(alpha, 2)

error_a = errorFunc(gravitational, [betas[0], h], [betas[2], 10 ** (-3)])
a = gravitational(betas[0], h)
print(a, error_a)

