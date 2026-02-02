"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1d
"""

from Problem1a import convert_from_binary
from Problem1c import function_ek

def get_ciphertext():
	plaintext = "how do you like computer science"
	key = "101101010010100101101011"

	ciphertext_bits = function_ek(plaintext, key)
	ciphertext = convert_from_binary(ciphertext_bits)

	return ciphertext


if __name__ == "__main__":
	result = get_ciphertext()
	print(result)