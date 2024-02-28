import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import linalg, optimize, special

"""
Matplotlib is an open-source library for plotting data. Example 1: simple plot of a sinusoidal function.
"""
# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1, y2 = np.sin(x), np.cos(x)
 
# fig, axes = plt.subplots()
# axes.plot(x, y1, label='Sin(x)', color='b')
# axes.plot(x, y2, label='Cos(x)', color='r', linestyle='--')

# plt.legend()
# plt.show()

# # Plotting multiple lines on a single plot
plt.plot(x, y1, label='Sin(x)', color='b')
plt.plot(x, y2, label='Cos(x)', color='r', linestyle='--')
 
# # Adding labels and title
plt.xlabel('X - 0~2pi')
plt.ylabel('Y - sin/cos')
plt.title('Multiple Lines Plot')
 
# # Displaying the legend and the plot
plt.legend()
plt.show()



"""
example 2: Plotting the Bessel function of a given order and wavenumber.
Bessel functions are a family of solutions to Bessel’s differential equation with real or complex order.
Among other uses, these functions arise in wave propagation problems.

"""
# kth_zero = special.jn_zeros(3, 4)
# print(np.round(kth_zero, decimals=4))
# np.set_printoptions(precision=4)  
# print(f'{kth_zero} {type(kth_zero)} {kth_zero[-1]}')

j3_roots = special.jn_zeros(3, 4)
xmax = 18
xmin = -1
x = np.linspace(xmin, xmax, 500)
y = special.jn(3, x)

fig, ax = plt.subplots()
ax.plot(x, y, label=r'$J_3$')
ax.scatter(j3_roots, np.zeros((4, )), s=30, c='r',
           label=r"$J_3$_Zeros", zorder=5)
ax.scatter(0, 0, s=30, c='k',
           label=r"Root at 0", zorder=5)
ax.hlines(0, 0, xmax, color='k')
ax.set_xlim(xmin, xmax)
plt.legend()
plt.show()


"""Example 3: A rectangular step function on [0, 1] and Ramp function on [-1, 1]:
"""
def step(x):
    return 0.5*(np.sign(x) + np.sign(1 - x))
def ramp(x):
    return np.maximum(0, x)

x = np.linspace(-6, 6, 100)
y1 = step(x)
y2 = ramp(x)
plt.plot(x, y1, label='Step Func', color='g')
plt.plot(x, y2, label='Ramp Func', color='r')

# # Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Step and Ramp Function Plot')
 
# # Displaying the legend and the plot
plt.legend()
plt.show()



"""
example 4 TBC: an example of a circular drum head anchored at the edge

Define a function that calculates the Bessel function, which is a solution to Bessel's differential equation. 
The function takes five arguments: n, k, distance, angle, and t.
n: The order of the Bessel function.
k: The wavenumber, or the number of waves per unit length.
distance: The distance from the edge of the drum head to the point where the function is being evaluated.
angle: The angle between the normal to the drum head and the direction of propagation of the wave.
J_n(k*r) = C * cos(n*θ) * jn(n, k*r)
"""

def drum_height_bessel_eq(n: int, 
                          k: float, 
                          distance: float, 
                          angle: float, 
                          t: float) -> float:
    """
    Calculates the Bessel function for a given set of parameters.

    Args:
        n (int): The order of the Bessel function.
        k (float): The wavenumber, or the number of waves per unit length.
        distance (float): The distance from the edge of the drum head to the point where the function is being evaluated.
        angle (float): The angle between the normal to the drum head and the direction of propagation of the wave.
        t (float): The time.

    Returns:
        float: The value of the Bessel function at the given point.

    """
    #calculates the kth zero of the Bessel function using the special.jn_zeros function from SciPy
    #This returns an array of zeros, and the last element of the array is taken as the kth zero.
    kth_zero = special.jn_zeros(n, k)[-1]
    return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)

theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drum_height_bessel_eq(1, 1, r, theta, 0.5) for r in radius])

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes(rect=(0, 0.05, 0.95, 0.95), projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='RdBu_r', vmin=-0.5, vmax=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xticks(np.arange(-1, 1.1, 0.5))
ax.set_yticks(np.arange(-1, 1.1, 0.5))
ax.set_zlabel('Z')
plt.show()

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

#which you would then use twice to populate two subplots:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
plt.show()