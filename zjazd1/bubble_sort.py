def bubble_sort(A):
    changed = True
    while changed:
        changed = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                changed = True
    return A
