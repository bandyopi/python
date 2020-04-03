import numpy as np
import matplotlib.pyplot as plt

circle = plt.Circle((1, 1), 1, color='r')
plt.gcf().gca().add_artist(circle)
plt.plot([0, 1, 2, 3], [0, 1, 2, 3])
plt.show()
