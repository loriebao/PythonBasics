import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import linalg, optimize, special

#Bessel functions are a family of solutions to Bessel’s differential equation with real or complex order alpha:
#Among other uses, these functions arise in wave propagation problems, such as the vibrational modes of a thin drum head.
#Here is an example of a circular drum head anchored at the edge:

"""
The selected code is a function that calculates the Bessel function, which is a solution to Bessel's differential equation. 
The function takes five arguments: n, k, distance, angle, and t.
n: The order of the Bessel function.
k: The wavenumber, or the number of waves per unit length.
distance: The distance from the edge of the drum head to the point where the function is being evaluated.
angle: The angle between the normal to the drum head and the direction of propagation of the wave.
J_n(k*r) = C * cos(n*θ) * jn(n, k*r)
"""

def bessel_eq(n: int, k: float, distance: float, angle: float, t: float) -> float:
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
    print(kth_zero)
    return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)

kth_zero = special.jn_zeros(2, 5)
print(f'{kth_zero} {type(kth_zero)} {kth_zero[-1]}')

j3_roots = special.jn_zeros(3, 4)
xmax = 18
xmin = -1
x = np.linspace(xmin, xmax, 500)
fig, ax = plt.subplots()
ax.plot(x, special.jn(3, x), label=r'$J_3$')
ax.scatter(j3_roots, np.zeros((4, )), s=30, c='r',
           label=r"$J_3$_Zeros", zorder=5)
ax.scatter(0, 0, s=30, c='k',
           label=r"Root at 0", zorder=5)
ax.hlines(0, 0, xmax, color='k')
ax.set_xlim(xmin, xmax)
plt.legend()
plt.show()