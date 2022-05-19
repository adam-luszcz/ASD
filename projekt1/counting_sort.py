def counting_sort(A):
    a_length = len(A)
    c_length = max(A)

    B = [0 for _ in range(a_length)]
    C = [0 for _ in range(c_length + 1)]

    for i in A:
        C[i] += 1

    for i in range(c_length):
        C[i] += C[i-1]

    for i in range(a_length):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    for i in range(a_length):
        A[i] = B[i]
