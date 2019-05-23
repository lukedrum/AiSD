from pathlib import Path


def naive_ser(table, pattern):
    """
      Basic, naive function which search for pattern in given table
      :param table: Matrix to search for pattern
      :param pattern: Pattern
      :return: Number of pattern occurrences in given table
      """
    lenght = len(table)
    ct = 0
    for line in table:
        i = table.index(line)
        if i < lenght - 2:
            n = len(line)
            m = len(pattern[0])
            for element in range(n - m):  # shifting through the line searching for the first element of the pattern
                for pos in range(m):  # after finding the pattern it shifts through the pattern
                    if pattern[0][pos] != line[element + pos]:
                        break
                    if pos == m - 1:
                        if pattern[1][0] == table[i + 1][element]:
                            if pattern[2][0] == table[i + 2][element]:
                                ct += 1
                                # print("This pattern appears in " + str(i+1), end=' ')
                                # print("line and is shifted " + str(s) + " positions from the beginning.")
    print("Pattern appears " + str(ct) + " times in this matrix.")
    # return ct


values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def basic_hash(a, b, c):
    """
    Hash function
    :param a: first element
    :param b: second element
    :param c: third element
    :return: hash value for given values
    """
    h = 0
    h = values[c] + 16 * values[b] + (16 ** 2) * values[a]
    h = h % 5000
    return h


def prev_next_hash(h, prv, nxt):
    """
    modyfication of hash function to use previous and next value from given table
    :param h: current hash value
    :param prv: previous element of givenm table
    :param nxt: next element of given table
    :return: hash value
    """
    hc = (h - ((16 ** 2 % 5000) * values[prv])) % 5000
    hc = (hc * 16) % 5000
    hc = (hc + values[nxt]) % 5000
    return hc


def hash_ser(table, pattern):
    """
    Function which search for pattern in given table using hash function
    :param table: Matrix to search for pattern
    :param pattern: Pattern
    :return: Number of pattern occurrences in given table
    """
    patt = basic_hash(pattern[0][0], pattern[0][1], pattern[0][2])
    # print(patt)
    ct = 0
    for line in table:
        t = None
        i = table.index(line)
        if i < len(table) - 2:
            for x in range(len(line) - 2):
                if t is not None:
                    t = prev_next_hash(t, line[x - 1], line[x + 2])
                else:
                    t = basic_hash(line[x], line[x + 1], line[x + 2])
                if t == patt:
                    if pattern[1][0] == table[i + 1][x]:
                        if pattern[2][0] == table[i + 2][x]:
                            ct += 1
    print("Pattern appears " + str(ct) + " times in this matrix.")
    # return ct


def main():
    """
    Main program
    :return: Number of pattern occurrences counted by naive search and hash search function
    """
    matrix_size = input("Type input matrix size(1000, 2000, 3000, 4000, 5000, 8000): ")

    mypath = "./patterns"
    full_path = Path(mypath, "{0}_pattern.txt".format(matrix_size))
    file = open(full_path, 'r')

    table = []
    txt = file.read()
    txt = txt.splitlines()
    for line in txt:
        table.append(line)

    patt = ['ABC',
            'B  ',
            'C  ']
    print("Pattern:", patt)

    print("--NAIVE SEARCH--")
    naive_ser(table, patt)

    print("\n--EFFECTIVE SEARCH--")
    hash_ser(table, patt)

    file.close()


if __name__ == "__main__":
    main()
