import numpy as np
from Derivative import printProp 
import Student

g = 10

def imElastic(m1, m2, a1, a2, l):
    global g
    return 2*np.sqrt(g*l)*m1*np.sin(np.pi * a1 / 360) - 2*np.sqrt(g*l)*m2*np.sin(np.pi * a2 / 360)

def imElastic0(m1, a1, l):
    global g
    return 2*np.sqrt(g*l)*m1*np.sin(np.pi * a1 / 360)

def enElastic(m1, m2, a1, a2, l):
    global g
    return 2*g*l*( m1 * np.sin(np.pi * a1 / 360) ** 2 + m2 * np.sin(np.pi * a2 / 360) ** 2)

def enElastic0(m1, a1, l):
    global g
    return 2*g*l*( m1 * np.sin(np.pi * a1 / 360) ** 2)

def imNonElastic(m1, m2, b, l):
    global g
    return 2*np.sqrt(g*l)*( (m1 + m2) * np.sin(np.pi * b / 360))

def imNonElastic0(m1, b, l):
    global g
    return 2*np.sqrt(g*l)*( (m1) * np.sin(np.pi * b / 360))

def enNonElastic(m1, m2, b, l):
    global g
    return 2*g*l*((m1 + m2) * np.sin(np.pi * b / 360) ** 2)

def enNonElastic0(m1, b, l):
    global g
    return 2*g*l*( (m1) * np.sin(np.pi * b / 360) ** 2)

    


a1 = np.array([11.25,11.50,11.75,11.75,11.25,11.50,11.50,11.50,11.50,11.75], dtype=float)
a2 = np.array([0.5,0.5,0.75,0.75,0.75,0.5,0.5,0.5,0.5,0.75], dtype=float)
b = np.array([7.25,7.38,7.38,7.38,7.5,7.38,7.38], dtype=float)


a1_mean = np.mean(a1)
a2_mean = np.mean(a2)
b_mean  = np.mean(b)

a1_ran = Student.student[a1.size] * np.std(a1) / np.sqrt(a1.size)

a2_ran = Student.student[a2.size] * np.std(a2) / np.sqrt(a2.size)

b_ran = Student.student[b.size] * np.std(b)  / np.sqrt(b.size)

m = np.array([[0.168, 0.1147], [0.039, 0.033]], dtype=float)
#              bigger, smaller, bigger, smaller

l = 0.4875

dm = 0.0001
dl = 0.0025
da = 0.25
da1 = np.sqrt(a1_ran**2 + da ** 2)
da2 = np.sqrt(a2_ran**2 + da ** 2)
db  = np.sqrt(b_ran **2 + da ** 2)

print(a1_mean)
print(a2_mean)
print(b_mean)

print("-------------")

print(a1_ran)
print(a2_ran)
print(b_ran)

print("-------------")

print(da1)
print(da2)
print(db)
print("-------------")


printProp(imElastic, [m[0][0], m[0][1], a1_mean, a2_mean, l], [dm, dm, da1, da2, dl])
printProp(imElastic0, [m[0][1], 15, l], [dm, da, dl])
printProp(imNonElastic, [m[1][0], m[1][1], b_mean, l], [dm, dm, db, dl])
printProp(imNonElastic0, [m[1][1], 15, l], [dm, db, dl])

print("-------------")

printProp(enElastic, [m[0][0], m[0][1], a1_mean, a2_mean, l], [dm, dm, da1, da2, dl])
printProp(enElastic0, [m[0][1], 15, l], [dm, da, dl])
printProp(enNonElastic, [m[1][0], m[1][1], b_mean, l], [dm, dm, db, dl])
printProp(enNonElastic0, [m[1][1], 15, l], [dm, db, dl])


# print(imElastic(m[0][0], m[0][1], a1_mean, a2_mean, l) / errorFunc(imElastic, [m[0][0], m[0][1], a1_mean, a2_mean, l], [dm, dm, da1, da2, dl]))