"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1a
"""

def get_map():
    mapping = {
        'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,
        'F': 5,  'G': 6,  'H': 7,  'I': 8,  'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
        ' ': 26, '.': 27, ',': 28, '?': 29, '(': 30, ')': 31
    }
    return mapping

def convert_to_binary(readable_message):
    mapping = get_map()
    output = ''
    readable_message = readable_message.upper()
    for char in readable_message:
        if char in mapping:
            value = mapping[char]
            output += format(value, '05b')
        else:
            raise ValueError(f"Character '{char}' not in mapping.")
    return output

def convert_from_binary(binary_message):
    mapping = get_map()
    reverse_mapping = {v: k for k, v in mapping.items()}
    output = ''
    for i in range(0, len(binary_message), 5):
        chunk = binary_message[i:i+5]
        value = int(chunk, 2)
        if value in reverse_mapping:
            output += reverse_mapping[value]
        else:
            raise ValueError(f"Binary chunk '{chunk}' does not map to any character.")
    return output

message = "This is a test message."
encoded = convert_to_binary(message)
decoded = convert_from_binary(encoded)

print(f"Original Message: {message.upper()}")
print(f"Binary Message: {encoded}")
print(f"Decoded Message: {decoded}")