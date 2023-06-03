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


t = np.concatenate((t1 ,t2 , t3))
T = np.concatenate((T1 ,T2 , T3))

dt = 1
dT = 0.05

Plots.plotPoints(t, T, [dt]*len(t), [dT]*len(T))
Plots.show("Plot of temperature", "Time: t, s", "Temperature: T, K")



