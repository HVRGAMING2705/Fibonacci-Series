"""Plot F(n+1)/F(n) converging to the golden ratio phi."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from fibonacci import golden_ratio_approximations, _PHI

terms = 25
ratios = golden_ratio_approximations(terms)
ns = list(range(3, terms + 2))

plt.figure(figsize=(9, 5))
plt.plot(ns, ratios, "o-", label="F(n+1) / F(n)")
plt.axhline(_PHI, color="red", linestyle="--", label=f"phi = {_PHI:.10f}")
plt.xlabel("n")
plt.ylabel("ratio")
plt.title("Convergence of Fibonacci ratios to the golden ratio")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("golden_ratio.png", dpi=120)
print("saved golden_ratio.png")
print(f"F(26)/F(25) = {ratios[-1]:.12f}  vs  phi = {_PHI:.12f}")
