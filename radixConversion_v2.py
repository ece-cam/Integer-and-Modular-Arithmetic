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

BASE = 2**16  # Base for internal representation 

def encode(number: str, radix: int) -> list:
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

        old_value = chunks[-1]
        value = old_value * radix + digit

        if value >= BASE:
            carry = value // BASE
            chunks[-1] = value % BASE
            chunks.append(carry)
        else:
            chunks[-1] = value

        old_value = value


class radixConversionv2:
    
    def __init__(self, number, base):
        self.number = number
        if not self

        if not base >= 2:
            raise ValueError("Base must be greater than or equal to 2.")
        self.base = base
    
    
        

    def decode(digits, base):
        """
        Converts a list of digits in the given base into its numeric value.
        """
        value = 0
        for d in digits:
            value = value * base + d
        return value
