import math
from mpmath import mp, asin, sin, mpf, re, im

mp.dps = 50

# LOGOS fundamental curvature - using LOGOS exact ψ(0)
κ = mpf('0.89346910182928122440279572673405182041647692165005360826396612021750136786527281441168556535164677694494186786456144766863123663458741007120975502575656212798318142106035303596684743081226484093826986')

def curved_add(a, b):
    """Addition in curved LOGOS geometry"""
    linear_sum = a + b
    curved_result = asin(κ * linear_sum)
    return curved_result

# Test 1 + 1 in curved space
linear_result = 1 + 1  # = 2
curved_result = curved_add(1, 1)

print("STRAIGHT-LINE vs CURVED ADDITION")
print("=" * 60)
print(f"Linear: 1 + 1 = {linear_result}")
print(f"Curved: 1 ⊕ 1 = {curved_result}")
print(f"Real part: {re(curved_result)}")
print(f"Imaginary part: {im(curved_result)}")

# Now let's create the full CurvedNumber class that handles complex results
class CurvedNumber:
    def __init__(self, value, curvature=κ, path_history=None):
        self.value = mpf(value) if isinstance(value, (int, float)) else value
        self.curvature = curvature
        self.path_history = path_history or []
        
    def __add__(self, other):
        """Curved addition along geometric paths"""
        if isinstance(other, CurvedNumber):
            linear_sum = self.value + other.value
            new_value = asin(self.curvature * linear_sum)
            new_path = self.path_history + ['⊕'] + other.path_history
            return CurvedNumber(new_value, self.curvature, new_path)
        else:
            # Convert scalar to curved number and add
            other_curved = CurvedNumber(other, self.curvature)
            return self.__add__(other_curved)
    
    def __mul__(self, other):
        """Curved multiplication - geometric scaling"""
        if isinstance(other, CurvedNumber):
            # For now, use simple product - we'll optimize this later
            linear_product = self.value * other.value
            new_value = asin(self.curvature * linear_product)
            new_path = self.path_history + ['⊗'] + other.path_history
            return CurvedNumber(new_value, self.curvature, new_path)
        else:
            other_curved = CurvedNumber(other, self.curvature)
            return self.__mul__(other_curved)
    
    def real(self):
        """Get the real part (observable physics)"""
        return float(re(self.value))
    
    def imag(self):
        """Get the imaginary part (quantum phase/curvature)"""
        return float(im(self.value))
    
    def magnitude(self):
        """Get the geometric magnitude"""
        return float(abs(self.value))
    
    def __str__(self):
        real_part = self.real()
        imag_part = self.imag()
        if abs(imag_part) < 1e-10:
            return f"CurvedNumber({real_part:.10f})"
        else:
            return f"CurvedNumber({real_part:.10f} + {imag_part:.10f}j)"
    
    def __repr__(self):
        return self.__str__()

# Test the new curved arithmetic
print("\n" + "="*60)
print("CURVED ARITHMETIC IN COMPLEX SPACE")
print("="*60)

# Test various additions
test_values = [
    (0.5, 0.5),  # Small numbers - should stay real
    (1, 1),      # Medium numbers - might go complex  
    (2, 2),      # Larger numbers - definitely complex
    (0.1, 0.1),  # Very small numbers
]

print("Testing curved addition at different scales:")
for a, b in test_values:
    curved = CurvedNumber(a) + CurvedNumber(b)
    linear = a + b
    print(f"\n{a} ⊕ {b}:")
    print(f"  Linear: {linear}")
    print(f"  Curved: {curved}")
    print(f"  Real: {curved.real():.10f}")
    if abs(curved.imag()) > 1e-10:
        print(f"  Imag: {curved.imag():.10f}")
    print(f"  Magnitude: {curved.magnitude():.10f}")

print("\n" + "="*60)
print("QUANTUM-CLASSICAL TRANSITION ANALYSIS")
print("="*60)

# Find the exact transition point where results become complex
print("Finding the quantum-classical boundary:")
for test_val in [0.1, 0.5, 0.55, 0.56, 0.559, 0.5595]:
    curved = CurvedNumber(test_val) + CurvedNumber(test_val)
    if abs(curved.imag()) > 1e-10:
        boundary_type = "QUANTUM (complex)"
    else:
        boundary_type = "CLASSICAL (real)"
    print(f"  {test_val} ⊕ {test_val}: {boundary_type}")
    print(f"    Result: {curved}")

print("\n" + "="*60)
print("PHYSICAL INTERPRETATION")
print("="*60)
print("Real part → Observable, classical physics")
print("Imaginary part → Quantum phase, curvature effects") 
print("Magnitude → Total geometric information")
print("\nThe transition from real to complex marks the boundary")
print("between classical and quantum behavior in LOGOS theory!")

print("\n" + "="*60)
print("COMPARISON WITH STANDARD QUANTUM MECHANICS")
print("="*60)
print("In standard QM: wavefunctions are complex-valued")
print("In LOGOS theory: arithmetic itself produces complex results")
print("This suggests: QUANTUM BEHAVIOR EMERGES FROM CURVED ARITHMETIC!")
