def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular multiplicative inverse of a modulo m."""
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return None

class AffineCipher:
    def __init__(self, a=5, b=8):
        """Initialize the Affine cipher with keys a and b.
        a must be coprime with 26 (alphabet size)"""
        if gcd(a, 26) != 1:
            raise ValueError("'a' must be coprime with 26")
        self.a = a
        self.b = b
        
    def encrypt(self, text):
        """Encrypt the input text using Affine cipher."""
        result = ""
        for char in text.upper():
            if char.isalpha():
                # Convert letter to number (A=0, B=1, ...)
                x = ord(char) - ord('A')
                # Apply affine transformation: (ax + b) mod 26
                encrypted_num = (self.a * x + self.b) % 26
                # Convert back to letter
                result += chr(encrypted_num + ord('A'))
            else:
                result += char
        return result
    
    def decrypt(self, text):
        """Decrypt the input text using Affine cipher."""
        result = ""
        # Find modular multiplicative inverse of a
        a_inv = mod_inverse(self.a, 26)
        if a_inv is None:
            raise ValueError("Modular multiplicative inverse does not exist")
            
        for char in text.upper():
            if char.isalpha():
                # Convert letter to number (A=0, B=1, ...)
                y = ord(char) - ord('A')
                # Apply inverse affine transformation: a^(-1)(y - b) mod 26
                decrypted_num = (a_inv * (y - self.b)) % 26
                # Convert back to letter
                result += chr(decrypted_num + ord('A'))
            else:
                result += char
        return result

# Example usage
if __name__ == "__main__":
    # Create cipher with keys a=5, b=8
    cipher = AffineCipher(5, 8)
    
    # Test encryption
    message = "HELLO WORLD"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")