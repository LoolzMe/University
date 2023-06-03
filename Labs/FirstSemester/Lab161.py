import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

p = 8930
d = 0.135 * 10 ** (-3)


along_p = p * np.pi * (d ** 2) / 4


#print(along_p)


v2_mean = np.array([1339.8,1490.2,1616.2,1798.0,2007.2], dtype=float)


v2_error = np.array([49.0,52.3,45.0,57.9,49.5], dtype=float)

overtone = 1

F = np.array([0.1,0.15,0.2,0.25,0.3], dtype=float)

dF = 0.01

def show(f, v2):
    x = f 
    y = v2

    err_x = np.array([dF] * len(f), dtype=float)
    err_y = np.array(v2_error, dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    Plots.show("Orthogonal Distance Regression with errors", "force: F, N"
               , r"frequency: $v^2$, $s^{-2}$")

    return betas

betas = show(F, v2_mean)

print(betas)


l = 0.62
dl = 0.01

def ro_l(l, b):

    return 1 / (4 * (l ** 2) * (b))


printProp(ro_l, [l, betas[0]], [dl, betas[2]])


mean_ro_l = ro_l(l, betas[0])
error_ro_l = errorFunc(ro_l, [l, betas[0]], [dl, betas[2]])

def ro(mean_ro_l):
    global d

    return 4 * mean_ro_l / (np.pi * d ** 2)


printProp(ro, [mean_ro_l], [error_ro_l])