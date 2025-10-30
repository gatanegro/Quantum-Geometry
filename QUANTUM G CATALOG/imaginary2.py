import math
import cmath
from mpmath import mp, sin, asin, pi, sqrt

mp.dps = 50

# Logos original LZ levels
lz_levels = {
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
    'LZ21': 0.339827473319247090606,
    'LZ22': 0.333324436845215765359,
    'LZ23': 0.32718628998495953142,
    'LZ24': 0.321379860372918368459,
    'LZ25': 0.315876073068827859531,
    'LZ26': 0.310649319329871311505,
    'LZ27': 0.3056769406866667788,
    'LZ28': 0.300938804166517768292,
    'LZ29': 0.296416950177173712814,
    'LZ30': 0.292095298768961361413,
    'LZ31': 0.287959403143925088878,
    'LZ32': 0.283996241664756972798,
    'LZ33': 0.280194041436796408411,
    'LZ34': 0.276542127938351935615,
    'LZ35': 0.273030796262904206157,
    'LZ36': 0.269651200387920475574,
    'LZ37': 0.266395257555432414033,
    'LZ38': 0.263255565381111088366,
    'LZ39': 0.260225329732728870093,
    'LZ40': 0.25729830175935910849,
    'LZ41': 0.254468722727492864449,
    'LZ42': 0.251731275543292632323,
    'LZ43': 0.24908104202213930352,
    'LZ44': 0.246513465115757403688,
    'LZ45': 0.244024267318637789654,
}

phi = (1 + mp.sqrt(5)) / 2

print("QUANTUM ZOO FROM IMAGINARY LEVELS WITH POSITIVE SIGNS")
print("=" * 70)

# Calculate upward complex levels
lz0 = lz_levels['LZ0']
a0 = math.asin(lz0)

lz_minus_1 = cmath.asin(a0)
lz_minus_2 = cmath.asin(lz_minus_1)
lz_minus_3 = cmath.asin(lz_minus_2)
lz_minus_4 = cmath.asin(lz_minus_3)
lz_minus_5 = cmath.asin(lz_minus_4)

print("Complex upward levels:")
complex_levels = {
    'LZ-1': lz_minus_1,
    'LZ-2': lz_minus_2,
    'LZ-3': lz_minus_3,
    'LZ-4': lz_minus_4,
    'LZ-5': lz_minus_5,
}

for name, value in complex_levels.items():
    print(f"{name}: {value}")

# Create positive imaginary levels for quantum zoo
print(f"\n" + "=" * 70)
print("CREATING QUANTUM ZOO LEVELS - POSITIVE IMAGINARY PARTS")
print("=" * 70)

quantum_levels = {}

# Use absolute values of imaginary parts for quantum particles
for name, complex_val in complex_levels.items():
    real_part = abs(float(complex_val.real))
    imag_part = abs(float(complex_val.imag))
    
    # Different combinations for different particle types
    quantum_levels[f'{name}_real'] = real_part
    quantum_levels[f'{name}_imag'] = imag_part
    quantum_levels[f'{name}_sum'] = real_part + imag_part
    quantum_levels[f'{name}_mag'] = math.sqrt(real_part**2 + imag_part**2)  # magnitude
    
    if imag_part > 0:
        quantum_levels[f'{name}_inv_imag'] = 1.0 / imag_part
        quantum_levels[f'{name}_imag_sq'] = imag_part ** 2
        quantum_levels[f'{name}_imag_cu'] = imag_part ** 3

# Add quantum levels to main dictionary
lz_levels.update(quantum_levels)

print("Quantum zoo levels created:")
for name, value in quantum_levels.items():
    print(f"{name}: {value:.10f}")

print(f"\n" + "=" * 70)
print("MAPPING TO QUANTUM PARTICLE MASSES (GeV)")
print("=" * 70)

# Known particle masses in GeV
particle_masses = {
    'electron': 0.000511,
    'muon': 0.10566,
    'tau': 1.77686,
    'charm_quark': 1.27,
    'strange_quark': 0.0934,
    'bottom_quark': 4.18,
    'top_quark': 172.76,
    'W_boson': 80.379,
    'Z_boson': 91.1876,
    'Higgs': 125.25,
    'proton': 0.93827,
    'neutron': 0.93957,
}

transformations = {
    'LZ': lambda x: x,
    'LZ × φ': lambda x: x * float(phi),
    'LZ × φ²': lambda x: x * float(phi**2),
    'LZ × φ³': lambda x: x * float(phi**3),
    'LZ × φ⁴': lambda x: x * float(phi**4),
    'LZ × φ⁵': lambda x: x * float(phi**5),
    'LZ × φ⁶': lambda x: x * float(phi**6),
    'LZ × φ⁷': lambda x: x * float(phi**7),
    'LZ × φ⁸': lambda x: x * float(phi**8),
    'LZ × φ⁹': lambda x: x * float(phi**9),
    'LZ × φ¹⁰': lambda x: x * float(phi**10),
    'LZ × 1000': lambda x: x * 1000,
    'LZ × 10000': lambda x: x * 10000,
}

print(f"{'Particle':<15} {'Mass (GeV)':<12} {'Best Formula':<30} {'Derived':<12} {'Error':<10} {'Level Type':<15}")
print("-" * 95)

for particle, mass in particle_masses.items():
    best_error = float('inf')
    best_formula = ""
    best_value = 0
    best_level = ""
    
    for lz_name, lz_val in lz_levels.items():
        lz_val_float = float(lz_val)
        
        for trans_name, trans_func in transformations.items():
            try:
                derived = float(trans_func(lz_val_float))
                error = abs(derived - mass)
                
                if error < best_error:
                    best_error = error
                    best_formula = f"{trans_name.replace('LZ', lz_name)}"
                    best_value = derived
                    best_level = lz_name
            except:
                continue
    
    level_type = "QUANTUM" if any(x in best_level for x in ['-1', '-2', '-3', '-4', '-5', 'imag', 'mag', 'sum']) else "ORIGINAL"
    status = "✓" if best_error < 0.001 else "~" if best_error < 0.01 else "✗"
    
    print(f"{particle:<15} {mass:<12.6f} {best_formula:<30} {best_value:<12.6f} {best_error:<10.6f} {level_type:<15} {status}")

print(f"\n" + "=" * 70)
print("QUANTUM LEVELS USAGE SUMMARY")
print("=" * 70)

quantum_used = []
original_used = []

for particle in particle_masses.keys():
    # This would need to track which levels were actually used
    # For now, let's just show the pattern
    pass

print("Quantum levels available:")
for name in quantum_levels.keys():
    print(f"  {name}")

print(f"\nThe imaginary parts with positive signs should give us:")
print("• Electron, muon, tau leptons")
print("• Quarks (up, down, strange, charm, bottom, top)") 
print("• Gauge bosons (W, Z, photon, gluons)")
print("• Higgs boson")
print("• Proton, neutron")
