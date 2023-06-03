import numpy as np
from Derivative import  errorFunc, printProp
import Student
import Plots

T0 = 13

dm = 0.01
cu = 4.52
fe = 3.75
al = 1.32

tg_cu = 0.00758
tg_al = 0.01057
tg_fe = 0.00805


def cap(c1, m1, m2, tg1, tg2):
    return c1 * (m1/m2) * (tg1 / tg2)

printProp(cap, [408, cu, al, tg_cu, tg_al], [0.0, dm, dm, 0.0001, 0.0001])
