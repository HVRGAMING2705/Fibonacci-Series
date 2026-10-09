"""Benchmark all five Fibonacci algorithms."""
import timeit

from fibonacci import fib_naive, fib_memoized, fib_iterative, fib_matrix, fib_binet


def time_best(fn, n, repeats=5):
    return min(timeit.repeat(lambda: fn(n), number=1, repeat=repeats))


def main():
    print("Small n (all methods incl. naive recursion):")
    for n in (10, 20, 30):
        row = {
            "naive": time_best(fib_naive, n),
            "memoized": time_best(fib_memoized, n),
            "iterative": time_best(fib_iterative, n),
            "matrix": time_best(fib_matrix, n),
            "binet": time_best(fib_binet, n),
        }
        print(f"  n={n:>3}: " + "  ".join(f"{k}={v*1000:8.3f}ms" for k, v in row.items()))

    print("\nLarge n (naive excluded — it would never finish):")
    for n in (1_000, 10_000, 100_000):
        row = {
            "memoized": time_best(fib_memoized, n, repeats=3),
            "iterative": time_best(fib_iterative, n, repeats=3),
            "matrix": time_best(fib_matrix, n, repeats=3),
        }
        print(f"  n={n:>7,}: " + "  ".join(f"{k}={v*1000:9.3f}ms" for k, v in row.items()))

    # exactness check
    assert fib_matrix(1000) == fib_iterative(1000) == fib_memoized(1000)
    assert fib_binet(70) == fib_iterative(70)
    print("\nExactness verified: matrix == iterative == memoized at n=1000;")


if __name__ == "__main__":
    main()
