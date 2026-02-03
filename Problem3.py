"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 3
"""

from Problem1a import convert_to_binary, convert_from_binary
from Problem1b import function_f, x_or

def encrypt_block(block: str, key: str) -> str:
	if len(block) != 16:
		raise ValueError("Block must be 16 bits")
	if len(key) < 24:
		raise ValueError("Key must be at least 24 bits (two 12-bit subkeys)")

	K1 = key[:12]
	K2 = key[12:24]

	L = block[:8]
	R = block[8:]

	f1 = function_f(R, K1)
	L1 = R
	R1 = x_or(L, f1)

	f2 = function_f(R1, K2)
	L2 = R1
	R2 = x_or(L1, f2)
	return L2 + R2


def pad_to_block_multiple(bits: str, block_size: int = 16) -> str:
    while len(bits) % block_size != 0:
        bits += "0"
    return bits

def cbc_encrypt(plaintext: str, key: str, iv: str):
    normalized = plaintext.replace("\n", " ")

    p_bits = convert_to_binary(normalized)
    p_bits = pad_to_block_multiple(p_bits, 16)

    ciphertext_blocks = []
    prev = iv
    
    for i in range(0, len(p_bits), 16):
        block = p_bits[i:i+16]
        xored = x_or(block, prev)
        c_block = encrypt_block(xored, key)
        ciphertext_blocks.append(c_block)
        prev = c_block

    c_bits = "".join(ciphertext_blocks)
    c_text = convert_from_binary(c_bits)
    
    return c_bits, c_text


if __name__ == "__main__":
	plaintext = (
		"cryptography is an important tool for network security. but there are other issues for network security."
	)

	key = "101111010101110011001100"
	iv = "0000000000000000"

	c_bits, c_text = cbc_encrypt(plaintext, key, iv)

	print("Plaintext:", plaintext)
	print("\nKey (24 bits):", key)
	print("IV (16 bits):", iv)
	print("\nCiphertext (bits):")
	print(c_bits)
	print("\nCiphertext (mapped text):")
	print(c_text)
