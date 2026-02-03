"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1b
"""

# Defining the S-boxes used in the function f
S1 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

S2 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

# Expanding from an 8-bit input to a 12-bit output
def expand(B):
    return B[0:4] + B[2:6] + B[4:8]

# XOR operation between two binary strings
def x_or(s1, s2):
    return "".join('1' if s1[i] != s2[i] else '0' for i in range(len(s1)))

# Search logic in the S-boxes
def search(bits, matrix):
    # Determine row and column for S-box lookup
    row = int(bits[0] + bits[5], 2)
    col = int(bits[1:5], 2)
    val = matrix[row][col]
    # 4-bit binary representation of the S-box output
    return format(val, '04b')

# The main function f 
def function_f(B, K):
    # 8-bit B, 12-bit K
    E = expand(B)
    # Perform xor between expanded B and K
    xored = x_or(E, K)
    # Split into two 6-bit halves and process through S-boxes
    B1, B2 = xored[:6], xored[6:]
    return search(B1, S1) + search(B2, S2)

# Testing the function_f
if __name__ == "__main__":
    plaintext_8bit = "10110101"
    key_12bit = "110011001100"
    result = function_f(plaintext_8bit, key_12bit)
    print(f"Result: {result}")