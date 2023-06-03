import numpy as np
from Derivative import  errorFunc
import Student
import Plots

mean_t = np.array([1068,996,957,897,823], dtype=float)
mean_t *= 10 ** (-3)

h = np.array([40.8, 37.0, 32.8, 29.9, 25.9], dtype=float) * (10 ** (-2))

error_t = np.abs(np.array([26., 2., 3., 2., 3.], dtype=float) * (10 ** (-3)))

error_h = np.abs(np.array([0.1]*5, dtype=float) * (10 ** (-2)))



x = np.sqrt(h)
y = mean_t
error_h = error_h / (2 * x)


betas = Plots.plotODR(x, y, error_h, error_t)
Plots.plotPoints(x, y, error_h, error_t)
Plots.show("Orthogonal Distance Regression with errors", "square of height: sqrt(h), sqrt(m)"
            , "time: t, s")

def acceleration(alpha):
    return 2 / np.power(alpha, 2)

error_a = errorFunc(acceleration, [betas[0]], [betas[2]])
a = acceleration(betas[0])


