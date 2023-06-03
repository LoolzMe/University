import numpy as np
import Student


ts = [1.972,1.993,1.972,1.970,1.953,1.975]
ts = [2.035,2.027,2.025,2.036,2.031,2.033,2.036]
ts = [2.079,2.070,2.089,2.099,2.088,2.079,2.097]
ts = [1.230,1.246,1.248,1.238,1.227,1.239,1.239]




ts = np.array(ts)

mean = np.mean(ts)

std = np.std(ts)

stu = Student.student[ts.size] * std / np.sqrt(ts.size)


# print(mean)
stu = np.sqrt(stu**2 + 0.001**2)
#print(stu)

m = 414.7
m = 539.5
m = 674.3
m = 156.2

m *= 0.001

r = 5.05 * 0.001
h = 0.295

dr = 0.05 * 0.001
dh = 0.004
dm = 0.1 * 0.001

g = 9.81

I = m * np.power(r, 2) * (g * np.power(mean, 2) /(2*h) - 1)

print(I)

print(np.sqrt((2*m*r*(g*mean**2/(2*h) - 1) * dr)**2 + ((m*r ** 2 * g * mean / (h)) * stu)**2  + (m*r**2 *(g*mean**2/(2*h**2)) * dh)**2 ))

r = np.array([5.05, 43.0, 52.0])
r *= 0.001
m = np.array([32.2, 124, 258.5])
m = np.array([32.2, 124, 383.3])
m = np.array([32.2, 124, 518.1])
m = np.array([32.2, 124, 0])

m *= 0.001

It = 0.5*m[0]*(r[0]) ** 2 + 0.5*m[1]*(r[0] ** 2 + r[1] ** 2) + 0.5*m[2]*(r[1] ** 2 + r[2] ** 2)
print(np.abs(1 - I/It))
#print(1.325657 * 10 ** -4)