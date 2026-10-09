# Fibonacci Algorithms Lab

The original notebook printed a Fibonacci series. This lab implements
**five** algorithms, benchmarks them head-to-head, visualizes golden-ratio
convergence, and applies the math to Fibonacci retracement.

## Algorithms (`fibonacci.py`)

- `fib_naive` — textbook tree recursion, O(phi^n). Kept as a cautionary tale.
- `fib_memoized` — top-down DP, O(n)
- `fib_iterative` — bottom-up loop, O(n) time / O(1) space
- `fib_matrix` — exponentiation of [[1,1],[1,0]], O(log n), exact at any n
- `fib_binet` — closed form, O(1), exact only to n ~ 70 (float precision)

## How to run

```bash
pip install -r requirements.txt   # only matplotlib
python benchmark.py               # timing shootout (small n and large n)
python golden_ratio.py            # writes golden_ratio.png
python retracement.py             # retracement/extension price levels
```

```python
from fibonacci import fib
fib(1000, method="matrix")   # exact, instant
fib(30, method="naive")      # exact, ~1M recursive calls — feel the pain
```

## Files

- `fibonacci.py` — the five implementations + `golden_ratio_approximations`
- `benchmark.py` — `timeit` comparison; verifies exactness across methods
- `golden_ratio.py` — matplotlib plot of F(n+1)/F(n) -> phi
- `retracement.py` — Fibonacci retracement/extension demo (educational,
  not financial advice)
- `complexity.md` — written complexity analysis and key insights

## Sample output

```
Small n (all methods incl. naive recursion):
  n= 30: naive=  154.321ms  memoized=   0.004ms  iterative=   0.003ms  matrix=   0.006ms  binet=   0.001ms
Large n (naive excluded — it would never finish):
  n=100,000: memoized=  42.1ms  iterative=  38.9ms  matrix=   5.2ms
```
