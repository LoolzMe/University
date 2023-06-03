import scipy.misc as misc
import numpy as np

def partial_derivative(func, var=0, point=[]):
    args = point[:]

    def wraps(x):
        args[var] = x
        return func(*args)

    return misc.derivative(wraps, point[var], dx = 1e-6)

def errorFunc(func, args=[], error_args=[]):
    sum = 0

    for i in range(len(args)):
        sum += (partial_derivative(func, i, args) ** 2) * (error_args[i] ** 2)


    return np.sqrt(sum)

# print output of the func and its statistical error 
def printProp(func, args=[], error_args=[]):
    mean = func(*args)
    error = errorFunc(func=func, args=args, error_args=error_args)
    
    print(func.__name__)
    print("mean: ", mean)
    print("error: ", error)