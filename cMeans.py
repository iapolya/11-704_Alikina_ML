import numpy as np
import matplotlib.pyplot as plt
import random


def calculate_distance(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def dots_to_clusters(dots_with_probability):
    clusters_result = [0] * n
    for i in range(n):
        best_match = max(dots_with_probability[i])
        for j in range(k):
            if dots_with_probability[i][j] == best_match:
                clusters_result[i] = j
    return clusters_result


def visualize(x, y, clusters_for_dots, x_cc, y_cc):
    colors = ["red", "green", "blue", "purple", "pink", "yellow", "gray", "orange"]
    for i in range(0, n - 1):
        plt.scatter(x[i], y[i], color=colors[clusters_for_dots[i]])

    for i in range(0, k):
        plt.scatter(x_cc[i], y_cc[i], color='black')
    plt.show()


def get_clusters_for_dots_and_probabilities(x, y, dots_with_probability):
    x_cc = np.zeros(k)
    y_cc = np.zeros(k)

    for i in range(k):
        n = 0
        sum_x = 0
        sum_y = 0

        for j in range(len(x)):
            max = 0
            for t in dots_with_probability[j]:
                if t > max:
                    max = t
            if dots_with_probability[j, i] == max:
                n = n + dots_with_probability[j, i] ** extra_weight
                sum_x = sum_x + dots_with_probability[j, i] ** extra_weight * x[j]
                sum_y = sum_y + dots_with_probability[j, i] ** extra_weight * y[j]

        if n != 0:
            x_cc[i] = sum_x / n
            y_cc[i] = sum_y / n
        else:
            x_cc[i] = 0
            y_cc[i] = 0

    return x_cc, y_cc


def calculate_new_probability(n, k, x, y, x_c, y_c):
    matrix = np.zeros((n, k))
    for i in range(n):
        for j in range(k):
            sum = 0
            distance_to_center_j = calculate_distance(x[i], y[i], x_c[j], y_c[j])
            for t in range(k):
                distance_to_center_t = calculate_distance(x[i], y[i], x_c[t], y_c[t])
                sum += (distance_to_center_j / distance_to_center_t) ** (2 / (extra_weight - 1))
            matrix[i, j] = 1 / sum
    return matrix


def is_precised(old_dots_with_probability, dots_with_probability):
    max = 0
    for i in range(n):
        for j in range(k):
            diff = np.abs(dots_with_probability[i, j] - old_dots_with_probability[i, j])
            if diff > max:
                max = diff
    return max < e


def c_means_clustering(dots_with_probability):
    need_to_continue = True
    while need_to_continue:
        x_c, y_c = get_clusters_for_dots_and_probabilities(x, y, dots_with_probability)
        new_matrix = calculate_new_probability(n, k, x, y, x_c, y_c)
        if is_precised(new_matrix, dots_with_probability):
            clusters = dots_to_clusters(new_matrix)
            visualize(x, y, clusters, x_c, y_c)
            need_to_continue = False
        dots_with_probability = new_matrix


n, k, extra_weight, e = 200, 4, 1.5, 0.1

x = [random.randint(1, 50) for i in range(n)]
y = [random.randint(1, 50) for i in range(n)]

dots_with_probability = np.zeros((n, k))
for i in range(n):
    for j in range(k):
        dots_with_probability[i, j] = random.randint(1, 4)

c_means_clustering(dots_with_probability)