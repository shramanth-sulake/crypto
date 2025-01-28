def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    previous_x, x = 1, 0
    previous_y, y = 0, 1
    
    while b:
        quotient = a // b
        a, b = b, a % b
        x, previous_x = previous_x - quotient * x, x
        y, previous_y = previous_y - quotient * y, y
    
    return a, previous_x, previous_y

# Quick test
a, b = 26, 15
gcd, x, y = extended_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"x = {x}, y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {gcd}")