import numpy as np

lis = 6*[10]
lis.append(9.5)

results = np.array(lis, dtype=float)

mean = np.mean(results)
standard = np.std(results)
Sx = standard / np.sqrt(results.size)


print(mean)

#print(standard)

students = Sx * 2.4

print(students)

error = np.sqrt(students**2 + 0.05**2)
print(error)

print(error/mean)