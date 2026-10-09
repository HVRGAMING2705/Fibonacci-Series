"""Benchmark: pure-Python loops vs NumPy vectorization, with a timing chart."""
import timeit

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def loop_sum_of_squares(n):
    total = 0.0
    for i in range(n):
        total += i * i
    return total


def numpy_sum_of_squares(n):
    return np.sum(np.arange(n, dtype=float) ** 2)


def loop_matmul(n):
    a = [[float(i + j) for j in range(n)] for i in range(n)]
    b = [[float(i - j) for j in range(n)] for i in range(n)]
    c = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += a[i][k] * b[k][j]
            c[i][j] = s
    return c


def numpy_matmul(n):
    a = np.fromfunction(lambda i, j: i + j, (n, n))
    b = np.fromfunction(lambda i, j: i - j, (n, n))
    return a @ b


def main():
    sizes = [10_000, 100_000, 1_000_000]
    loop_t, np_t = [], []
    for n in sizes:
        lt = timeit.timeit(lambda: loop_sum_of_squares(n), number=3) / 3
        nt = timeit.timeit(lambda: numpy_sum_of_squares(n), number=3) / 3
        loop_t.append(lt)
        np_t.append(nt)
        # correctness
        assert loop_sum_of_squares(1000) == numpy_sum_of_squares(1000)
        print(f"n={n:>9,}: python loop {lt*1000:9.2f} ms | numpy {nt*1000:9.4f} ms | speedup {lt/nt:8.0f}x")

    mat_sizes = [20, 60, 120]
    m_loop, m_np = [], []
    for n in mat_sizes:
        lt = timeit.timeit(lambda: loop_matmul(n), number=1)
        nt = timeit.timeit(lambda: numpy_matmul(n), number=3) / 3
        m_loop.append(lt)
        m_np.append(nt)
        print(f"matmul {n}x{n}: python loop {lt:7.3f} s | numpy {nt*1000:8.3f} ms | speedup {lt/nt:9.0f}x")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    x = range(len(sizes))
    ax1.bar([i - 0.2 for i in x], loop_t, 0.4, label="python loop")
    ax1.bar([i + 0.2 for i in x], np_t, 0.4, label="numpy")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels([f"{s//1000}k" for s in sizes])
    ax1.set_ylabel("seconds")
    ax1.set_title("Sum of squares: loop vs NumPy")
    ax1.legend()

    x2 = range(len(mat_sizes))
    ax2.bar([i - 0.2 for i in x2], m_loop, 0.4, label="python loop")
    ax2.bar([i + 0.2 for i in x2], m_np, 0.4, label="numpy")
    ax2.set_xticks(list(x2))
    ax2.set_xticklabels([f"{s}x{s}" for s in mat_sizes])
    ax2.set_ylabel("seconds")
    ax2.set_title("Matrix multiply: loop vs NumPy")
    ax2.legend()

    plt.tight_layout()
    plt.savefig("benchmark.png", dpi=120)
    print("saved benchmark.png")


if __name__ == "__main__":
    main()
