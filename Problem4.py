"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 2 - Problem 4

Reference(s): https://www.geeksforgeeks.org/dsa/primality-test-set-3-miller-rabin/
"""

# Import random module for generating random numbers
import random

# Miller-Rabin primality test implementation
def miller_rabin(n, k=8):
    # Handle base cases
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    # Write n-1 as d*2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Witness loop
    for _ in range(k):
        # Pick a random integer a in [2, n-2]
        a = random.randint(2, n - 2)
        # Compute x = a^d mod n
        x = pow(a, d, n)
        # Check if x is 1 or n-1
        if x == 1 or x == n - 1:
            continue
        # Square x s-1 times
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
            
    return True

# Testing function for Miller-Rabin
def test_number(n):
    if miller_rabin(n):
        print(f"the number {n} is a prime")
    else:
        print(f"the number {n} is not a prime")

# Function to find and print three big prime numbers larger than a given start
def find_big_primes(start, count=3):
    print(f"Three prime numbers larger than {start} are:")
    found = 0
    current = start + 1
    if current % 2 == 0: current += 1 
    
    while found < count:
        if miller_rabin(current):
            print(f"Found: {current}")
            found += 1
        current += 2

# Testing the functions
if __name__ == "__main__":
    val = int(input("Enter integer: "))
    test_number(val)
    
    find_big_primes(10**8)