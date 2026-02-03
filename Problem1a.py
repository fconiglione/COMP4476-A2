"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 1a
"""

def get_map():
    # Defining the Z32 mapping
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
    # Turning text into its 5-bit binary representation
    mapping = get_map()
    output = ''
    # Force uppercase to match mapping keys
    readable_message = readable_message.upper()
    for char in readable_message:
        if char in mapping:
            value = mapping[char]
            # format(value, '05b') ensures the binary result is 5 bits long with leading zeros
            output += format(value, '05b')
        else:
            raise ValueError(f"Character '{char}' not in mapping.")
    return output

def convert_from_binary(binary_message):
    # Turning 5-bit binary representation back into text
    mapping = get_map()
    # Creating a reverse dictionary for decoding
    reverse_mapping = {v: k for k, v in mapping.items()}
    output = ''
    # iterate through the string with a step of 5
    for i in range(0, len(binary_message), 5):
        chunk = binary_message[i:i+5]
        # Convert to integer
        value = int(chunk, 2)
        if value in reverse_mapping:
            output += reverse_mapping[value]
        else:
            raise ValueError(f"Binary chunk '{chunk}' does not map to any character.")
    return output

# Testing the code
if __name__ == "__main__":

    message = "This is a test message."
    encoded = convert_to_binary(message)
    decoded = convert_from_binary(encoded)

    print(f"Original Message: {message.upper()}")
    print(f"Binary Message: {encoded}")
    print(f"Decoded Message: {decoded}")