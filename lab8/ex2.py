import time as t
import matplotlib.pyplot as plt
import ex1 as PS

sizes = [1000, 2000, 3000, 4000, 5000, 8000]
naive_times = []
hash_times = []


def main():
    """
    Main program
    :return: Number of pattern occurrences counted by naive search and hash search function
    as well as plot a graph of time against table size
    """
    for n in sizes:
        path = "./patterns/" + str(n) + "_pattern.txt"
        file = open(path, 'r')

        table = []
        txt = file.read()
        txt = txt.splitlines()
        for line in txt:
            table.append(line)

        patt = ['ABC',
                'B  ',
                'C  ']

        print("\n--EFFECTIVE SEARCH--")
        start = t.time()
        PS.hash_ser(table, patt)
        end = t.time()
        hash_times.append(end - start)

        print("\n--NAIVE SEARCH--")
        start = t.time()
        PS.naive_ser(table, patt)
        end = t.time()
        naive_times.append(end - start)

        file.close()

    plt.plot(sizes, naive_times, 'g')
    plt.plot(sizes, hash_times, 'b')
    plt.xlabel("Matrix Size")
    plt.ylabel("Execution Time")
    plt.show()


if __name__ == '__main__':
    main()
