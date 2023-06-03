import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


a1 = np.array([0.034,0.044,0.054,0.064,0.074], dtype=float)
a2 = np.array([0.027,0.037,0.047,0.057,0.067], dtype=float)
omega1 = np.array([0.122,0.147,0.180,0.208,0.240], dtype=float)
omega2 = np.array([0.098,0.137,0.162,0.189,0.221], dtype=float)



def show(a, o):
    x = a 
    y = o
    da = 5 * 10 ** (-4)
    do = 10 ** (-3)
    err_x = np.array([da] * len(a), dtype=float)
    err_y = np.array([do] * len(o), dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    # Plots.show("Orthogonal Distance Regression with errors", "distance: a, m"
    #            , r"angular velocity: omega, $s^{-1}$")

    return betas


beta1 = show(a1, omega1)
beta2 = show(a2, omega2)

#beta = Student.combineErrors([beta1[0], beta2[0]], [beta1[2], beta2[2]], [len(a1), len(a2)])

#print(beta)

f = 40
m = 204 * (10 ** (-3))
dm = 1 * (10 ** (-3))
g = 9.81

def moment(m, k):
    global g, f
    return m * g / (k * 2 * np.pi * f)


error_m1 = errorFunc(moment, [m, beta1[0]], [dm, beta1[2]])
error_m2 = errorFunc(moment, [m, beta2[0]], [dm, beta2[2]])

m1 = moment(m, beta1[0])
m2 = moment(m, beta2[0])

print([m1, m2], [error_m1, error_m2])
print(Student.combineErrors([m1, m2], [error_m1, error_m2], [1, 1]))