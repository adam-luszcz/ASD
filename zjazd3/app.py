# 1. Sprawdz czy tablica jest poprawnym kopcem
# 2. Zbuduj kopiec w czasie liniowym
# 3. Zwroc k-ty najwiekszy element kopca
# 4. Polacz 2 posortowane listy w jedna takze posortowana w czasie liniowym

def max_heapify(A, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l <= (len(A) - 1) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= (len(A) - 1) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range((len(A) - 1) // 2, -1, -1):
        max_heapify(A, i)


def is_heap(A):
    for i in range(0, (len(A)-1) // 2):
        if A[i] < A[(2 * i) + 1] or A[i] < A[(2 * i) + 2]:
            return False
    return True


def merge_sorted_lists(A, B):
    result = []
    idx_a = 0
    idx_b = 0
    while idx_a < len(A) and idx_b < len(B):
        if A[idx_a] < B[idx_b]:
            result.append(A[idx_a])
            idx_a += 1
        else:
            result.append(B[idx_b])
            idx_b += 1
    return result


def main():
    tab = [50, 9, 8, 7, 2, 1, 7, 4, 4]
    tab2 = [50, 9, 8, 7, 2, 1, 7, 4, 8]
    tab3 = [50, 9, 8, 7, 2, 1, 7, 4, 4, 2]

    a1 = [1, 2, 8, 9, 29, 49]
    a2 = [3, 5, 8, 10]

    a3 = merge_sorted_lists(a1, a2)
    print(a3)


if __name__ == '__main__':
    main()
