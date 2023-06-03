import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

def g(h1, h2):
    return h1 / (h1 - h2)

gamma = np.array([1.36,      1.36,      1.48275862,1.45714286,1.42222222,1.34285714
,1.31707317,1.28358209,1.31666667,1.29411765])

h1 = np.array([6.8,6.8,4.3,5.1,6.4,4.7,5.4,8.6,7.9,6.6])



h2 = np.array([1.8,1.8,1.4,1.6,1.9,1.2,1.3,1.9,1.9,1.5])


# for i in range(len(h1)):
#     #print(h1[i] / (h1[i] - h2[i]))
#     printProp(g, [h1, h2], [0.1, 0.1])


dg = np.array([0.02813681,0.02813681,0.05377132,0.0436334, 0.03296828,0.03959815
,0.03304151,0.01961992,0.02257019,0.02602195])


print(Student.combineErrors(gamma, dg, [1] * len(gamma)))