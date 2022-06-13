def head(A):
    return A[0]


def tail(A):
    return A[1:]


def is_empty(A):
    if len(A) > 0:
        return False
    return True


def reverse_word(A):
    if is_empty(A):
        return -1
    if len(A) == 1:
        return head(A)
    return reverse_word(tail(A)) + head(A)


if __name__ == '__main__':
    print(reverse_word('kot'))