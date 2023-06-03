import numpy as np
import Student
from Derivative import printProp, errorFunc

#np.set_printoptions(suppress=True)

def friction(r, n, a, b):
    return r * (a) * np.tan(b) / (4*n)

angles = np.array([2, 3, 4], dtype=float)

angles = angles * np.pi / 180

n30 = np.array([[3, 3, 3, 3, 3], [5, 6, 5, 5, 5], [7, 8, 7, 7, 7]])
n45 = np.array([[4,4,5,5,5], [7,7,8,8,8], [10, 10, 11,11,11]])
n60 = np.array([[7,7,8,8,7], [12,11,13,13,12], [16,17,19,19,17]])

results = np.empty((3,3), dtype=float)

means = np.zeros((3,3), dtype=float)

for i in range(3):
    results[0][i] = angles[i] * np.tan(np.pi / 6) / (4*np.mean(n30[i]))
    results[1][i] = angles[i] / (4*np.mean(n45[i]))
    results[2][i] = angles[i] * np.tan(np.pi / 3) / (4*np.mean(n60[i]))
    means[0][i]   = np.mean(n30[i])
    means[1][i]   = np.mean(n45[i])
    means[2][i]   = np.mean(n60[i])

# print(means)

means_std = np.zeros((3,3), dtype=float)
means_stud = np.zeros((3,3), dtype=float)
friction_values = np.zeros((3, 3), dtype=float)
friction_errors = np.zeros((3, 3), dtype=float)

for i in range(3):
    means_std[0][i] = np.std(n30[i])
    means_std[1][i] = np.std(n45[i])
    means_std[2][i] = np.std(n60[i])
    means_stud[0][i] = Student.student[n30[i].size] * means_std[0][i] / np.sqrt(n30[i].size) 
    means_stud[1][i] = Student.student[n45[i].size] * means_std[1][i] / np.sqrt(n45[i].size)
    means_stud[2][i] = Student.student[n60[i].size] * means_std[2][i] / np.sqrt(n60[i].size)

r = 10 * (0.001)
dr = 0.05 * (0.001)
da = 0.5 * np.pi / 180
db = np.pi / 180
table_b = np.array([np.pi / 6, np.pi / 4, np.pi / 3], dtype=float)


for i in range(3):
    for j in range(3):
        friction_values[j][i] = friction(r, means[j][i], angles[i], table_b[j]) 
        friction_errors[j][i] = errorFunc(friction, [r, means[j][i], angles[i], table_b[j]], [dr, means_stud[j][i], da, db])

#print(results)


#print(means_stud)
print(friction_values)
print('-------------')
print(friction_errors)

print(np.mean(friction_values.reshape(-1)), Student.student[9] * np.sqrt(np.sum(np.power(friction_errors.reshape(-1), 2))) / 9)

# print(results)

# results = results.reshape(-1)

# nu_std = np.std(results)
# nu_stud = Student.student[results.size] * nu_std / np.sqrt(results.size) 



# print(np.mean(results))
# print(nu_std)
# print(nu_stud)