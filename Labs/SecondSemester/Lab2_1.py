import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots



t1 = np.array([0,120,210,310,390,490])

T1 = np.array([2.1,2.05,2.0,1.95,1.9,1.85])

t2 = np.array([527,530,540,554,567,580,602,615,630,637])

T2 = np.array([2.0,2.2,2.5,2.7,3.0,3.2,3.6,3.9,4.1,4.2])

t3 = np.array([661,718,786,849,1224,1281,1391,1442])


T3 = np.array([4.3,4.2,4.1,4.0,3.55,3.5,3.4,3.35])


dt = 1
dT = 0.05

def show(t, T):
    global dt, dT
    x = t
    y = T

    err_x = np.array([dt] * len(x), dtype=float)
    err_y = np.array([dT] * len(y), dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    # Plots.show("Orthogonal Distance Regression with errors, Temperature T2", "Time: t, s"
    #            , "Temperature: T, K")

    return betas

betas1 = show(t1, T1)


betas3 = show(t3, T3)


#print(betas1)


def theta(b1, b3, t1, t3):
    return -0.5 * (b1 + b3) * (t3 - t1)


printProp(theta, [betas1[0], betas3[2], t1[-1], t3[0]], [betas1[2], betas3[2], dt, dt])


th = 0.041854797692104394

dth = 0.0028620482648336588

m = 0.128
dm = 0.1 * 10 ** (-3)

p = 12
dp = 0.2

w = 170

def c(p, t1, t2, T1, T3, th, m):
    global w
    return (p * (t2 - t1) / (T3 - T1 + th) - w) / m


printProp(c, [p, t1[-1], t2[-1], T1[-1], T3[0], th, m], [dp, dt, dt, dT, dT, dth, dm])
