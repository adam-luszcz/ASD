def max_heapify(A, n, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l <= (n - 1) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= (n - 1) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def heap_sort(A):
    n = len(A)
    for i in range((n - 1) // 2, -1, -1):
        max_heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)
