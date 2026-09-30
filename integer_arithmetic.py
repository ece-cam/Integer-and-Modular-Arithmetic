BASE = 2**16


def addition(self, a: list, b: list) -> list:
    """
    Performs addition of two numbers a and b in base b.
    Keeps track of carry c and propagates it across all digits.
    
    Args:
        a (list): The first number represented as a list of digits.
        b (list): The second number represented as a list of digits.
    Returns:
        list: The sum of a and b represented as a list of digits.
    """
    n = max(len(a), len(b)) 
    c = [0]
    c = 0

    for i in range(n):
        # Pad the shorter list with zeros to make them the same length
        xi = a[i] if i < len(a) else 0
        yi = b[i] if i < len(b) else 0

        # Temporary c digit at position i
        zi = xi + yi + c

        # Handle carry if overflow occurs
        if zi >= BASE:
            zi -= BASE
            c = 1
        else:
            c = 0

        # Computed digit is appended
        c.append(zi)

    # If there's a carry at the end, add a final digit 1
    if c == 1:
        c.append(1)
    return c


def strip_zeros(self, a: list) -> list:
    """
    Removes leading zeros from a list of digits.

    Args:
        a (list): The list of digits to strip leading zeros from.
    Returns:
        list: The list of digits with leading zeros removed.
    """
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def compare(a: list, b: list) -> list:
    """
    Compares two numbers a and b represented as lists of digits.

    Args:
        a (list): The first number represented as a list of digits.
        b (list): The second number represented as a list of digits.
    Returns:
        int: 1 if a > b, -1 if a < b, 0 if a == b.
    """
    # Strip leading zeros from both numbers before comparison
    a = strip_zeros(a)
    b = strip_zeros(b)

    # Compare lengths first
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1

    # If lengths are equal, compare digit by digit from the most significant to the least significant
    else:
        for i in range(len(a) - 1, -1, -1):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        return 0

def subtraction(self, a: list, b: list) -> list:
    """
    Performs subtraction of two numbers a and b in base BASE.
    Keeps track of borrow c and propagates it across all digits.

    Args:
        a (list): The first number represented as a list of digits.
        b (list): The second number represented as a list of digits.
    Returns:
        c (list): The difference of a and b represented as a list of digits.
    """
    n = max(len(a), len(b))
    c = [0]
    c = 0

    for i in range(len(a)):
        # State the current digit for b
        if len(b) > i:
            yi = b[i]
        else:
            yi = 0

        # Compute the temporary c digit at position i
        zi = a[i] - yi - c

        # Handle borrow if underflow occurs
        if zi < 0:
            zi += BASE
            c = 1
        else:
            c = 0

        c.append(zi)
    return strip_zeros(c)







def primaryMultiplication(a,b,base):
    m=len(a)
    n=len(b)
    z = [0] * (m + n)   
    for i in range(0, m):  
        c=0
        for j in range(0, n):  
          t = z[i+j] + a[i]*b[j] + c
          c = t // base               
          z[i + j] = t - c * base        
          z[i + n] = c     
        z[i + n] = c
    return strip_zeros(z)
 
def pad(a, n):
    #pad function, used for making a number a n digits long.
    return a + [0] * (n - len(a))



def extended_auclidian_algorithm(self, a: list, b: list) -> tuple:

    a.sign = postive
    b.sign = postive

    x1 = 1, x2 = 0
    y1 = 0, y2 = 1

    while b_prime != 0:
        q, r = division(a_prime, b_prime)
        a_prime = b_prime
        b_prime = r

        x3 = x1 - q * x2
        y3 = y1 - q * y2

        x1, x2 = x2, x3
        y1, y2 = y2, y3


    gcd = a_prime
    if a >= 0:
        x = x1
    else:
        x = -x1
    if b >= 0:
        y = y1
    else:
        y = -y1
        
    return gcd, a, b
    
