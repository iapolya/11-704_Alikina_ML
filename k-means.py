import matplotlib.pyplot as plt
import numpy as np
import random

n, k = 100, 4
x = [random.randint(1, 100) for i in range(n)]
y = [random.randint(1, 100) for i in range(n)]

x_c = np.mean(x)
y_c = np.mean(y)


# расстояние между точками
def points_distance(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


R = 0
for i in range(0, n):
    r = points_distance(x_c, y_c, x[i], y[i])
    if r > R:
        R = r

# инициализируем точки для кластеров
x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
y_cc = [R * np.sin(2 * np.pi * i / k) + x_c for i in range(k)]


# cluster[i] - номер кластера точки под индексом i
def generate_clusters(x, y, x_cc, y_cc):
    cluster = []
    for i in range(n):
        d = points_distance(x[i], y[i], x_cc[0], y_cc[0])
        cluster_num = 0
        for j in range(k):
            if points_distance(x[i], y[i], x_cc[j], y_cc[j]) < d:
                d = points_distance(x[i], y[i], x_cc[j], y_cc[j])
                cluster_num = j
        cluster.append(cluster_num)

    return cluster


def calculate_k_means(x_cc, y_cc):
    while True:
        clusters = generate_clusters(x, y, x_cc, y_cc)
        calc_x_cc = []
        calc_y_cc = []

        for i in range(k):
            x_sum = 0
            y_sum = 0
            count = 0

            for j in range(n):
                if i == clusters[j]:
                    x_sum += x[j]
                    y_sum += y[j]
                    count += 1

            if count > 0:
                calc_x_cc.append(x_sum / count)
                calc_y_cc.append(y_sum / count)
            else:
                calc_x_cc.append(x_cc[i])
                calc_y_cc.append(y_cc[i])

        # как только не сможем улучшать, выходим их цикла
        if (x_cc == calc_x_cc) & (y_cc == calc_y_cc):
            break;

        x_cc = calc_x_cc
        y_cc = calc_y_cc

    return x_cc, y_cc


# наиболее оптимальные центры кластеров
final_x_cc, final_y_cc = calculate_k_means(x_cc, y_cc)
# итоговое разбиение на кластеры
final_clusters = generate_clusters(x, y, final_x_cc, final_y_cc)

for i in range(n):
    colors = ['r', 'b', 'g', 'y']
    plt.scatter(x[i], y[i], color=colors[final_clusters[i]])

for i in range(0, k):
    plt.scatter(final_x_cc[i], final_y_cc[i], color='black')
plt.show()
