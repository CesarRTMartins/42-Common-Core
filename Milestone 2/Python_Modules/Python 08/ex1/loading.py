import importlib
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use("Agg")


PACKAGES = [
    ("pandas",     "Data manipulation ready"),
    ("numpy",      "Numerical computation ready"),
    ("matplotlib", "Visualization ready"),
]

print("LOADING STATUS:")
print("Loading programs...")
print("Checking dependencies:")

missing = []
for pkg, label in PACKAGES:
    try:
        mod = importlib.import_module(pkg)
        print(f"  [OK] {pkg} ({mod.__version__}) - {label}")
    except ImportError:
        print(f"  [MISSING] {pkg} - not installed")
        missing.append(pkg)

if missing:
    print()
    print("Install missing packages with:")
    print("  pip install -r requirements.txt")
    print("  poetry install")
    sys.exit(1)


print()
print("Analyzing Matrix data...")

rng = np.random.default_rng(42)
data = rng.normal(0, 1, 1000)
df = pd.DataFrame({"value": data})

print("Processing 1000 data points...")
print("Generating visualization...")

plt.figure(figsize=(8, 4))
plt.plot(df["value"], color="green", lw=0.7)
plt.title("Matrix Analysis")
plt.savefig("matrix_analysis.png")
plt.close()

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
