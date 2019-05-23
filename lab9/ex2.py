class miasto:
    def __init__(self, nazwa, x, y):
        self.nazwa = nazwa
        self.x = x
        self.y = y


tekst_file = open('TSP.txt', "r")

miasta = []

for line in tekst_file:
    podzial = line.split()
    nazwa = int(podzial[0])
    x = float(podzial[1])
    y = float(podzial[2])
    miasta.append(miasto(nazwa, x, y))

macierz = [[None for x in range(len(miasta))] for y in range(len(miasta))]

for i in range(len(miasta)):
    for j in range(len(miasta)):
        miasto1 = miasta[i]
        miasto2 = miasta[j]
        droga = ((miasto1.x - miasto2.x) ** 2 + (miasto1.y - miasto2.y) ** 2) ** (0.5)
        if i != j:
            macierz[i][j] = droga
        else:
            macierz[i][j] = float("inf")

odleglosc = 0
obecnyindeks = 0

for i in range(len(miasta) - 1):
    indexofmin = macierz[obecnyindeks].index(min(macierz[obecnyindeks]))
    odleglosc += macierz[obecnyindeks][indexofmin]
    for k in macierz:
        del k[obecnyindeks]
    del macierz[obecnyindeks]
    if obecnyindeks < indexofmin:
        obecnyindeks = indexofmin - 1
    else:
        obecnyindeks = indexofmin

droga = ((miasta[0].x - miasta[obecnyindeks].x) ** 2 + (miasta[0].y - miasta[obecnyindeks].y) ** 2) ** (0.5)
odleglosc += droga

print(odleglosc)




