global n


def min_heapify(A: list, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def build_min_heap(A: list):
    global n
    n = len(A) - 1
    for i in range((n // 2), -1, -1):
        min_heapify(A, i)


def heap_enq(A: list, i):
    A.append(i)
    build_min_heap(A)


def heap_deq(A: list):
    global n
    if n < 1:
        return A.pop()
    smallest, A[0] = A[0], A.pop()
    n -= 1
    min_heapify(A, 0)
    return smallest


# for debugging
def is_min_heap(A: list):
    for i in range(0, (len(A) - 1) // 2):
        print(f'{A[i]}, {A[(2 * i) + 1]}, {A[(2 * i) + 2]}')
        if A[i] > A[(2 * i) + 1] or A[i] > A[(2 * i) + 2]:
            return False
    print(f'{A[(len(A) // 2) - 1]}, {A[-1]}')
    if A[(len(A) // 2) - 1] > A[-1]:
        return False
    return True
