import matplotlib.pyplot as plt
import numpy as np

n = 500
eps, minPts = 40, 3
x = [np.random.randint(1, 100) for i in range(n)]
y = [np.random.randint(1, 100) for i in range(n)]
flags = []


def points_distance(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

def isNeighb(i, j):
    return points_distance(x[i], y[i], x[j], y[j]) <= eps & i != j

for i in range(n):
    neighb = 0
    for j in range(n):
        if isNeighb(i, j):
            neighb += 1
    if neighb >= minPts:
        flags.append('g')
    else:
        # точка-отшельник
        flags.append('r')

for i in range(n):
    if flags[i] == 'r':
        for j in range(n):
            if flags[j] == 'g':
                if isNeighb(i, j):
                    # выброс-одиночка
                    flags[i] = 'y'

for i in range(n):
    plt.scatter(x[i], y[i], color=flags[i])

plt.show()
