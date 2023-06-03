# import numpy as np

# print(np.sqrt(8 * 8.13 * 288.15 / (np.pi * 29 * 10 ** (-3))))

# print(3 * (18 * 10 ** (-6)) / (1.225 * 453.55))


import numpy as np
from matplotlib import pyplot as plt

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*(x - 1.69e-10)**i
    return y / 1.602

x = np.linspace(0, 3*1.69e-10, 100)
coeffs = [0,0, 19/2, -5.5e10/3]
plt.plot(x, PolyCoefficients(x, coeffs))
plt.xlabel("r, A")
plt.ylabel("W, eB")

plt.show()
