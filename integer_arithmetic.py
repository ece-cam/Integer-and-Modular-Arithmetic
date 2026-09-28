BASE = 2**16


def addition(self, x: list, y: list) -> list:
    """
    Performs addition of two numbers x and y in base b.
    Keeps track of carry c and propagates it across all digits.
    
    Args:
        x (list): The first number represented as a list of digits.
        y (list): The second number represented as a list of digits.
    Returns:
        list: The sum of x and y represented as a list of digits.
    """
    n = max(len(x), len(y)) 
    z = [0]
    c = 0

    for i in range(n):
        # Pad the shorter list with zeros to make them the same length
        xi = x[i] if i < len(x) else 0
        yi = y[i] if i < len(y) else 0

        # Temporary z digit at position i
        zi = xi + yi + c

        # Handle carry if overflow occurs
        if zi >= BASE:
            zi -= BASE
            c = 1
        else:
            c = 0

        # Computed digit is appended
        z.append(zi)

    # If there's a carry at the end, add a final digit 1
    if c == 1:
        z.append(1)

    return z


def strip_zeros(self, x: list) -> list:
    """
    Removes leading zeros from a list of digits.

    Args:
        x (list): The list of digits to strip leading zeros from.
    Returns:
        list: The list of digits with leading zeros removed.
    """
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x

def compare(x: list, y: list) -> list:
    """
    Compares two numbers x and y represented as lists of digits.

    Args:
        x (list): The first number represented as a list of digits.
        y (list): The second number represented as a list of digits.
    Returns:
        int: 1 if x > y, -1 if x < y, 0 if x == y.
    """
    # Strip leading zeros from both numbers before comparison
    x = strip_zeros(x)
    y = strip_zeros(y)

    # Compare lengths first
    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1

    # If lengths are equal, compare digit by digit from the most significant to the least significant
    else:
        for i in range(len(x) - 1, -1, -1):
            if x[i] > y[i]:
                return 1
            elif x[i] < y[i]:
                return -1
        return 0

def subtraction(self, x: list, y: list) -> list:
    """
    Performs subtraction of two numbers x and y in base BASE.
    Keeps track of borrow c and propagates it across all digits.

    Args:
        x (list): The first number represented as a list of digits.
        y (list): The second number represented as a list of digits.
    Returns:
        z (list): The difference of x and y represented as a list of digits.
    """
    n = max(len(x), len(y))
    z = [0]
    c = 0

    for i in range(len(x)):
        # State the current digit for y
        if len(y) > i:
            yi = y[i]
        else:
            yi = 0

        # Compute the temporary z digit at position i
        zi = x[i] - yi - c

        # Handle borrow if underflow occurs
        if zi < 0:
            zi += BASE
            c = 1
        else:
            c = 0

        z.append(zi)
    
    return strip_zeros(z)







def multiplication(self):
    pass

def division(self):
    pass