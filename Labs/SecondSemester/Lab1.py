import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots


T0 = 13

dm = 0.01
cu = 4.52
fe = 3.75
al = 1.32

# T = np.array([310,250,220,200,180,170,150,130,120,110,100,90,80,70], dtype=np.float32)

# t = np.array(["1:07","1:31","1:46","1:57","2:10","2:19","2:36","2:56","3:09","3:27","3:37","3:46","4:02","4:21"], dtype=str)


# T = np.array([320,300,280,260,240,210,190,160,150,130,110,90,80,70], dtype=np.float32)
# t = np.array(["0:33","0:39","0:44","0:50","0:57","1:08","1:17","1:34","1:40","1:56","2:13","2:31","2:44","3:00"])
T = np.array([320,300,280,260,240,230,200,180,160,130,100,90,80,70], dtype=np.float32)

t = np.array(["0:36","0:44","0:51","1:00","1:09","1:13","1:30","1:42","1:57","2:26","3:02","3:11","3:28","3:46"], dtype=str)


dt = 3
dT = 5

def fromTStoTime(timestamps):
    if type(timestamps) == list or type(timestamps) == np.ndarray:

        return np.array([int(timestamp.split(":")[0]) * 60 + int(timestamp.split(":")[1]) for timestamp in timestamps])
    else:
        return int(timestamps.split(":")[0]) * 60 + int(timestamps.split(":")[1])



# print(fromTStoTime(t[-1]))

def show(t, T):
    global dt, dT
    x = fromTStoTime(t) - fromTStoTime(t[0])
    y = np.log(T)

    err_x = np.array([dt] * len(t), dtype=float)
    err_y = dT / T 
    betas = Plots.plotODR(x, y, err_x, err_y)
    err_y[0] *= 1
    Plots.plotPoints(x, y, err_x, err_y)
    Plots.show("Orthogonal Distance Regression with errors, metal Fe", "time: t, s"
               , r"$\ln(T - T_0)$")

    return betas


betas = show(t, T)

print(Student.appr(betas[2], len(T)))