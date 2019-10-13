import random
import time


def binary_search(arr, x):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = lower + (upper - lower) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lower = mid + 1
        elif arr[mid] > x:
            upper = mid - 1


def binary_test_1(n, m, t):  # for first few tests
    start_time = time.time()
    for k in range(t):
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
            l1.sort()
        x = random.choice(l1)
        binary_search(l1, x)
    return (time.time() - start_time)


def binary_test_2(n, m, t):  # for unit run time tests
    start_time = time.time()
    for k in range(t):
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
            l1.sort()
        x = random.choice(l1)
        binary_search(l1, x)
    return ((time.time() - start_time) / t) * 1000


def binary_test_3(n, m, t):  # for finding best worst and average
    for k in range(t):
        start_time = time.time()
        l1 = []
        for i in range(n):
            element = random.randint(0, m)
            l1.append(element)
            l1.sort()
        x = random.choice(l1)
        binary_search(l1, x)
        return time.time() - start_time


def main(): # All experiments
    print(binary_test_1(1000, 100, 1000))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(1000, 10000, 1000))
    print(binary_test_1(1000, 100000, 1000))

    """print(binary_test_1(10, 1000, 1000))
    print(binary_test_1(100, 1000, 1000))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(10000, 1000, 1000))

    print(binary_test_1(1000, 1000, 100))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(1000, 1000, 10000))
    print(binary_test_1(1000, 1000, 100000))

    print(binary_test_1(10, 1000, 1000))
    print(binary_test_1(100, 1000, 1000))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(10000, 1000, 1000))

    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(1000, 1000, 1000))
    print(binary_test_1(1000, 1000, 1000))

    print(binary_test_3(10000, 100000, 1000))"""


if __name__ == '__main__':
    main()
