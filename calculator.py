# -----------------------------------------------------------------------------
# calculator.py
# HW6
# Zewei Liu
#cProfile 
#before change, original cProfile result is as following:
# the original total calling time: 1.64 s(calculated by timeit)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    2.029    2.029 <string>:1(<module>)
#         2    1.023    0.512    1.037    0.518 calculator.py:19(multiply)
#         1    0.405    0.405    0.492    0.492 calculator.py:32(sqrt)
#         1    0.000    0.000    2.026    2.026 calculator.py:45(hypotenuse)
#         1    0.492    0.492    0.498    0.498 calculator.py:6(add)
#   1000000    0.081    0.000    0.081    0.000 {math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         4    0.000    0.000    0.000    0.000 {numpy.core.multiarray.zeros}
#      4004    0.024    0.000    0.024    0.000 {range}
#The function multiply, add and sqrt cost most of the time.
#
#line_profiler:
#For the original function:
#Total time: 3.50525 s
# Line #      Hits         Time  Per Hit   % Time  Line Contents
#     67                                           def hypotenuse(x,y):
#     68                                               """
#     69                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
#     70                                               x and y must be two-dimensional arrays of the same shape.
#     71                                               """
#     72         1       884909 884909.0     25.2      xx = multiply(x,x)
#     73         1       937097 937097.0     26.7      yy = multiply(y,y)
#     74         1       900426 900426.0     25.7      zz = add(xx, yy)
#     75         1       782822 782822.0     22.3      return sqrt(zz)
#
# 
# Speedup after change:
#  1.64/0.0119 = 137.81512605042016
# ----------------------------------------------------------------------------- 

import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    return np.add(x,y)


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    return np.multiply(x,y)


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    return np.sqrt(x)

def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)