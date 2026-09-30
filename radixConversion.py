BASE = 2**16  # Base for internal representation 


class SignAndMagnitude:
    """
    Represents a class for sign and magnitude representation of integers.
    Attributes:
        is_negative (bool): The sign of the integer, either True or False.
        magnitude (list): A list of integers representing the magnitude of the integer.
    """
    def __init__(self, is_negative: bool, magnitude: list):
        """
        Initializes a SignAndMagnitude object with the given sign and magnitude.
        Args:
            is_negative (bool): The sign of the integer, either True or False.
            magnitude (list): A list of integers representing the magnitude of the integer.
        """
        self.is_negative = is_negative
        self.magnitude = magnitude




def digit_value(c, radix):
    """
    Returns the integer value of a digit character for a given radix.
    To do this, we use ASCII values deltas to get the ordinal value.
    Accounts for exceptions where the character is not valid for that radix.
    """
    if "0" <= c <= "9":
        v = ord(c) - ord("0")
    elif "A" <= c <= "F":
        v = ord(c) - ord("A") + 10  # Account for the 10 offset
    else:
        raise ValueError(f"'{c}' is not a valid digit character")
    if v >= radix:
        raise ValueError(f"digit '{c}' (value {v}) is not valid for radix {radix}")
    return v
    
def insert_digit(chunks, digit, radix):
    """
    Multiplies the whole limb list by `radix` and adds `digit`,
    propagating carry across every limb (not just the last one).
    """
    carry = digit  # the digit being added in is the starting carry

    # Propagate carry across all limbs
    for i in range(len(chunks)):
        value = chunks[i] * radix + carry
        chunks[i] = value % BASE
        carry = value // BASE

    while carry > 0:
        chunks.append(carry % BASE)
        carry //= BASE
    return chunks



def decode(number_str: str, radix: int) -> list:
    """
    Converts a string number in a given radix in a list of integers 
    representing the number in base 2^16.
    """
    if radix < 2:
        raise ValueError("Radix must be greater than or equal to 2.")

    number = SignAndMagnitude([0], False)

    # Handle negative numbers
    number.is_negative = False
    if number_str.startswith("-"):
        number.is_negative = True
        number_str = number_str[1:]

    # Iterate character, convert and insert into chunks
    for d in number_str:
        digit = digit_value(d, radix)
        number.magnitude = insert_digit(number.magnitude, digit, radix)
    return number.is_negative, number.magnitude



def encode(chunks, base, radix):
    """
    Converts a list of chunks in the given base into a string number in the given radix
    """
    if radix < 2:
        raise ValueError("Radix must be greater than or equal to 2.")
    if radix > 16:
        raise ValueError("Radix must be smaller than or equal to 16")
    
    chunks = chunks.copy() #work on a copy of chunks so the original stays untouched
    result = "" 

    # While loop runs until the whole number has been divided down to zero
    while any(chunks):
        remainder = 0

        # Long Division: Divide the whole number by radix, starting at the biggest chunk
        for i in range(len(chunks) - 1, -1, -1):
            value = remainder * base + chunks[i] #leftover from above + this chunk = number to divide now
            chunks[i] = value // radix #quotient: stays in this chunk
            remainder = value % radix #remainder: passed down to the next chunk

        # The final remainder is the next digit (last digit first)
        if remainder < 10:
            digit = chr(ord("0") + remainder)
        else:
            digit = chr(ord("A") + remainder - 10) # Account for the 10 offset

        result = digit + result #add the new digits at the front

    if result == "":  # the number is zero
        return "0"

    return result


tests = [
    ("0", 10),
    ("7", 10),
    ("255", 10),
    ("65535", 10),      # biggest single chunk
    ("65536", 10),      # first number that needs two chunks
    ("70000", 10),
    ("123456789", 10),
    ("FF", 16),
    ("1A3", 16),
    ("FFFFFFFF", 16),   # exactly two full chunks
    ("1010", 2),
    ("777", 8),
]

for s, r in tests:
    is_negative, chunks = decode(s, r)
    back = encode(chunks, BASE, r)
    print(s, r, "OK" if back == s else f"FAIL (got {back})")

for s, r in tests:
    is_negative, chunks = decode(s, r)
    value = sum(c * BASE**i for i, c in enumerate(chunks))
    print(s, r, "OK" if value == int(s, r) else "FAIL")

import random

for _ in range(1000):
    n = random.randint(0, 10**30)
    for r in [2, 8, 10, 16]:
        s = format(n, {2: "b", 8: "o", 10: "d", 16: "X"}[r])
        is_negative, chunks = decode(s, r)
        assert encode(chunks, BASE, r) == s, (s, r)
print("all random tests passed")

for bad in [("G", 16), ("9", 8), ("a", 16), ("1", 1)]:
    try:
        decode(*bad)
        print(bad, "FAIL (no error raised)")
    except ValueError:
        print(bad, "OK (error raised)")