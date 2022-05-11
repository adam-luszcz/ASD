def task3(A):
    run = True

    while run:
        run = False
        for i in range(len(A) - 1):
            if A[i + 1] > 0 and A[i] < 0:
                A[i + 1], A[i] = A[i], A[i + 1]
                run = True


if __name__ == '__main__':
    tab = [5, -2, 3, 10, 65, 4, -3, -1, -10, 13]

    task3(tab)
    print(tab)

