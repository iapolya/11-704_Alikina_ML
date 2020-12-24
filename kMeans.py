import matplotlib.pyplot as plt
import numpy as np
import random

def calculate_distance(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def dots_to_clusters(x, y, x_cc, y_cc, k, n):
    cluster = []
    for i in range(0, n - 1):
        d = calculate_distance(x[i], y[i], x_cc[0], y_cc[0])
        numb = 0
        for j in range(0, k):
            if calculate_distance(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = calculate_distance(x[i], y[i], x_cc[j], y_cc[j])
                numb = j
        cluster.append(numb)
    return cluster


def calculate_k_means(x, y, x_cc, y_cc, k, n):
    is_final = False

    while is_final is False:

        clusters = dots_to_clusters(x, y, x_cc, y_cc, k, n)

        new_x_cc = []
        new_y_cc = []

        for i in range(0, k):

            summed_x = 0
            summed_y = 0
            counter = 0

            for j in range(0, n - 1):
                if i == clusters[j]:
                    summed_x += x[j]
                    summed_y += y[j]
                    counter += 1

            if counter > 0:
                new_x_cc.append(summed_x / counter)
                new_y_cc.append(summed_y / counter)
            else:
                new_x_cc.append(x_cc[i])
                new_y_cc.append(y_cc[i])

        is_final = (x_cc == new_x_cc) & (y_cc == new_y_cc)
        x_cc = new_x_cc
        y_cc = new_y_cc
    return x_cc, y_cc


def visualize(x, y, clusters_for_dots, x_cc, y_cc, k, n):
    colors = ["red", "green", "blue", "purple", "pink", "yellow", "gray", "orange", "salmon", "peru", "linen", "fuchsia"]
    for i in range(0, n - 1):
        plt.scatter(x[i], y[i], color=colors[clusters_for_dots[i]])

    for i in range(0, k):
        plt.scatter(x_cc[i], y_cc[i], color='black')
    plt.show()


def calculate_distance_for_all_dots(x, y, x_cc, y_cc, dots_with_clusters):
    sum = 0
    for i in (0, len(dots_with_clusters) - 1):
        x_cc_dot = x_cc[dots_with_clusters[i]]
        y_cc_dot = y_cc[dots_with_clusters[i]]
        sum += calculate_distance(x[i], y[i], x_cc_dot, y_cc_dot)
    return sum


def generate_centers(k, x_c, y_c, R):
    x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    y_cc = [R * np.sin(2 * np.pi * i / k) + y_c for i in range(k)]
    return x_cc, y_cc


def calculate_optimal_clusters(k, n, precise, x, y, x_c, y_c, R):
    distance_k_minus_1 = 0
    is_optimal = True
    x_cc_calc, y_cc_calc = generate_centers(k, x_c, y_c, R)
    dots_with_clusters = dots_to_clusters(x, y, x_cc_calc, y_cc_calc, k, n)
    distance_k = calculate_distance_for_all_dots(x, y, x_cc_calc, y_cc_calc, dots_with_clusters)
    while is_optimal:
        x_cc_calc, y_cc_calc = calculate_k_means(x, y, x_cc_calc, y_cc_calc, k, n)
        dots_with_clusters = dots_to_clusters(x, y, x_cc_calc, y_cc_calc, k, n)
        distance_k_plus_1 = calculate_distance_for_all_dots(x, y, x_cc_calc, y_cc_calc, dots_with_clusters)
        diff = abs(distance_k - distance_k_plus_1) / abs(distance_k_minus_1 - distance_k)
        distance_between = diff * diff
        is_optimal = distance_between >= precise
        distance_k_minus_1 = distance_k
        distance_k = distance_k_plus_1
        if is_optimal:
            k += 1
            x_cc_calc, y_cc_calc = generate_centers(k, x_c, y_c, R)
    return x_cc_calc, y_cc_calc, k


def execute(n, k, min_value, max_value, presize):
    x = [random.randint(min_value, max_value) for i in range(n)]
    y = [random.randint(min_value, max_value) for i in range(n)]

    x_c = np.mean(x)
    y_c = np.mean(y)

    R = 0
    for i in range(0, n):
        r = calculate_distance(x_c, y_c, x[i], y[i])
        if r > R:
            R = r

    final_x_cc, final_y_cc, k = calculate_optimal_clusters(k, n, precise, x, y, x_c, y_c, R)
    final_clusters = dots_to_clusters(x, y, final_x_cc, final_y_cc, k, n)
    return x, y, final_clusters, final_x_cc, final_y_cc, k


n, k, precise = 200, 2, 0.05
x, y, final_clusters, final_x_cc, final_y_cc, k = execute(n, k, 1, 200, precise)
