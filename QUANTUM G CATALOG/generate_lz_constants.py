import matplotlib.pyplot as plt
from mpmath import mp, sin, exp, mpf, plot
"""
LOGOS THEORY
Author: Martin Doina 
"""


# Set precision to 100 decimal places
mp.dps = 100

# Define the number of iterations
num_iterations = 20

# Initialize with the EXACT high-precision initial value
psi_values = [mpf('0.8934691018292812244027')]

# Compute the evolution with high precision
for i in range(1, num_iterations):
    psi_values.append(sin(psi_values[i-1]) + exp(-psi_values[i-1]))

# Convert to float for plotting (loses precision but needed for matplotlib)
psi_values_float = [float(val) for val in psi_values]

# Plot
plt.figure(figsize=(8, 4))
plt.plot(range(num_iterations), psi_values_float, marker="o", linestyle="-", color="blue", label="Ψ(n) Evolution")
plt.xlabel("Recursion Level (n)")
plt.ylabel("Wave Function Ψ(n)")
plt.title("LOGOS Recursive Wave Function Evolution")
plt.legend()
plt.grid(True)
plt.show()

# Display the computed values WITH FULL PRECISION
print("LOGOS EXACT LZ & HQS VALUES (100 decimals):")
print("=" * 85)
for i, val in enumerate(psi_values):
    print(f"LZ_{i} = {val}")

print(f"\nHQS VALUES for each LZ:")
print("=" * 85)
for i, val in enumerate(psi_values):
    hqs = exp(-val) / val
    print(f"HQS_{i} = {hqs}")
