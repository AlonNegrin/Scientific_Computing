#!/usr/bin/env python3

from typing import Iterable, Set
import numpy as np


# Fix

def fix_me(numbers: Iterable[int]) -> Iterable[int]:
    # Return all the even numbers in the parameter numbers.
    results = []
    for num in numbers:
        if num % 2 == 0:
            results.append(num)
    return results


def fix_me_too(numbers: Iterable[int], threshold: int) -> int:
    """
    The function takes an iterable of integers and a threshold.
    The function returns the number of values in numbers that are above the given threshold.
    """
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
        return count


# Implement

# Return the set of numbers that are shared by all sets
def get_shared_items(sets: Iterable[Set[int]]) -> Set[int]:
    shared = None
    for s in sets:
        if shared is None:
            shared = s
        else:
            shared = shared.intersection(s)
    if shared is None:
        shared = set()
    return shared


def get_randoms(divby: int) -> int:
    """
    Return a random number ranged between 1 and 1000 that is divisible by divby.
    Generate numbers using np.random.randint until you get such a number.
    """
    np.random.seed(0)
    n = np.random.randint(1, 1001)
    while n % divby != 0:
        n = np.random.randint(1, 1001)
    return n


def inner_product_r(v1: Iterable[float], v2: Iterable[float]) -> float:
    return sum(i * j for (i, j) in zip(v1, v2))


def inner_product_c(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    return sum(map(lambda i, j: i * complex(j).conjugate(), c1, c2))


v = [2, 5]
w = [6, 2]

print(inner_product_r(v, w))
print(np.dot(v, w))
