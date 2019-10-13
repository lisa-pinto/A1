import random
import time


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]
        merge_sort(left_side)
        merge_sort(right_side)
        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                l1[k] = left_side[i]
                i += 1
            else:
                l1[k] = right_side[j]
                j += 1
            k += 1
        while i < len(left_side):
            l1[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            l1[k] = right_side[j]
            j += 1
            k += 1


def merge_test_1(n, m, t):  # for first few tests
    start_time = time.time()
    for k in range(t):
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
        merge_sort(l1)
    return time.time() - start_time


def merge_test_2(n, m, t):  # for unit run time tests
    start_time = time.time()
    for k in range(t):
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
        merge_sort(l1)
    return (((time.time() - start_time)) / t) * 1000


def merge_test_3(n, m, t):  # for finding best worst and average
    for k in range(t):
        start_time = time.time()
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
        merge_sort(l1)
        return time.time() - start_time


def main():  # All experiments
    print(merge_test_1(1000, 100, 1000))
    print(merge_test_1(1000, 1000, 1000))
    print(merge_test_1(1000, 10000, 1000))
    print(merge_test_1(1000, 100000, 1000))

   """print(merge_test_1(100, 10000, 1000))
    print(merge_test_1(1000, 10000, 1000))
    print(merge_test_1(10000, 10000, 1000))
    print(merge_test_1(100000, 10000, 1000))

    print(merge_test_1(1000, 10000, 100))
    print(merge_test_1(1000, 10000, 1000))
    print(merge_test_1(1000, 10000, 10000))
    print(merge_test_1(1000, 10000, 100000))

    print(merge_test_2(100, 10000, 1000))
    print(merge_test_2(1000, 10000, 1000))
    print(merge_test_2(10000, 10000, 1000))
    print(merge_test_2(100000, 10000, 1000))

    print(merge_test_2(10000, 100000, 1000))"""


if __name__ == '__main__':
    main()
