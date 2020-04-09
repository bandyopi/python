import matplotlib.pyplot as plt
import numpy as np

radius, modulo, multiplier = 1, 360, 13
ax = plt.gcf().gca()
ax.set_aspect('equal')
ax.add_artist(plt.Circle((0, 0), radius, edgecolor='r', facecolor='w'))
plt.xlim(-radius-0.1, radius+0.1)
plt.ylim(-radius-0.1, radius+0.1)
x_points, y_points = [], []
for i in range(modulo):
    theta = i*360.0/modulo
    x_points.append(radius*np.cos(theta*np.pi/180))
    y_points.append(radius*np.sin(theta*np.pi/180))
for j in range(modulo):
    ax.add_artist(plt.Line2D((x_points[j], x_points[j*multiplier % modulo]),
                             (y_points[j], y_points[j*multiplier % modulo]),
                             color='r', linewidth=0.25))
plt.show()
