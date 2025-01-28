class VigenereCipher:
    def __init__(self, key):
        """Initialize the Vigenere cipher with the given key."""
        self.key = self._clean_text(key)
        if not self.key:
            raise ValueError("Key must contain at least one letter")

    def _clean_text(self, text):
        """Remove non-alphabetic characters and convert to uppercase."""
        return ''.join(char for char in text.upper() if char.isalpha())

    def _extend_key(self, text):
        """Extend the key to match the length of the text."""
        cleaned_text = self._clean_text(text)
        quotient, remainder = divmod(len(cleaned_text), len(self.key))
        return self.key * quotient + self.key[:remainder]

    def encrypt(self, text):
        """Encrypt the input text using Vigenere cipher."""
        cleaned_text = self._clean_text(text)
        if not cleaned_text:
            return text
            
        extended_key = self._extend_key(cleaned_text)
        result = []
        text_index = 0
        
        for char in text:
            if char.isalpha():
                # Convert letters to numbers (A=0, B=1, etc.)
                text_num = ord(char.upper()) - ord('A')
                key_num = ord(extended_key[text_index]) - ord('A')
                
                # Apply Vigenere encryption formula
                encrypted_num = (text_num + key_num) % 26
                
                # Convert back to letter
                encrypted_char = chr(encrypted_num + ord('A'))
                result.append(encrypted_char if char.isupper() else encrypted_char.lower())
                text_index += 1
            else:
                result.append(char)
                
        return ''.join(result)

    def decrypt(self, text):
        """Decrypt the input text using Vigenere cipher."""
        cleaned_text = self._clean_text(text)
        if not cleaned_text:
            return text
            
        extended_key = self._extend_key(cleaned_text)
        result = []
        text_index = 0
        
        for char in text:
            if char.isalpha():
                # Convert letters to numbers (A=0, B=1, etc.)
                text_num = ord(char.upper()) - ord('A')
                key_num = ord(extended_key[text_index]) - ord('A')
                
                # Apply Vigenere decryption formula
                decrypted_num = (text_num - key_num) % 26
                
                # Convert back to letter
                decrypted_char = chr(decrypted_num + ord('A'))
                result.append(decrypted_char if char.isupper() else decrypted_char.lower())
                text_index += 1
            else:
                result.append(char)
                
        return ''.join(result)

# Example usage
if __name__ == "__main__":
    # Create cipher with key "SECRETKEY"
    cipher = VigenereCipher("SECRETKEY")
    
    # Test messages
    original_message = "HELLO WORLD"
    encrypted_message = cipher.encrypt(original_message)
    decrypted_message = cipher.decrypt(encrypted_message)
    
    print(f"Original: {original_message}")
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}")
