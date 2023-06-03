from scipy import odr
from scipy import stats 
import numpy as np
import matplotlib.pyplot as plt

def line(b, x):
    y = b[0] * x + b[1]
    return y

def fitModel(x, y, err_x, err_y):
    linear_model = odr.Model(line)
    collected_data = odr.Data(x, y, wd=1./err_x, we=1./err_y)
    odr_model = odr.ODR(collected_data, linear_model, beta0=[1., 2.])
    output = odr_model.run()
    return output


def plotLinearRegression(x, y):
    linear_regression = stats.linregress(x, y)
    mn=np.min(x)
    mx=np.max(x)
    x1=np.linspace(mn, mx, 500)
    plt.plot(x1, line([linear_regression.slope, linear_regression.intercept], x1), label='Least squares', lw=3, color='green', ls='--')

    print("(LR) standard deviations of slope, intercept:", linear_regression.stderr, linear_regression.intercept_stderr)
    return [linear_regression.slope, linear_regression.intercept, linear_regression.stderr, linear_regression.intercept_stderr]


def plotPoints(x, y, err_x, err_y):
    plt.errorbar(x, y, err_y, err_x, 'o', label="points and their error bars", markersize=5, capsize=2, alpha=0.8)


def plotODR(x, y, err_x, err_y):
    mn=np.min(x)
    mx=np.max(x)
    x1=np.linspace(mn, mx, 500)
    regression = fitModel(x, y, err_x, err_y)
    plt.plot(x1, line(regression.beta, x1), label='ax + b'.format(*regression.beta), lw=3, color='purple', alpha=0.7)
    plt.text(0.81, 0.4, ("$\\alpha$ = {0:.5f}\n $\\beta$ = {1:.5f}\n std_$\\alpha$ = {2:.5f}\n std_$\\beta$ = {3:.5f}\n").format(*regression.beta, *regression.sd_beta), fontsize=11, transform=plt.gcf().transFigure)
    

    print("(ODR) standard deviations of slope, intercept:", regression.sd_beta)
    return [*regression.beta, *regression.sd_beta]


def show(title, xlabel, ylabel):
    plt.legend(loc="upper left")
    plt.subplots_adjust(right=0.8)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.4)
    plt.show()