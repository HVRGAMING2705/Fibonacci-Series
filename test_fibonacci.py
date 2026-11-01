"""Tests for the Fibonacci Algorithms Lab. Run: python3 -m unittest test_fibonacci -v

Locks in the Phase 1 QA findings: all exact methods agree, Binet breaks
at n=71, golden-ratio convergence, and retracement math.
"""
import math
import unittest

from fibonacci import (
    fib_naive, fib_memoized, fib_iterative, fib_matrix, fib_binet,
    golden_ratio_approximations, _PHI,
)
from retracement import retracement_levels, extension_levels, LEVELS

# Known values, cross-checked against the closed-form-free iterative method.
KNOWN = {0: 0, 1: 1, 2: 1, 10: 55, 30: 832040,
         100: 354224848179261915075}


class TestExactMethods(unittest.TestCase):
    def test_known_values(self):
        for n, want in KNOWN.items():
            for fn in (fib_memoized, fib_iterative, fib_matrix):
                self.assertEqual(fn(n), want, f"{fn.__name__}({n})")

    def test_all_agree_0_to_100(self):
        for n in range(101):
            want = fib_iterative(n)
            self.assertEqual(fib_memoized(n), want)
            self.assertEqual(fib_matrix(n), want)

    def test_naive_agrees_to_30(self):
        for n in range(31):
            self.assertEqual(fib_naive(n), fib_iterative(n))

    def test_large_n_agreement(self):
        self.assertEqual(fib_matrix(1000), fib_iterative(1000))
        self.assertEqual(fib_memoized(1000), fib_iterative(1000))
        self.assertEqual(len(str(fib_iterative(10000))), 2090)

    def test_invalid_inputs(self):
        for fn in (fib_naive, fib_memoized, fib_iterative, fib_matrix, fib_binet):
            with self.assertRaises(ValueError):
                fn(-1)
            with self.assertRaises(TypeError):
                fn(2.5)


class TestBinet(unittest.TestCase):
    def test_exact_through_70_then_breaks(self):
        for n in range(71):
            self.assertEqual(fib_binet(n), fib_iterative(n))
        self.assertNotEqual(fib_binet(71), fib_iterative(71))


class TestGoldenRatio(unittest.TestCase):
    def test_convergence(self):
        ratios = golden_ratio_approximations(25)
        self.assertEqual(len(ratios), 24)  # n = 2..25
        self.assertEqual(ratios[0], 2.0)   # F(3)/F(2)
        self.assertAlmostEqual(ratios[-1], _PHI, delta=1e-9)  # F(26)/F(25)
        self.assertAlmostEqual(_PHI, (1 + math.sqrt(5)) / 2, places=12)


class TestRetracement(unittest.TestCase):
    def test_swing_100_to_200(self):
        got = retracement_levels(100.0, 200.0)
        self.assertAlmostEqual(got["23.6%"], 176.4)
        self.assertAlmostEqual(got["38.2%"], 161.8)
        self.assertAlmostEqual(got["50.0%"], 150.0)
        self.assertAlmostEqual(got["61.8%"], 200 - 100 / _PHI, places=6)
        self.assertAlmostEqual(got["78.6%"], 121.4)

    def test_levels_match_python_constants(self):
        self.assertAlmostEqual(LEVELS["61.8%"], 1 / _PHI)

    def test_extensions(self):
        got = extension_levels(100.0, 200.0)
        self.assertAlmostEqual(got["127.2%"], 327.2)
        self.assertAlmostEqual(got["161.8%"], 200 + 100 * _PHI, places=6)


if __name__ == "__main__":
    unittest.main()
