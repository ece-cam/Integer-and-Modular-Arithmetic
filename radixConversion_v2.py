DIGIT_VALUES = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

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



class radixConversionv2:
    def __init__(self, number, base):
        self.number = number

        if not base >= 2:
            raise ValueError("Base must be greater than or equal to 2.")
        self.base = base
    
    def encode():
        

    def decode():
        pass