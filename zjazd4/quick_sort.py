# Metoda lomuto
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    tab = [7, 13, 24, 1, 5, 18, 9]
    tab2 = [5, 12, 21, 7, 5, 5, 13, 4, 2, 12, 13]

    quick_sort(tab, 0, len(tab) - 1)
    print(tab)

    quick_sort(tab2, 0, len(tab2) - 1)
    print(tab2)
