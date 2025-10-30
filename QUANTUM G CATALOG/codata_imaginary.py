import math
import cmath
from mpmath import mp, sin, asin, pi, sqrt

mp.dps = 50

phi = (1 + mp.sqrt(5)) / 2


# ORIGINAL CODE - UNCHANGED
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

# ORIGINAL TRANSFORMATIONS - UNCHANGED
transformations = {
    'LZ/φ': lambda x: x / phi,
    'LZ/φ²': lambda x: x / (phi**2),
    'LZ/φ³': lambda x: x / (phi**3),
    'LZ/φ⁴': lambda x: x / (phi**4),
    'LZ/φ⁵': lambda x: x / (phi**5),
    'LZ/φ⁶': lambda x: x / (phi**6),
    'LZ/φ⁷': lambda x: x / (phi**7),
    'LZ/φ⁸': lambda x: x / (phi**8),
    'LZ/φ⁹': lambda x: x / (phi**9),
    'LZ/φ¹⁰': lambda x: x / (phi**10),
    'sin(LZ)': lambda x: mp.sin(x),
    'LZ × (1/φ)': lambda x: x * (1/phi),
    'LZ × (1/φ²)': lambda x: x * (1/(phi**2)),
    'φ × LZ': lambda x: phi * x,
    'φ² × LZ': lambda x: (phi**2) * x,
    'φ³ × LZ': lambda x: (phi**3) * x,
    'sin(π×LZ/φ)': lambda x: mp.sin(pi * x / phi),
    'LZ/π': lambda x: x / pi,
    '1/φ': 1/phi,
    '1/φ²': 1/(phi**2),
    '1/φ³': 1/(phi**3),
    '1/φ⁴': 1/(phi**4),
    '2/φ': 2/phi,
    '3/φ': 3/phi,
    'φ/2': phi/2,
    'φ/3': phi/3,
    'φ/4': phi/4,
    
}

# JUST ADD IMAGINARY LEVELS TO EXPAND
print("CODATA EXPERIMENTAL")

# Calculate upward levels from  LZ0
lz0 = lz_levels['LZ0']
a0 = math.asin(lz0)

# Add imaginary levels with positive signs
imaginary_levels = {}
current = a0
for i in range(1, 15):
    current = cmath.asin(current)
    real_part = abs(current.real)
    imag_part = abs(current.imag)
    
    # Add to levels with positive signs only
    imaginary_levels[f'LZ-{i}_real'] = real_part
    imaginary_levels[f'LZ-{i}_imag'] = imag_part
    imaginary_levels[f'LZ-{i}_sum'] = real_part + imag_part
    imaginary_levels[f'LZ-{i}_mag'] = math.sqrt(real_part**2 + imag_part**2)
    
    if imag_part > 0:
        imaginary_levels[f'LZ-{i}_inv_imag'] = 1.0 / imag_part
        imaginary_levels[f'LZ-{i}_imag_p2'] = imag_part ** 2
        imaginary_levels[f'LZ-{i}_imag_p3'] = imag_part ** 3

# COMBINE ORIGINAL + IMAGINARY LEVELS
all_levels = {**lz_levels, **imaginary_levels}

print(f"Original levels: {len(lz_levels)}")
print(f"Imaginary levels: {len(imaginary_levels)}") 
print(f"Total levels: {len(all_levels)}")
print()

# NOW TEST WITH ALL CODATA CONSTANTS
codata_constants = {
    'fine_structure_constant': 0.0072973525693,
    'inverse_fine_structure': 137.035999084,
    'weak_mixing_angle': 0.22290,
    'weinberg_angle_sin2theta': 0.23121,
    'strong_coupling_alpha_s': 0.1179,
    'electron_g_minus_2': 0.00115965218128,
    'muon_g_minus_2': 0.00116592089,
    'electron_muon_mass_ratio': 0.00483633170,
    'muon_tau_mass_ratio': 0.05946,
    'proton_electron_mass_ratio': 1836.15267343,
    'neutron_proton_mass_ratio': 1.00137841931,
    'w_z_boson_mass_ratio': 0.88147,
    'up_down_quark_ratio': 0.462,
    'strange_down_quark_ratio': 19.99,
    'charm_strange_quark_ratio': 13.59,
    'bottom_charm_quark_ratio': 4.49,
    'top_bottom_quark_ratio': 41.33,
    'cabibbo_angle': 0.22650,
    'ckm_theta12': 0.22650,
    'ckm_theta23': 0.04120,
    'ckm_theta13': 0.00370,
    'ckm_delta_cp': 1.144,
    'pmns_theta12': 0.590,
    'pmns_theta23': 0.866,
    'pmns_theta13': 0.150,
    'pmns_delta_cp': 1.360,
    'qcd_scale_lambda': 0.218,
    'fermi_coupling_constant': 1.1663787e-5,
    'baryon_density': 0.0486,
    'dark_matter_density': 0.2589,
    'dark_energy_density': 0.6911,
    'spectral_index': 0.9649,
    'tensor_to_scalar_ratio': 0.036,
    'primordial_helium_abundance': 0.245,
}

print("TESTING WITH EXPANDED LEVELS:")
print(f"{'Constant':<30} {'Experimental':<15} {'Best Formula':<25} {'Value':<15} {'Error':<10} {'Level Type':<12}")
print("-" * 100)

for const_name, experimental in codata_constants.items():
    best_error = float('inf')
    best_formula = ""
    best_value = 0
    best_level = ""
    
    for lz_name, lz_val in all_levels.items():
        for trans_name, trans_func in transformations.items():
            try:
                if callable(trans_func):
                    derived = float(trans_func(lz_val))
                else:
                    derived = float(trans_func)
                
                error = abs(derived - experimental)
                
                if error < best_error:
                    best_error = error
                    best_formula = f"{trans_name.replace('LZ', lz_name)}"
                    best_value = derived
                    best_level = lz_name
            except:
                continue
    
    level_type = "IMAGINARY" if 'imag' in best_level else "REAL" if 'real' in best_level else "ORIGINAL"
    status = "EXCELLENT" if best_error < 0.001 else "VERY GOOD" if best_error < 0.01 else "GOOD"
    
    print(f"{const_name:<30} {experimental:<15.6f} {best_formula:<25} {best_value:<15.6f} {best_error:<10.6f} {level_type:<12} {status}")


