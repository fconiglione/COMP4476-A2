"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1c
"""

from Problem1a import get_map
from Problem1b import function_f

def function_ek(message, key):
    char_map = get_map()
    binary_stream = ""
    for char in message.upper():
        if char in char_map:
            binary_stream += format(char_map[char], '05b')
            
    while len(binary_stream) % 16 != 0:
        binary_stream += "0"

    K1 = key[:12]
    K2 = key[12:]
    
    ciphertext = ""

    for i in range(0, len(binary_stream), 16):
        block = binary_stream[i:i+16]
        L = block[:8] 
        R = block[8:]
        f1_output = function_f(R, K1)
        L1 = R
        R1 = "".join('1' if L[j] != f1_output[j] else '0' for j in range(8))
        f2_output = function_f(R1, K2)
        L2 = R1
        R2 = "".join('1' if L1[j] != f2_output[j] else '0' for j in range(8))

        ciphertext += L2 + R2

    return ciphertext

if __name__ == "__main__":
    test_key = "101111010101110011001100"
    print(function_ek("This is a test message.", test_key))