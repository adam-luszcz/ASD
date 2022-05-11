def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    tab = [7, 13, 24, 1, 5, 18, 9]
    tab2 = [5, 12, 21, 7, 5, 5, 13, 4, 2, 12, 13]

    merge_sort(tab)
    merge_sort(tab2)
    print(tab)
    print(tab2)