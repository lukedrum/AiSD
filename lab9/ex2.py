class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


file = open('TSP.txt', "r")

cities = []

for line in file:
    element = line.split()
    name = int(element[0])
    x = float(element[1])
    y = float(element[2])
    cities.append(City(name, x, y))

matrix = [[None for x in range(len(cities))] for y in range(len(cities))]

for i in range(len(cities)):
    for j in range(len(cities)):
        first_city = cities[i]
        second_city = cities[j]
        distance = ((first_city.x - second_city.x) ** 2 + (first_city.y - second_city.y) ** 2) ** 0.5
        if i != j:
            matrix[i][j] = distance
        else:
            matrix[i][j] = float("inf")

total_distance = 0
current_index = 0

for i in range(len(cities) - 1):
    min_index = matrix[current_index].index(min(matrix[current_index]))
    total_distance += matrix[current_index][min_index]
    for k in matrix:
        del k[current_index]
    del matrix[current_index]
    if current_index < min_index:
        current_index = min_index - 1
    else:
        current_index = min_index

distance = ((cities[0].x - cities[current_index].x) ** 2 + (cities[0].y - cities[current_index].y) ** 2) ** 0.5
total_distance += distance

print(total_distance)
