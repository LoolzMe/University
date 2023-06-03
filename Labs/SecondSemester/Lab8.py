import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


n0 = 1.05 * 10 ** (-3)


t = np.array([61.3,64.7,67.7,77.3,79.0])

dt = np.array([1.7,1.7,1.7,8.0,1.0])

tx = 73.0
dtx = 1.0


c = np.array([0,5,10,15,20])

ro = np.array([1.0, 1.051,1.107,1.167,1.23]) * 1000

def nu(t0, t,ro0, ro):
    global n0
    return n0 * (t/t0) * (ro / ro0)

# printProp(nu, [np.array([t[0]]*len(t[1:])), t[1:], np.array([1000]*len(ro[:])), ro], [np.array([dt[0]] * len(dt[1:])), dt[1:], np.array([0.001] * len(ro)), np.array([0.001] * len(ro))])


# printProp(nu, [t[0], tx, 1000,])
nu1 = np.array([0.00116476, 0.0012837,  0.00154518, 0.00166441])
dnu1 = np.array([4.44972929e-05 ,4.80256696e-05, 1.65557019e-04, 5.07392132e-05])

def show(t, ro):
    global dt
    x = ro
    y = t
    dx = [0.0000001]*len(ro)
    dy = dt

    err_x = np.array(dx)
    err_y = np.array(dy)
    betas = Plots.plotODR(x, y, err_x, err_y)
    # Plots.plotPoints(x, y, err_x, err_y)
    # Plots.plotLine(x, [betas[0], betas[1] + betas[3]])
    # Plots.plotLine(x, [betas[0], betas[1] - betas[3]])
    # Plots.show("Orthogonal Distance Regression with errors", "density: ro"
    #            , "time: t")

    return betas

# betas_ro = show(t, ro)


# print(betas_ro)


def reverse(x, b1, b2):
    return (x - b2) / b1


# printProp(reverse, [tx, betas_ro[0], betas_ro[1]], [dtx, betas_ro[2], betas_ro[3]])

rox = 1155
drox = 163

printProp(nu, [t[0], tx, 1000,rox], [dt[0], dtx, 0.001, drox])

def show1(c, nu1):
    global dnu1
    x = c[1:]
    y = nu1
    dx = np.array([0.000001]*len(c[1:]))
    dy = dnu1
    err_x = np.array(dx)
    err_y = np.array(dy)
    betas = Plots.plotODR(x, y, err_x, err_y)
    # Plots.plotPoints(x, y, err_x, err_y)
    # # Plots.plotLine(x, [betas[0], betas[1] + betas[3]])
    # # Plots.plotLine(x, [betas[0], betas[1] - betas[3]])
    # Plots.show("Orthogonal Distance Regression with errors", "concentration: c"
    #            , "viscosity: eta")

    return betas


betas_nu1 = show1(c, nu1)
print(betas_nu1)

nux = 0.0014442210440456774
dnux = 0.000208654532517527
printProp(reverse, [nux, betas_nu1[0], betas_nu1[1]], [dnux, betas_nu1[2], betas_nu1[3]])
