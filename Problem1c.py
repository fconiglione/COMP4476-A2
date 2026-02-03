"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1c
"""

from Problem1a import get_map
from Problem1b import function_f

# The main encryption function
def function_ek(message, key):
    # Convert message to binary using 5-bit representation
    char_map = get_map()
    binary_stream = ""
    for char in message.upper():
        if char in char_map:
            binary_stream += format(char_map[char], '05b')
    # Add padding to make the length a multiple of 16
    while len(binary_stream) % 16 != 0:
        binary_stream += "0"

    # Split the key into two 12-bit subkeys
    K1 = key[:12]
    K2 = key[12:]
    
    # Initialize ciphertext
    ciphertext = ""

    # Process each 16-bit block
    for i in range(0, len(binary_stream), 16):
        block = binary_stream[i:i+16]
        # Split block into left and right halves
        L = block[:8] 
        R = block[8:]
        # Formula: L1 = R0; R1 = L0 XOR f(R0, K1)
        f1_output = function_f(R, K1)
        L1 = R
        R1 = "".join('1' if L[j] != f1_output[j] else '0' for j in range(8))
        # Formula: L2 = R1; R2 = L1 XOR f(R1, K2)
        f2_output = function_f(R1, K2)
        L2 = R1
        # Manual XOR operation
        R2 = "".join('1' if L1[j] != f2_output[j] else '0' for j in range(8))
        # Ciphertext is just the concatenation of L2 and R2
        ciphertext += L2 + R2

    return ciphertext

# Testing the function_ek
if __name__ == "__main__":
    test_key = "101111010101110011001100"
    print(function_ek("This is a test message.", test_key))