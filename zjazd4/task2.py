if __name__ == '__main__':
    tab = [1, 2, 3, 4, 5, 6, 7, 8]
    if len(tab) % 2 == 0:
        x = len(tab)
    else:
        x = len(tab) - 1

    for i in range(0, x, 2):
        tab[i], tab[i+1] = tab[i+1], tab[i]

    print(tab)