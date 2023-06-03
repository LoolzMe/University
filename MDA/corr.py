import numpy as np
import matplotlib.pyplot as plt
import Student

T = np.array([216.1, 297.3, 357.7, 599, 699, 798.7, 899, 999], dtype=float)
A = np.array([1.0101957167594453, 0.998233054208753, 0.9951907370640377, 0.9928767047276027, 0.9994434330310783, 0.99550322657241, 0.9929647570601301, 0.9892211656690564], dtype=float)
alpha = np.array([1.0088970064945268, 1.0009496442937365, 1.0021522725958103, 0.9960424878874473, 1.0017643924685553, 0.9991769050100527, 0.9948032878667622, 0.9971983252938333], dtype=float)
dump = A ** 2 / alpha ** 3
print(dump)
alpha = alpha
A = A


print("Means:", np.mean(A), np.mean(alpha))
print("Stds:", Student.stud(A), Student.stud(alpha))

# coef_A = np.polyfit(T, A, deg=1)
# coef_alpha = np.polyfit(T, alpha, deg=1)

# Ts = np.linspace(200, 1000)

# pol_A = np.poly1d(coef_A)
# pol_alpha = np.poly1d(coef_alpha)

# plt.subplot(121)

# plt.plot(Ts, pol_A(Ts), label='fit')
# plt.plot(T, A, 'o')
# plt.xlabel("Coeffs: {}".format(coef_A))
# plt.title("A")
# plt.legend()

# plt.subplot(122)

# plt.plot(Ts, pol_alpha(Ts), label='fit')
# plt.plot(T, alpha, 'o')
# plt.xlabel("Coeffs: {}".format(coef_alpha))
# plt.title("alpha")
# plt.legend()


# plt.show()