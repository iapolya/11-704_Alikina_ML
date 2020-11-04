import numpy as np
import matplotlib.pyplot as plt
import random


# Train data generator
def generateData(numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        # Choose random center of 2-dimensional gaussian
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        # Choose numberOfClassEl random nodes with RMS=0.5
        for rowNum in range(numberOfClassEl):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data


def generateRandomPoints(count):
    points = []
    for i in range(count):
        points.append([random.random() * 5.0, random.random() * 5.0])
    return points


def dist(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


n = 16
classes = 4
k = 3
colors = ["red", "green", "blue", "purple"]
# по 16 точек 4 классов
data = generateData(n, classes)
points = generateRandomPoints(5)


# здесь k - количество ближайших соседей
def kNN(points, test, k, numberOfClasses):
    labels = []

    for testPoint in test:
        testDist = [[dist(testPoint, points[i][0]), points[i][1]] for i in range(len(points))]
        stat = [0 for i in range(numberOfClasses)]
        for d in sorted(testDist)[0:k]:
            stat[d[1]] += 1
        labels.append(sorted(zip(stat, range(numberOfClasses)), reverse=True)[0][1])
    return labels


testPointsClasses = kNN(data, points, k, classes)

for idx, pointClass in enumerate(testPointsClasses):
    plt.scatter(points[idx][0], points[idx][1], color=colors[pointClass])

plt.show()