import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# set up a figure twice as wide as it is tall
fig = plt.figure()
ax = plt.figure().add_subplot(projection='3d')

# ==============
# define degree n homogenous polynomial in the basis of P_n
# and sample it.
#
# Ex. xyz or xy 
# ==============

# sample S^2
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

f = x * y * z
# Plot the surface
ax.plot_surface(f * x, f * y, f * z, cmap=cm.plasma)

# Set an equal aspect ratio
ax.set_aspect('auto')

plt.show()