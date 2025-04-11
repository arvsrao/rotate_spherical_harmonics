from generate_s03_representation import *
import matplotlib.pyplot as plt
import numpy as np

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
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
f = x * y
ax.plot_surface(f * x, f * y, f * z, cmap=cm.plasma)

# Set an equal aspect ratio
ax.set_aspect('auto')

# ==============
# Rotated version of f
# ==============
ax = fig.add_subplot(1, 2, 2, projection='3d')

A, axis = generateSO3()
rho2 = representationOfSO3(A,2)

# plot the axis arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
axis_samples = np.linspace(-2, 2, 100)

ax.plot(axis_samples * axis[0], 
	axis_samples * axis[1], 
	axis_samples * axis[2], color='r', label='rotation axis')
ax.legend()

[x * x, x * y, y * y, x * z, y * z, z * z]
g = -0.5 * x * x + 0.5 * y * y
ax.plot_surface(g * x, g * y, g * z, cmap=cm.plasma)

# Set an equal aspect ratio
ax.set_aspect('auto')

plt.show()