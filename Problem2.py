from Problem1a import convert_from_binary
from Problem1b import function_f, x_or

def decrypt_dk(ciphertext_bits, key):
    K1 = key[:12]
    K2 = key[12:]
    
    plaintext_bits = ""

    for i in range(0, len(ciphertext_bits), 16):
        block = ciphertext_bits[i:i+16]
        L2 = block[:8]
        R2 = block[8:]

        f2_out = function_f(L2, K2)
        L1 = x_or(R2, f2_out)
        R1 = L2

        f1_out = function_f(L1, K1)
        L0 = x_or(R1, f1_out)
        R0 = L1

        plaintext_bits += L0 + R0

    return plaintext_bits

if __name__ == "__main__":
    original_text = "how do you like computer science"
    key = "101101010010100101101011"

    from Problem1c import function_ek
    cipher_bits = function_ek(original_text, key)
    
    decrypted_bits = decrypt_dk(cipher_bits, key)
    
    final_text = convert_from_binary(decrypted_bits)
    
    print(f"Original:  {original_text.upper()}")
    print(f"Decrypted: {final_text}")
    
    if original_text.upper() in final_text.upper():
        print("Encryption is correct!")