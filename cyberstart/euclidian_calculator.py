import math

points = [(3.3,0),(2.5,0),(5.7,0),(8.4,0)]
def euclidianDistance( point1 , point2):
    return math.sqrt(((point2[0]-point1[0])**2)+ ((point2[1]-point1[1])**2))

distances = []
for i in range(len(points)):
    for j in range(i+1 , len(points)):
        distance = euclidianDistance(points[i],points[j])
        distances.append(distance)


min_distance=min(distances)
print("distances which calculated: ",distances)
print("minimum distances: ",min_distance)