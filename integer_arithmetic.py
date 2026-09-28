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
    """
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x

def compare(x: list, y: list) -> list:
    x.strip_zeros()
    y.strip_zeros()

    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    else:
        for i in range(len(x) - 1, -1, -1):
            if x[i] > y[i]:
                return 1
            elif x[i] < y[i]:
                return -1
        return 0

def subtraction(self, x: list, y: list) -> list:
    """
    does something
    """
    n = max(len(x), len(y))
    z = [0]
    c = 0

    for i in range(len(x)):
        if len(y) > i:
            yi = y[i]
        else:
            yi = 0

        zi = x[i] - yi - c

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