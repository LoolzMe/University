import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

f = np.array([40,45,50,55,60], dtype=float)



a1 = 0.034
a2 = 0.027

omega1 = np.array([0.122,0.102,0.096,0.090,0.086], dtype=float)
omega2 = np.array([0.101,0.092,0.082,0.074,0.062], dtype=float)

def inverse(x):
    return 1 / (2 * np.pi * x)

f = inverse(f)


def show(o, O):
    x = o 
    y = O
    do = np.zeros((5), dtype=float)
    dO = 10 ** (-3)
    
    for i in range(5):
        do[i] = errorFunc(inverse, [inverse(o[i])], [10 ** (-3)])

    err_x = np.array(do, dtype=float)
    err_y = np.array([dO] * len(O), dtype=float)
    betas = Plots.plotODR(x, y, err_x, err_y)
    Plots.plotPoints(x, y, err_x, err_y)
    # Plots.show("Orthogonal Distance Regression with errors", "angular velocity: 1/omega, s"
    #            , r"angular velocity: omega, $s^{-1}$")

    return betas


beta1 = show(f, omega1)
beta2 = show(f, omega2)

# print(beta1)
# print(beta2)

# beta = Student.combineErrors([beta1[0], beta2[0]], [beta1[2], beta2[2]], [len(f), len(f)])

print(beta1)
print(beta2)

m = 204 * (10 ** (-3))
dm = 1 * (10 ** (-3))
da = 5 * 10 ** (-4)
g = 9.81

def moment(m, k, a):
    global g, f
    return m * g * a / (k)


printProp(moment, [m, beta1[0], a1], [dm, beta1[1], da])
printProp(moment, [m, beta2[0], a2], [dm, beta2[1], da])
