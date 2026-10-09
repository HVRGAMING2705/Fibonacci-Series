"""Fibonacci retracement demo: given a price swing (low -> high), compute
the standard retracement levels traders watch (23.6%, 38.2%, 50%, 61.8%, 78.6%).

The 61.8% level is 1/phi; the others derive from Fibonacci ratios.
Educational demo only — not financial advice.
"""
from fibonacci import _PHI

LEVELS = {
    "23.6%": 0.236,
    "38.2%": 0.382,
    "50.0%": 0.500,
    "61.8%": 1 / _PHI,   # the golden retracement
    "78.6%": 0.786,
}


def retracement_levels(low, high):
    """Price levels for a pullback after a low->high swing."""
    swing = high - low
    return {name: high - pct * swing for name, pct in LEVELS.items()}


def extension_levels(low, high):
    """Upside extension targets beyond the swing high."""
    swing = high - low
    return {
        "127.2%": high + 1.272 * swing,
        "161.8%": high + _PHI * swing,
    }


if __name__ == "__main__":
    low, high = 100.0, 200.0
    print(f"Swing: {low} -> {high}\nRetracement levels (support zones on pullback):")
    for name, price in retracement_levels(low, high).items():
        print(f"  {name:>6}: {price:8.2f}")
    print("\nExtension levels (targets if the rally continues):")
    for name, price in extension_levels(low, high).items():
        print(f"  {name:>6}: {price:8.2f}")
