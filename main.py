import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (x*x + y - 11)**2 + (x + y*y - 7)**2      # Himmelblau function
    # return (1-x)**2 + 100*(y-x*x)**2             # Rosenbrock function


n = 101
x = np.linspace(-6, 6, n)   #  scale for
y = np.linspace(-6, 6, n)   #  Himmelblau function
# x = np.linspace(-6, 6, n)   #  scale for
# y = np.linspace(-6, 6, n)   #  Rosenbrock function
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots()

ax.contour(X, Y, Z, 60)  # the last argument is responsible for the number of level сurves

fig.set_figwidth(6)  # image width
fig.set_figheight(6)  # and height

plt.show()

# you can use this code for any function f(x,y) with any scale
