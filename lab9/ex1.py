class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def main():
    file = open('./TSP.txt', "r")

    cities = []

    for line in file:
        element = line.split()
        name = int(element[0])
        x = float(element[1])
        y = float(element[2])
        cities.append(City(name, x, y))

    total_distance = 0

    for i in range(len(cities) - 1):
        first_city = cities[i]
        second_city = cities[i + 1]
        distance = ((first_city.x - second_city.x) ** 2 + (first_city.y - second_city.y) ** 2) ** 0.5
        total_distance = total_distance + distance

    print(total_distance)


if __name__ == '__main__':
    main()
