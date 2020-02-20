# Code by Hatilima
# 16.12.2019
import numpy as np


def finiteDividedDiffCoeffs(x, y):
    # x and y are arrays of data points
    # you can write a small function to enter them one by
    # one or to read them from some file (xls, txt, csv, etc)
    n = len(x)
    x.astype(float)
    y.astype(float)
    F = np.zeros((n, n), dtype=float)
    b = np.zeros(n)

    for i in range(n):
        F[i, 0] = y[i]

    for i in range(1, n):
        for j in range(i, n):
            F[j, i] = float(F[j, i-1]-F[j-1, i-1])/float(x[j]-x[j-i])

    for i in range(n):
        b[i] = F[i, i]

    return np.array(b)


def interpol(b, x, input_value):
    # b is array of coeffs
    # x is array of x data points
    # input_value is the x value whose output is to be interpolated
    x.astype(float)
    n = len(b)-1
    temp = b[n]
    yamba = b[3]
    print(yamba)
    for i in range(n-1, -1, -1):
        temp = temp*(input_value-x[i]) + b[i]

    return temp


# The following code just tests if the interpolation works
x = np.array([5, 6, 9, 11])
y = np.array([12, 13, 14, 16])

b = finiteDividedDiffCoeffs(x, y)
y_interpo = interpol(b, x, 7)
print("X value of 7")
print("Y value is  {}".format(y_interpo))
