BASE = 2**16  # Base for internal representation 


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


def decode(number: str, radix: int) -> list:
    """
    Converts a string number in a given radix in a list of integers representing the number in base 2^16.
    """
    if radix < 2:
        raise ValueError("Radix must be greater than or equal to 2.")

    is_negative = False
    if number.startswith("-"):
        is_negative = True
        number = number[1:]

    chunks = [0]

    for d in number:
        digit = digit_value(d, radix)
        chunks = insert_digit(chunks, digit, radix)

    return is_negative, chunks
    
def insert_digit(chunks, digit, radix):
    """
    Multiplies the whole limb list by `radix` and adds `digit`,
    propagating carry across every limb (not just the last one).
    """
    carry = digit  # the digit being added in is the starting carry
    for i in range(len(chunks)):
        value = chunks[i] * radix + carry
        chunks[i] = value % BASE
        carry = value // BASE
    while carry > 0:
        chunks.append(carry % BASE)
        carry //= BASE
    return chunks
    

def encode(chunks, base, radix):
    """
    Converts a list of chunks in the given base into a string number in the given radix
    """
    if radix < 2:
        raise ValueError("Radix must be greater than or equal to 2.")
    if radix > 16:
        raise ValueError("Radix must be smaller than or equal to 16")
    
    chunks = chunks.copy() # Work on a copy of chunks so the original stays untouched
    result = "" 

    # While loop runs until the whole number has been divided down to zero
    while any(chunks):
        remainder = 0

        # Long Division: Divide the whole number by radix, starting at the biggest chunk
        for i in range(len(chunks) - 1, -1, -1):
            value = remainder * base + chunks[i] # leftover from above + this chunk = number to divide now
            chunks[i] = value // radix # quotient: stays in this chunk
            remainder = value % radix # remainder: passed down to the next chunk

        # The final remainder is the next digit (last digit first)
        if remainder < 10:
            digit = chr(ord("0") + remainder)
        else:
            digit = chr(ord("A") + remainder - 10) # Account for the 10 offset

        result = digit + result # Add the new digits at the front

    if result == "":  # The number is zero
        return "0"

    return result
