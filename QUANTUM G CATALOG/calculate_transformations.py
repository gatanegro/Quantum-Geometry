import math
import cmath
from mpmath import mp, pi

mp.dps = 50
phi = (1 + mp.sqrt(5)) / 2

# Original levels (truncated for brevity)
lz_levels = {
    'LZ0': 0.8934691018292812244027,
    'LZ1': 0.77925056166461613546,
    # Add remaining original levels here...
}

# Transformations dictionary
transformations = {
    'LZ/φ': lambda x: x / phi,
    'LZ/φ²': lambda x: x / (phi**2),
    'LZ/φ³': lambda x: x / (phi**3),
    'sin(LZ)': lambda x: mp.sin(x),
    'LZ × (1/φ)': lambda x: x * (1/phi),
    'φ × LZ': lambda x: phi * x,
    'sin(π×LZ/φ)': lambda x: mp.sin(pi * x / phi),
    'LZ/π': lambda x: x / pi,
    # Add more transformations as needed...
}

# Calculate imaginary levels
def calculate_imaginary_levels(lz0, levels_count=14):
    imaginary_levels = {}
    current = math.asin(lz0)
    for i in range(1, levels_count + 1):
        current = cmath.asin(current)
        real_part = abs(current.real)
        imag_part = abs(current.imag)

        imaginary_levels[f'LZ-{i}_real'] = real_part
        imaginary_levels[f'LZ-{i}_imag'] = imag_part
        imaginary_levels[f'LZ-{i}_sum'] = real_part + imag_part
        imaginary_levels[f'LZ-{i}_mag'] = math.sqrt(real_part**2 + imag_part**2)

        if imag_part > 0:
            imaginary_levels[f'LZ-{i}_inv_imag'] = 1.0 / imag_part
            imaginary_levels[f'LZ-{i}_imag_p2'] = imag_part ** 2
            imaginary_levels[f'LZ-{i}_imag_p3'] = imag_part ** 3
    return imaginary_levels

# Generate a combined dictionary of all levels
imaginary_levels = calculate_imaginary_levels(lz_levels['LZ0'])
all_levels = {**lz_levels, **imaginary_levels}

# Function to compute transformations and output results as a list of dicts
def compute_all_transformations(levels, transformations):
    results = []
    for level_name, level_value in levels.items():
        for trans_name, trans_func in transformations.items():
            try:
                # Apply transformation if callable else use value directly
                derived = float(trans_func(level_value)) if callable(trans_func) else float(trans_func)
                results.append({
                    'Level': level_name,
                    'Transformation': trans_name,
                    'Value': derived
                })
            except Exception:
                continue
    return results

# Usage example:
results = compute_all_transformations(all_levels, transformations)

# Format results as a table output for easy reproducibility
print(f"{'Level':<15} {'Transformation':<20} {'Value':<20}")
print("-" * 55)
for res in results:
    print(f"{res['Level']:<15} {res['Transformation']:<20} {res['Value']:<20.12f}")

