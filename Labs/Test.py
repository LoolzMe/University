# import numpy as np
# import matplotlib.pyplot as plt
# from numpy.polynomial.polynomial import polyfit 
# import pandas as pd
# import seaborn; seaborn.set()

# rand = np.random.RandomState(42)

# mean = [0, 0]
# cov = np.array([[6, -3], [-3, 3.5]])


# rand_values = rand.multivariate_normal(mean, cov, 800)
# c, b, a = polyfit(rand_values.T[0, :], rand_values.T[1, :], 2)
# #print(c, b, a)

# # plt.scatter(x[:, 0], x[:, 1])
# # plt.scatter()

# df = pd.DataFrame(rand_values, columns= ["x", "y"])
# print(df)
# seaborn.lmplot(x= "x", y = "y", data = df, errorbar="sd")
# plt.show()


# import numpy as np
# from typing import Tuple, List

# Bin = Tuple[float, float, int]

# def combine(a: Bin, b: Bin) -> Bin:
#     a_avg, a_err, n_a = a
#     b_avg, b_err, n_b = b
#     n = n_a + n_b

#     s_avg = ((n_a / n) * a_avg) + ((n_b / n) * b_avg)

#     N = n ** 2 - n
#     N_a = n_a ** 2 - n_a
#     N_b = n_b ** 2 - n_b

#     s_err = np.sqrt((N_a / N) * (a_err ** 2)
#              + (N_b / N) * (b_err ** 2)
#              + (n_a * n_b * (a_avg - b_avg) ** 2) / (n * N)
#              )

#     return (s_avg, s_err, n)


# print(combine((0.0, 0, 0), (0.0026600999663767455, 0.00011450134919481897, 1)))




import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the range of x-values
x = np.linspace(0, 10, 100)

# Define the mean values of a and b
mean_a = 2.0
mean_b = 10.0

# Define the standard deviations of a and b
std_a = 0.5
std_b = 0.3

# Calculate the y-values using the mean values of a and b
y_mean = mean_a * x + mean_b

# Randomly sampl
# e values of a and b
num_samples = 10
a_samples = np.random.normal(mean_a, std_a, num_samples)
b_samples = np.random.normal(mean_b, std_b, num_samples)

# Calculate the y-values for each sampled pair of a and b
y_samples = np.outer(a_samples, x) + b_samples[:, np.newaxis]

# Calculate the upper and lower bounds of the error band
y_upper = np.max(y_samples, axis=0)
y_lower = np.min(y_samples, axis=0)

# Plot the line with error band
sns.set(style='darkgrid')
plt.plot(x, y_mean, color='blue', label='Mean Line')
plt.fill_between(x, y_lower, y_upper, color='lightblue', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot with Error Band')
plt.legend()
plt.show()