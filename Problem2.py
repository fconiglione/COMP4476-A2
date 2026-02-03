"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 2
"""

# Import functions from previous problems
from Problem1a import convert_from_binary
from Problem1b import function_f, x_or
from Problem1c import function_ek

# The main decryption function
def decrypt_dk(ciphertext_bits, key):
    # Split the key into two 12-bit subkeys
    K1 = key[:12]
    K2 = key[12:]
    
    # Initialize plaintext
    plaintext_bits = ""

    # Process each 16-bit block
    for i in range(0, len(ciphertext_bits), 16):
        block = ciphertext_bits[i:i+16]
        # Split block into left and right halves
        L2 = block[:8]
        R2 = block[8:]
        # Reverse the encryption steps
        # Logic: L1 = R2 XOR f(L2, K2); R1 = L2
        f2_out = function_f(L2, K2)
        L1 = x_or(R2, f2_out)
        R1 = L2
        # Logic: L0 = R1 XOR f(L1, K1); R0 = L1
        f1_out = function_f(L1, K1)
        L0 = x_or(R1, f1_out)
        R0 = L1
        # Plaintext bits is just the concatenation of L0 and R0
        plaintext_bits += L0 + R0

    return plaintext_bits

# Testing the decrypt_dk function
if __name__ == "__main__":
    original_text = "how do you like computer science"
    key = "101101010010100101101011"

    cipher_bits = function_ek(original_text, key)
    
    decrypted_bits = decrypt_dk(cipher_bits, key)
    
    final_text = convert_from_binary(decrypted_bits)
    
    print(f"Original:  {original_text.upper()}")
    print(f"Decrypted: {final_text}")
    
    if original_text.upper() in final_text.upper():
        print("Encryption is correct!")