import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

h = np.array([1.36,1.68,1.88,2.00,2.12,2.20,2.24,2.28,2.32,2.40])
t = np.array([0,300,600,900,1200,1500,1800,2100,2400,2700])

dh = 0.04
dt = 2


def show(t, h):
    global dh, dt
    x = t[:3]
    y = h[:3]
    dx = dt
    dy = dh

    err_x = np.array([dx] * len(x), dtype=float)
    err_y = np.array([dy] * len(y), dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    Plots.show("Orthogonal Distance Regression with errors", "time: t, s"
               , "height: h, mm")

    return betas

show(t, h)