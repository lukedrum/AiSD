class miasto:
    def __init__(self, nazwa, x, y):
        self.nazwa = nazwa
        self.x = x
        self.y = y


tekst_file = open('./TSP.txt', "r")

miasta = []

for line in tekst_file:
    podzial = line.split()
    nazwa = int(podzial[0])
    x = float(podzial[1])
    y = float(podzial[2])
    miasta.append(miasto(nazwa, x, y))

odleglosc = 0

for i in range(len(miasta) - 1):
    miasto1 = miasta[i]
    miasto2 = miasta[i + 1]
    droga = ((miasto1.x - miasto2.x) ** 2 + (miasto1.y - miasto2.y) ** 2) ** (0.5)
    odleglosc = odleglosc + droga

print(odleglosc)


