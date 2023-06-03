import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

p = 8930
d = 0.135 * 10 ** (-3)


along_p = p * np.pi * (d ** 2) / 4


#print(along_p)


v_mean = np.array([43.4,90.2,135.6,180.0,226.4], dtype=float)


v_error = np.array([1.4,2.4,1.9,2.3,3.4], dtype=float)
overtones = np.arange(1, 6)

def show(n, v):
    x = n 
    y = v

    err_x = np.array([0.001] * len(v), dtype=float)
    err_y = np.array(v_error, dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    # Plots.show("Orthogonal Distance Regression with errors", "number of overtone: n"
    #            , "frequency: v, $s^{-1}$")

    return betas

betas = show(overtones, v_mean)

print(betas)

F = 0.3
dF = 0.01
l = 0.62
dl = 0.01

def ro_l(F, l, b):

    return F / (4 * (l ** 2) * (b ** 2))


printProp(ro_l, [F, l, betas[0]], [dF, dl, betas[2]])

mean_ro_l = ro_l(F, l, betas[0])
error_ro_l = errorFunc(ro_l, [F, l, betas[0]], [dF, dl, betas[2]])

def ro(mean_ro_l):
    global d

    return 4 * mean_ro_l / (np.pi * d ** 2)


printProp(ro, [mean_ro_l], [error_ro_l])