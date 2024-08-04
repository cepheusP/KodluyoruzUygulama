import math
points = [(0, 0), (3, 4), (5, 12), (2, 2)]
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        distances.append(dist)
min_distance = min(distances)
print(min_distance)
