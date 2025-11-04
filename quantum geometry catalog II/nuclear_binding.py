import math
import cmath
from mpmath import mp, sin, asin, pi, sqrt

"""
LOGOS THEORY - GOLDEN RATIO MAPPING
Using: sin(ℓₚ) ≈ ℓₚ/φ
"""

mp.dps = 50

print("Nuclear binding energies (MeV per nucleon) - key nuclei")
print("=" * 70)

# Nuclear binding energies (MeV per nucleon) - key nuclei
nuclear_binding_data = {
    'H2': 1.112,    # Deuterium
    'He4': 7.074,   # Alpha particle
    'C12': 7.680,
    'O16': 7.976,
    'Fe56': 8.790,  # Peak
    'Ag107': 8.552,
    'Pb208': 7.867,
    'U238': 7.570,
}

# REAL LZ levels (sine iterates)
real_lz_levels = {
    'LZ0': 0.8934691018292812244027,
    'LZ1': 0.77925056166461613546,     
    'LZ2': 0.70274643589057133551,      
    'LZ3': 0.646315844994190005925,    
    'LZ4': 0.602249409166941011016,     
    'LZ5': 0.566497560827266638609, 
    'LZ6': 0.536680037956250069056,  
    'LZ7': 0.511285603178539657953,      
    'LZ8': 0.48929884626327098115,      
    'LZ9': 0.470007121557258645354,   
    'LZ10': 0.452892634722198191231,
    'LZ11': 0.437568375282611265813,
    'LZ12': 0.423738191480105923173,
    'LZ13': 0.411170897372839147563,
    'LZ14': 0.399682908854264909393, 
    'LZ15': 0.38912626245028160807,
    'LZ16': 0.379380142329113925443,
    'LZ17': 0.370344758293618177551,
    'LZ18': 0.361936838052865187321,
    'LZ19': 0.354086251973120615728,
    'LZ20': 0.346733447618190129634,
}

# COMPLEX LZ levels (analytic continuation)
print("Calculating COMPLEX LZ levels (analytic continuation)...")
lz0 = real_lz_levels['LZ0']
a0 = math.asin(lz0)

complex_lz_levels = {}
current = a0
for i in range(1, 25):
    try:
        current = cmath.asin(current)
        complex_lz_levels[f'LZ-{i}'] = current
        # Print first few to verify
        if i <= 5:
            print(f"LZ-{i}: {current}")
    except:
        break

print(f"Generated {len(complex_lz_levels)} complex levels")

# Build QUANTUM ZOO with all levels
quantum_levels = {}

# Add REAL levels as-is
for name, value in real_lz_levels.items():
    quantum_levels[name] = value

# Add COMPLEX levels with full properties
for name, complex_val in complex_lz_levels.items():
    real_part = abs(float(complex_val.real))
    imag_part = abs(float(complex_val.imag))
    
    # Store the complex value itself
    quantum_levels[name] = complex_val
    
    # Store decomposed properties
    quantum_levels[f'{name}_real'] = real_part
    quantum_levels[f'{name}_imag'] = imag_part
    quantum_levels[f'{name}_sum'] = real_part + imag_part
    quantum_levels[f'{name}_mag'] = math.sqrt(real_part**2 + imag_part**2)
    quantum_levels[f'{name}_prod'] = real_part * imag_part
    
    # Enhanced operations
    if imag_part != 0:
        quantum_levels[f'{name}_inv_imag'] = 1.0 / imag_part
    if real_part != 0:
        quantum_levels[f'{name}_inv_real'] = 1.0 / real_part
    
    # Powers for scaling
    for power in [2, 3, 4]:
        quantum_levels[f'{name}_real_p{power}'] = real_part ** power
        quantum_levels[f'{name}_imag_p{power}'] = imag_part ** power

print(f"Total quantum levels available: {len(quantum_levels)}")

phi = float((1 + mp.sqrt(5)) / 2)
pi_val = float(mp.pi)

# TRANSFORMATIONS for nuclear binding range
transformations = {
    # Basic scaling
    'LZ': lambda x: x,
    '1/LZ': lambda x: 1.0 / x if x != 0 else 1e20,
    'LZ²': lambda x: x**2,
    'LZ³': lambda x: x**3,
    
    # Golden ratio scaling
    'LZ×φ': lambda x: x * phi,
    'LZ×φ²': lambda x: x * phi**2,
    'LZ×φ³': lambda x: x * phi**3,
    'LZ×φ⁴': lambda x: x * phi**4,
    'LZ×φ⁵': lambda x: x * phi**5,
    
    # Pi scaling
    'LZ×π': lambda x: x * pi_val,
    'LZ×π²': lambda x: x * pi_val**2,
    
    # Combined transforms
    'LZ×φ×π': lambda x: x * phi * pi_val,
    'LZ²×φ': lambda x: x**2 * phi,
    'LZ³×φ': lambda x: x**3 * phi,
}

print(f"\n{'Nucleus':<10} {'Actual':<8} {'Best Formula':<40} {'Derived':<8} {'Error':<8} {'Level Type':<12}")
print("-" * 90)

results = []

for nucleus, actual_value in nuclear_binding_data.items():
    best_error = float('inf')
    best_formula = ""
    best_derived = 0
    best_level_type = ""
    
    for lz_name, lz_val in quantum_levels.items():
        # Handle both real and complex values
        if isinstance(lz_val, complex):
            lz_val_float = abs(lz_val)  # Use magnitude for complex
            level_type = "COMPLEX"
        else:
            lz_val_float = float(lz_val)
            level_type = "REAL"
        
        for trans_name, trans_func in transformations.items():
            try:
                derived = trans_func(lz_val_float)
                
                # Skip unreasonable values for nuclear binding
                if derived <= 0 or derived > 20:
                    continue
                    
                error = abs(derived - actual_value)
                
                if error < best_error:
                    best_error = error
                    best_formula = f"{trans_name.replace('LZ', lz_name)}"
                    best_derived = derived
                    best_level_type = level_type
            except:
                continue
    
    results.append((nucleus, actual_value, best_formula, best_derived, best_error, best_level_type))

# Sort by error
results.sort(key=lambda x: x[4])

for nucleus, actual, formula, derived, error, level_type in results:
    status = "EXCELLENT" if error < 0.1 else "GOOD" if error < 0.5 else "CLOSE"
    print(f"{nucleus:<10} {actual:<8.3f} {formula:<40} {derived:<8.3f} {error:<8.3f} {level_type:<12} {status}")

print(f"\n" + "=" * 90)
print("ANALYSIS BY LEVEL TYPE:")
complex_matches = [r for r in results if r[5] == "COMPLEX"]
real_matches = [r for r in results if r[5] == "REAL"]

print(f"Complex level matches: {len(complex_matches)}")
print(f"Real level matches: {len(real_matches)}")
print(f"Best overall: {results[0][0]} (Error: {results[0][4]:.3f} MeV)")

if complex_matches:
    avg_complex_error = sum(r[4] for r in complex_matches) / len(complex_matches)
    print(f"Average complex level error: {avg_complex_error:.3f} MeV")

if real_matches:
    avg_real_error = sum(r[4] for r in real_matches) / len(real_matches)
    print(f"Average real level error: {avg_real_error:.3f} MeV")
