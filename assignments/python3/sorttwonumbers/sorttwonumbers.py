#! /usr/bin/env python3

import sys


def sort_two_numbers(a, b):
    return sorted([a, b])


def solve():
    data = sys.stdin.readlines()
    a, b = map(int, data[0].split())
    result = sort_two_numbers(a, b)
    print(result[0], result[1])


def test():
    # Basic unit tests
    assert sort_two_numbers(8, 6) == [6, 8]
    assert sort_two_numbers(5, 4) == [4, 5]
    assert sort_two_numbers(15, 12) == [12, 15]

    # Additional unit tests
    assert sort_two_numbers(3, 1) == [1, 3]
    assert sort_two_numbers(100, 200) == [100, 200]
    assert sort_two_numbers(-5, 10) == [-5, 10]

    print('All test cases passed...')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
