from heap_sort import *
from counting_sort import *
from merge_sort import *
from quick_sort import *
from timeit import timeit
from random import random

if __name__ == "__main__":
    random_arr = [int(random() * 10000 + 1) for _ in range(400000)]
    sorted_arr = [i for i in range(1, 400000)]
    unsorted_arr = [i for i in range(400000, 1, -1)]
    print('QUICK SORT\n')
    print(f'Random array: {timeit(lambda: quick_sort(random_arr, 0, len(random_arr) - 1), number=1)}\n')

    # RecursionError: maximum recursion depth exceeded in comparison
    # print(f'Sorted array: {timeit(lambda: quick_sort(sorted_arr, 0, len(sorted_arr) - 1), number=1)}')
    # print(f'Unsorted array: {timeit(lambda: quick_sort(unsorted_arr, 0, len(unsorted_arr) - 1), number=1)}')

    print('MERGE SORT\n')
    print(f'Random array: {timeit(lambda: merge_sort(random_arr), number=1)}')
    print(f'Sorted array: {timeit(lambda: merge_sort(sorted_arr), number=1)}')
    print(f'Unsorted array: {timeit(lambda: merge_sort(unsorted_arr), number=1)}\n')

    print('HEAP SORT\n')
    print(f'Random array: {timeit(lambda: heap_sort(random_arr), number=1)}')
    print(f'Sorted array: {timeit(lambda: heap_sort(sorted_arr), number=1)}')
    print(f'Unsorted array: {timeit(lambda: heap_sort(unsorted_arr), number=1)}\n')

    print('COUNTING SORT\n')
    print(f'Random array: {timeit(lambda: counting_sort(random_arr), number=1)}')
    print(f'Sorted array: {timeit(lambda: counting_sort(sorted_arr), number=1)}')
    print(f'Unsorted array: {timeit(lambda: counting_sort(unsorted_arr), number=1)}')
