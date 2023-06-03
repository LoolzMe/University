import numpy as np
import Student

l = np.array([1.3089,1.3060,1.3080,1.3080,1.3077,1.3076,1.3078,1.3076,1.3078,1.3079])

std = np.std(l)
stu = Student.student[l.size] * std / np.sqrt(l.size)


print(np.mean(l))
print(np.sqrt(stu**2 + 0.001**2))

