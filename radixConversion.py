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
    Converts a list of digits in the given base into its numeric value
    """
    if radix < 2:
        raise ValueError("Radix must be greater than or equal to 2.")
    
    chunks = chunks[:]
    digits = []

    while not (len(chunks) == 1 and chunks[0] == 0):
        digit, chunks = extract_digit(chunks, radix)
        digits.append(digit_char(digit))

    if not digits:
        digits.append("0")
    if is_negative:
        digits.append("-")

    return "".join(reversed(digits))
