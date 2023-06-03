import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


f1 = np.array([380,690,1010,1340], dtype=float)
f2 = np.array([410,730,1070,1420], dtype=float)
f3 = np.array([420,760,1100,1480], dtype=float)
f4 = np.array([430,780,1150,1530], dtype=float)

n = np.arange(1, 5)
df = 10
dn = 0.00001

def show(n, f):
    global df, dn
    x = n
    y = f

    err_x = np.array([dn] * len(f), dtype=float)
    err_y = np.array([df] * len(n), dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    # Plots.plotPoints(x, y, err_x, err_y)
    # Plots.show("Orthogonal Distance Regression with errors, Temperature T1", "number of resonance: n"
    #            , r"frequency: f, $s^{-1}$")

    return betas


betas = show(n, f4)
l = 51 * (10 ** -2)
R = 8.31
t = np.array([15.0, 31.0, 48.0, 64.0], dtype=float)
t = t + 273.15
dt = 0.5
nu = 29 * (10 ** -3)

def speed(a):
    global l

    return 2 * l * a

def gamma(v, T):
    global R, nu

    return nu * v * v / (T * R)

v = speed(betas[0])
dv = errorFunc(speed, [betas[0]], [betas[2]])

print(v, dv)

printProp(gamma, [v, t[3]], [dv, dt])