import sys
import matplotlib.pyplot as plt
import networkx as nx
import random


def connect_dots_with_minimal_distance(matrix_with_distances, graph):
    minimal_distance = 0
    i_min, j_min = 0, 0

    for i in range(n):
        for j in range(i + 1, n):
            if minimal_distance > matrix_with_distances[i][j]:
                minimal_distance = matrix_with_distances[i][j]
                i_min, j_min = i, j

    graph[i_min][j_min] = minimal_distance
    graph[j_min][i_min] = minimal_distance

    matrix_with_distances[i_min][j_min] = sys.maxsize
    matrix_with_distances[j_min][i_min] = sys.maxsize

    selection = [0] * n
    selection[i_min] = 1
    selection[j_min] = 1
    return selection


def connect_all_in_selection(matrix_with_distances, graph, selection):
    minimal_distance = sys.maxsize
    i_min, j_min = 0, 0

    for i in range(n):
        if selection[i] == 1:
            for j in range(n):
                if selection[j] == 0:
                    if minimal_distance > matrix_with_distances[i][j]:
                        minimal_distance = matrix_with_distances[i][j]
                        i_min, j_min = i, j

    graph[i_min][j_min] = minimal_distance
    graph[j_min][i_min] = minimal_distance

    matrix_with_distances[i_min][j_min] = matrix_with_distances[j_min][i_min] = sys.maxsize
    selection[i_min] = selection[j_min] = 1


def delete_connection(graph):
    maximal_distance = 0
    i_max = j_max = 0
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] > maximal_distance:
                maximal_distance = graph[i][j]
                i_max, j_max = i, j
    graph[i_max][j_max] = graph[j_max][i_max] = 0


n, k = 15, 3

matrix_with_distances = [[0 for i in range(n)] for i in range(n)]
for i in range(0, n):
    for j in range(i + 1, n):
        matrix_with_distances[i][j] = random.randint(1, 100)
        matrix_with_distances[j][i] = matrix_with_distances[i][j]

graph = [[0 for i in range(n)] for j in range(n)]

selection = connect_dots_with_minimal_distance(matrix_with_distances, graph)

while 0 in selection:
    connect_all_in_selection(matrix_with_distances, graph, selection)

for i in range(k - 1):
    delete_connection(graph)

graph_for_drawing = nx.Graph(strict=False)
for i in range(0, n):
    graph_for_drawing.add_node(i)
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 0:
            continue
        graph_for_drawing.add_edge(i, j, weight=graph[i][j])
        graph[i][j] = graph[j][i] = 0
nx.draw_circular(graph_for_drawing, with_labels=True)
pos = nx.circular_layout(graph_for_drawing)
edge_labels = nx.get_edge_attributes(graph_for_drawing, 'weight')
nx.draw_networkx_edge_labels(graph_for_drawing, pos=pos, edge_labels=edge_labels)
plt.show()