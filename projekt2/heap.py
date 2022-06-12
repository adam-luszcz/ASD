global n


def min_heapify(A: list, i: int):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def build_min_heap(A: list):
    global n
    n = len(A) - 1
    for i in range((n // 2) - 1, -1, -1):
        min_heapify(A, i)


def heap_enq(A: list, i):
    A.append(i)
    build_min_heap(A)


def heap_deq(A: list):
    if n < 1:
        return A.pop()
    smallest, A[0] = A[0], A.pop()
    n -= 1
    min_heapify(A, 0)
    return smallest
