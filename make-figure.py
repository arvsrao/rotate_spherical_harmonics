from generate_s03_representation import *
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

# ==============
# define degree n homogenous polynomial in the basis of P_n
# and sample it.
#
# Ex. xyz or xy 
# ==============
ax = fig.add_subplot(1, 2, 1, projection='3d')

# sample S^2
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

A, axis = generateSO3()
axis_samples = np.linspace(-5, 5, 100)

# plot the axis arrays x, y, z
ax.plot(axis_samples * axis[0], 
	axis_samples * axis[1], 
	axis_samples * axis[2], color='r', label='rotation axis')
ax.legend()

# Plot the surface
f = 10 * x * y
ax.plot_surface(f * x, f * y, f * z, cmap=cm.plasma)

# Set an equal aspect ratio
ax.set_aspect('auto')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# ==============
# Rotated version of f
# ==============
ax = fig.add_subplot(1, 2, 2, projection='3d')

rho2 = representationOfSO3(A,2)
v = Matrix([[0,1,0,0,0,0]]).transpose()
coeff = (rho2 * v).transpose().tolist()[0]
coeff = [float(c) for c in coeff]
basis = [x * x, x * y, y * y, x * z, y * z, z * z]
g = reduce(lambda x,y: x+y, [10 * a * b for a,b in zip(coeff, basis)])

# plot the axis arrays x, y, z
axis_samples = np.linspace(-5, 5, 100)
ax.plot(axis_samples * axis[0], 
	axis_samples * axis[1], 
	axis_samples * axis[2], color='r', label='rotation axis')
ax.legend()

#g = -0.05 * x * x + 0.05 * y * y
ax.plot_surface(g * x, g * y, g * z, cmap=cm.plasma)

# Set an equal aspect ratio
ax.set_aspect('auto')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
