import math
import cmath
from mpmath import mp, sin, asin, pi, sqrt

mp.dps = 50

# COMPLETE ATOMIC IONIZATION ENERGIES (eV) FOR ALL ELEMENTS
atomic_energies = {
    # Period 1
    'H': 13.59844,
    'He': 24.58741,
    
    # Period 2
    'Li': 5.39172,
    'Be': 9.32270,
    'B': 8.29803,
    'C': 11.26030,
    'N': 14.53414,
    'O': 13.61806,
    'F': 17.42282,
    'Ne': 21.56460,
    
    # Period 3
    'Na': 5.13908,
    'Mg': 7.64624,
    'Al': 5.98577,
    'Si': 8.15169,
    'P': 10.48669,
    'S': 10.36001,
    'Cl': 12.96764,
    'Ar': 15.75962,
    
    # Period 4
    'K': 4.34066,
    'Ca': 6.11316,
    'Sc': 6.56150,
    'Ti': 6.82812,
    'V': 6.74619,
    'Cr': 6.76651,
    'Mn': 7.43402,
    'Fe': 7.90247,
    'Co': 7.88101,
    'Ni': 7.63988,
    'Cu': 7.72638,
    'Zn': 9.39420,
    'Ga': 5.99930,
    'Ge': 7.89943,
    'As': 9.78855,
    'Se': 9.75238,
    'Br': 11.81381,
    'Kr': 13.99961,
    
    # Period 5
    'Rb': 4.17713,
    'Sr': 5.69485,
    'Y': 6.21730,
    'Zr': 6.63390,
    'Nb': 6.75885,
    'Mo': 7.09243,
    'Tc': 7.11938,
    'Ru': 7.36050,
    'Rh': 7.45890,
    'Pd': 8.33686,
    'Ag': 7.57623,
    'Cd': 8.99382,
    'In': 5.78636,
    'Sn': 7.34392,
    'Sb': 8.60839,
    'Te': 9.00966,
    'I': 10.45126,
    'Xe': 12.12987,
    
    # Period 6
    'Cs': 3.89390,
    'Ba': 5.21170,
    'La': 5.57690,
    'Ce': 5.53870,
    'Pr': 5.47300,
    'Nd': 5.52500,
    'Pm': 5.58200,
    'Sm': 5.64370,
    'Eu': 5.67040,
    'Gd': 6.14980,
    'Tb': 5.86380,
    'Dy': 5.93890,
    'Ho': 6.02150,
    'Er': 6.10770,
    'Tm': 6.18431,
    'Yb': 6.25416,
    'Lu': 5.42587,
    'Hf': 6.82507,
    'Ta': 7.54960,
    'W': 7.86403,
    'Re': 7.83352,
    'Os': 8.43823,
    'Ir': 8.96702,
    'Pt': 8.95883,
    'Au': 9.22555,
    'Hg': 10.43750,
    'Tl': 6.10829,
    'Pb': 7.41666,
    'Bi': 7.28551,
    'Po': 8.41670,
    'At': 9.31751,
    'Rn': 10.74850,
    
    # Period 7
    'Fr': 4.07274,
    'Ra': 5.27840,
    'Ac': 5.38020,
    'Th': 6.30670,
    'Pa': 5.89000,
    'U': 6.19405,
    'Np': 6.26570,
    'Pu': 6.02600,
    'Am': 5.97380,
    'Cm': 5.99140,
    'Bk': 6.19790,
    'Cf': 6.28170,
    'Es': 6.36760,
    'Fm': 6.50000,
    'Md': 6.58000,
    'No': 6.65000,
    'Lr': 4.90000,
}


# LOGOS original LZ levels
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
    # ... include all LOGOS LZ levels up to LZ45
}

# Calculate upward complex levels
lz0 = lz_levels['LZ0']
a0 = math.asin(lz0)

complex_levels = {}
current = a0
for i in range(1, 20):  # Extended to LZ-19 for more coverage
    current = cmath.asin(current)
    complex_levels[f'LZ-{i}'] = current

# Create quantum levels with positive imaginary signs
quantum_levels = {}
for name, complex_val in complex_levels.items():
    real_part = abs(float(complex_val.real))
    imag_part = abs(float(complex_val.imag))
    
    quantum_levels[f'{name}_real'] = real_part
    quantum_levels[f'{name}_imag'] = imag_part
    quantum_levels[f'{name}_sum'] = real_part + imag_part
    quantum_levels[f'{name}_mag'] = math.sqrt(real_part**2 + imag_part**2)
    quantum_levels[f'{name}_prod'] = real_part * imag_part if imag_part > 0 else real_part
    
    if imag_part > 0:
        quantum_levels[f'{name}_inv_imag'] = 1.0 / imag_part
        for power in [2, 3, 4]:
            quantum_levels[f'{name}_imag_p{power}'] = imag_part ** power
            quantum_levels[f'{name}_real_p{power}'] = real_part ** power

# Add original levels
quantum_levels.update(lz_levels)


phi = (1 + mp.sqrt(5)) / 2

# Transformations for finding relationships
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
    'LZ × 10': lambda x: x * 10,
    'LZ × 100': lambda x: x * 100,
    '1/LZ': lambda x: 1.0 / x if x != 0 else 1e10,
    '1/LZ²': lambda x: 1.0 / (x**2) if x != 0 else 1e10,
}

# Now run for all elements
print("CALCULATING LZ RELATIONS FOR ALL ELEMENTS:")
print(f"{'Element':<4} {'Energy (eV)':<12} {'Best LZ Formula':<35} {'Derived':<12} {'Error':<10} {'Status':<12}")
print("-" * 90)

for element, energy in atomic_energies.items():
    best_error = float('inf')
    best_formula = ""
    best_value = 0
    
    for lz_name, lz_val in quantum_levels.items():
        lz_val_float = float(lz_val)
        
        for trans_name, trans_func in transformations.items():
            try:
                derived = float(trans_func(lz_val_float))
                error = abs(derived - energy)
                
                if error < best_error:
                    best_error = error
                    best_formula = f"{trans_name.replace('LZ', lz_name)}"
                    best_value = derived
            except:
                continue
    
    status = "EXCELLENT" if best_error < 0.1 else "VERY GOOD" if best_error < 0.5 else "GOOD" if best_error < 1.0 else "CLOSE"
    print(f"{element:<4} {energy:<12.3f} {best_formula:<35} {best_value:<12.3f} {best_error:<10.3f} {status:<12}")
