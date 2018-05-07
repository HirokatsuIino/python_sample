import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

points = np.arange(-5, 5, 0.01)

dx, dy = np.meshgrid(points, points)

plt.plot(dx)

print(dx)

