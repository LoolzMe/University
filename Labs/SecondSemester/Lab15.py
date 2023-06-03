import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


alpha = np.array([0.00000925,0.00001281,0.00001958,0.00002377,0.00002376,0.000022670,0.00001846])

t = np.array([74,113,139,160,181,203,230])

l = np.array([0.01,0.02,0.03,0.04,0.05,0.06,0.07])





da = 0.000001 * np.array([2, 3, 7, 1, 1, 9, 6])
dl = 0.001

dt = 6

# def alp(l2, l1, t2, t1):
#     return (1/ (20 + l1) * (l2 - l1) / (t2 - t1))

# for i in range(1, len(t)):

#     printProp(alp, [l[i], l[i - 1], t[i], t[i - 1]], [dl, dl, dt, dt])


def r(a, E):
    return ((1.38 * 10 ** (-23)) / (2 * a * E)) ** (1/3)

printProp(r, [0.000013, 1.1 * 10**(11)], [ 0.00001, 0])

def show(t, h):
    global da, dt
    x = t[1:]
    y = h[1:]
    dx = dt
    dy = da[1:]

    err_x = np.array([dx] * len(x), dtype=float)
    err_y = np.array(dy, dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    Plots.show("Orthogonal Distance Regression with errors", "temperate: t, C"
               , "coefficient of linear expansion: a, 1/C")

    return betas

betas = show(t, alpha)


print(betas[1] + 20 * betas[0])
print(Student.appr(betas[3], len(t[1:])))
print(1.6898092551284268e-10 * 1.1 * 10**(11))
print(4.3461951729695e-11 * 1.1 * 10**(11))


def gamma(b, r):
    return b / (2*r)

printProp(gamma, [18.587901806412695, 1.6898092551284268e-10], [4.780814690266451, 4.3461951729695e-11])