# Complexity notes

Why five algorithms for one sequence? Because Fibonacci is the perfect
specimen for showing how algorithm choice dominates performance.

## The lineup

| Method | Time | Space | Exact? | Notes |
|---|---|---|---|---|
| Naive recursion | O(phi^n) | O(n) stack | yes | ~1.6M calls for n=30; ~2.7B for n=50 |
| Memoized (top-down DP) | O(n) | O(n) | yes | each F(k) computed once |
| Iterative (bottom-up) | O(n) | O(1) | yes | the practical default |
| Matrix exponentiation | O(log n) | O(1) | yes | exact at any n via [[1,1],[1,0]]^n |
| Binet's formula | O(1) | O(1) | only to n~70 | float64 rounding breaks it beyond |

## Key insights

1. **Exponential blowup is real.** `fib_naive(30)` makes about
   2*F(31) - 1 = 2,692,537 calls. Each +5 n costs ~11x more time.
   Run `benchmark.py` and watch the naive column explode.
2. **Memoization converts exponential to linear** by trading space for
   time: every subproblem solved once.
3. **Matrix exponentiation is logarithmic in n**, but each "step" is a
   big-integer multiplication whose cost grows with digit count — so
   wall-clock still grows with n, just far slower.
4. **Closed forms are not free.** Binet looks O(1), but IEEE-754 doubles
   only carry ~15.9 decimal digits; rounding gives the wrong integer
   past n = 70. Exactness has a price.
5. **Ratios converge to phi.** F(n+1)/F(n) -> (1+sqrt(5))/2; see
   `golden_ratio.py`. This is why 61.8% = 1/phi shows up in the
   retracement demo.
