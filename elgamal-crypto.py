import random

def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent >> 1
    return result

def generate_keys(q, g):
    # Private key (d)
    d = random.randint(2, q-1)
    
    # Public key (e1, e2)
    e1 = g
    e2 = mod_pow(g, d, q)
    
    return (e1, e2, q), d

def encrypt(msg, public_key):
    e1, e2, q = public_key
    
    # Convert message to number
    m = ord(msg) if isinstance(msg, str) else msg
    
    # Generate random r
    r = random.randint(2, q-1)
    
    # Calculate c1 and c2
    c1 = mod_pow(e1, r, q)
    c2 = (mod_pow(e2, r, q) * m) % q
    
    return c1, c2

def decrypt(cipher_text, private_key, q):
    c1, c2 = cipher_text
    
    # Decrypt message
    s = mod_pow(c1, private_key, q)
    s_inv = pow(s, -1, q)
    m = (c2 * s_inv) % q
    
    return chr(m) if m < 128 else m

# Example usage
if __name__ == "__main__":
    # Parameters
    q = 2357  # A prime number
    g = 2     # Generator
    
    print("Generating keys...")
    public_key, private_key = generate_keys(q, g)
    e1, e2, q = public_key
    d = private_key
    
    print(f"Public key (e1, e2, q): ({e1}, {e2}, {q})")
    print(f"Private key (d): {d}")
    
    # Encrypt a message
    message = 'A'
    print(f"\nOriginal message: {message}")
    
    cipher_text = encrypt(message, public_key)
    print(f"Encrypted (c1, c2): {cipher_text}")
    
    # Decrypt the message
    decrypted = decrypt(cipher_text, private_key, q)
    print(f"Decrypted message: {decrypted}")
    
    # Verify with numbers
    print("\nTrying with a number instead of text...")
    num_message = 123
    print(f"Original number: {num_message}")
    
    cipher_text = encrypt(num_message, public_key)
    print(f"Encrypted (c1, c2): {cipher_text}")
    
    decrypted = decrypt(cipher_text, private_key, q)
    print(f"Decrypted number: {decrypted}")
