def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


def sum3(n):
    if n < 1:
        return n
    if n % 3 == 0:
        return n + sum3(n - 3)
    return sum3(n - 1)


def binary(A, l, r, x):
    if r >= l:
        middle = (l + r) // 2
        if A[middle] == x:
            return middle
        elif A[middle] > x:
            return binary(A, l, middle - 1, x)
        else:
            return binary(A, middle + 1, r, x)
    else:
        return -1


if __name__ == '__main__':
    print(factorial(5))
    print(sum3(8))

    arr = [1, 3, 7, 9, 22, 34]
    print(binary(arr, 0, len(arr) - 1, 34))
