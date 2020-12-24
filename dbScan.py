import matplotlib.pyplot as plt
import numpy as np
import random


def calculate_distance(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def calculate_neibours(x, y):
    flags = []

    for i in range(0, n):
        count_neighbours = 0
        for j in range(0, n):
            if calculate_distance(x[i], y[i], x[j], y[j]) <= e:
                count_neighbours += 1
        if count_neighbours > min_neighbours_to_complete:
            flags.append('g')
        else:
            flags.append('black')

    for i in range(0, n):
        if flags[i] == 'black':
            for j in range(0, n):
                if flags[j] == 'g':
                    if calculate_distance(x[i], y[i], x[j], y[j]) <= e:
                        flags[i] = 'y'

    cluster = [0] * n

    c = 1
    for i in range(0, n):
        if flags[i] == 'g':
            for j in range(0, n):
                if calculate_distance(x[i], y[i], x[j], y[j]) <= e:
                    if flags[j] == 'g':
                        if cluster[i] == 0 and cluster[j] == 0:
                            cluster[i] = c
                            cluster[j] = c
                            c += 1
                        elif cluster[i] == 0 and cluster[j] != 0:
                            cluster[i] = cluster[j]
                        elif cluster[j] == 0 and cluster[i] != 0:
                            cluster[j] = cluster[i]
                        elif cluster[i] != 0 and cluster[j] != 0:
                            if cluster[i] < cluster[j]:
                                cluster[j] = cluster[i]
                            else:
                                cluster[i] = cluster[j]
                    elif flags[j] == 'y':
                        if cluster[i] == 0:
                            cluster[i] = c
                            c += 1

        if flags[i] == 'y':
            for j in range(0, n):
                if flags[j] == 'g':
                    if calculate_distance(x[i], y[i], x[j], y[j]) <= e and cluster[j] != 0:
                        cluster[i] = cluster[j]

    for i in range(n):
        for j in range(len(colors)):
            if cluster[i] == j:
                color_list[i] = colors[j]

    cluster.sort()
    print(cluster)

    for i in range(0, n):
        plt.scatter(x[i], y[i], color=flags[i])
    plt.show()

    for i in range(0, n):
        plt.scatter(x[i], y[i], color=color_list[i])
    plt.show()


n = 100
e, min_neighbours_to_complete = 5, 3
color_list = []
for i in range(n):
    color_list.append('pink')

colors = ["red", "green", "blue", "purple", "pink", "yellow", "gray", "orange", "salmon", "peru", "linen", "fuchsia"]

x = [random.randint(1, 50) for i in range(n)]
y = [random.randint(1, 50) for i in range(n)]

calculate_neibours(x, y)
