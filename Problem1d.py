"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1d
"""

# Import functions from previous problems
from Problem1a import convert_from_binary
from Problem1c import function_ek

# Function to get the ciphertext for the given plaintext and key
def get_ciphertext():
	plaintext = "how do you like computer science"
	key = "101101010010100101101011"

    # Generate ciphertext bits using the encryption function
	ciphertext_bits = function_ek(plaintext, key)
	# Convert ciphertext bits back to readable text
	ciphertext = convert_from_binary(ciphertext_bits)

	return ciphertext

# Putting it altogether to test the function
if __name__ == "__main__":
	result = get_ciphertext()
	print("Plaintext: ", "how do you like computer science")
	print("Key: ", "101101010010100101101011")
	print(result)