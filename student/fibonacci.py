from functools import lru_cache
from numba import jit
import numpy as np

# Gustavo solution: store the values of previously computed Fibonacci numbers
@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.

    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1. This function 
    uses a recursive approach to calculate the Fibonacci number at position n.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.

    Returns:
    int: The nth Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(9)
    34
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# other option, not as fast as storing the values of previously computed Fibonacci numbers
@jit(nopython=True, cache=True)
def fibonacci_numba(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# very slow
def fibonacci_numpy(n):
    if n <= 1:
        return n
    else:
        return np.sum(np.arange(n+1))
    
# n = 35
# print(f"Trying this solution: Fibonacci({n}) = {fibonacci(n)}")
