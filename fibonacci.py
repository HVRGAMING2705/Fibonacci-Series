"""Fibonacci Algorithms Lab — five ways to compute F(n), from the
textbook recursion to O(log n) matrix exponentiation.
"""
import math
from functools import lru_cache


def fib_naive(n):
    """Classic tree recursion. O(phi^n) time — the canonical example of
    why naive recursion can be catastrophic. Only usable for small n."""
    _check(n)
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def _check(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")


@lru_cache(maxsize=None)
def _fib_memo(n):
    return n if n < 2 else _fib_memo(n - 1) + _fib_memo(n - 2)


_fib_cache = {0: 0, 1: 1}


def fib_memoized(n):
    """Top-down DP with memoization. O(n) time.

    Iterative over an explicit cache so CPython's recursion limit does
    not cap n (a recursive lru_cache version dies past n ~ 1000).
    """
    _check(n)
    if n in _fib_cache:
        return _fib_cache[n]
    start = max(k for k in _fib_cache if k <= n)
    for i in range(start + 1, n + 1):
        _fib_cache[i] = _fib_cache[i - 1] + _fib_cache[i - 2]
    return _fib_cache[n]


def fib_iterative(n):
    """Bottom-up loop. O(n) time, O(1) space. The practical default."""
    _check(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _mat_mul(a, b):
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def _mat_pow(m, n):
    result = ((1, 0), (0, 1))
    while n:
        if n & 1:
            result = _mat_mul(result, m)
        m = _mat_mul(m, m)
        n >>= 1
    return result


def fib_matrix(n):
    """Matrix exponentiation: [[1,1],[1,0]]^n = [[F(n+1),F(n)],[F(n),F(n-1)]].
    O(log n) matrix multiplications — exact for arbitrarily large n."""
    _check(n)
    if n == 0:
        return 0
    return _mat_pow(((1, 1), (1, 0)), n - 1)[0][0]


_PHI = (1 + math.sqrt(5)) / 2
_PSI = (1 - math.sqrt(5)) / 2


def fib_binet(n):
    """Binet's closed form: (phi^n - psi^n) / sqrt(5).

    O(1), but float64 precision breaks it past n ~ 70. Included to
    demonstrate the exactness/performance trade-off of closed forms."""
    _check(n)
    return round((_PHI ** n - _PSI ** n) / math.sqrt(5))


def fib(n, method="iterative"):
    methods = {
        "naive": fib_naive,
        "memoized": fib_memoized,
        "iterative": fib_iterative,
        "matrix": fib_matrix,
        "binet": fib_binet,
    }
    if method not in methods:
        raise ValueError(f"unknown method {method!r}")
    return methods[method](n)


def golden_ratio_approximations(terms=20):
    """F(n+1)/F(n) converging to phi — the golden ratio."""
    return [fib_iterative(n + 1) / fib_iterative(n) for n in range(2, terms + 1)]
