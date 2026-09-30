from radixConversion import SignAndMagnitude


BASE = 2 ** 16



def addition(self, a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    """
    Performs addition of two numbers a and b in base b.
    Keeps track of carry c and propagates it across all digits.
    
    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        SignAndMagnitude: The sum of a and b represented in sign and magnitude.
    """
    n = max(len(a.magnitude), len(b.magnitude)) 
    c = SignAndMagnitude(False, [0])
    carry = 0

    for i in range(n):
        # Pad the shorter list with zeros to make them the same length
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0

        # Temporary c digit at position i
        ci = ai + bi + carry

        # Handle carry if overflow occurs
        if ci >= BASE:
            ci -= BASE
            carry = 1
        else:
            carry = 0

        # Computed digit is appended
        c.magnitude.append(ci)

    # If there's a carry at the end, add a final digit 1
    if carry == 1:
        c.magnitude.append(1)
    return c



def strip_zeros(self, a: SignAndMagnitude) -> list:
    """
    Removes leading zeros from a list of digits.

    Args:
        a (SignAndMagnitude): The list of digits to strip leading zeros from.
    Returns:
        list: The list of digits with leading zeros removed.
    """
    while len(a.magnitude) > 1 and a.magnitude[-1] == 0:
        a.magnitude.pop()
    return a

def compare(a: SignAndMagnitude, b: SignAndMagnitude) -> int:
    """
    Compares two numbers a and b represented as lists of digits.

    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        int: 1 if a > b, -1 if a < b, 0 if a == b.
    """
    # Strip leading zeros from both numbers before comparison
    a = strip_zeros(a)
    b = strip_zeros(b)  

    # Compare lengths first
    if len(a.magnitude) > len(b.magnitude):
        return 1
    elif len(a.magnitude) < len(b.magnitude):
        return -1

    # If lengths are equal, compare digit by digit from the most significant to the least significant
    else:
        for i in range(len(a.magnitude) - 1, -1, -1):
            if a.magnitude[i] > b.magnitude[i]:
                return 1
            elif a.magnitude[i] < b.magnitude[i]:
                return -1
        return 0

def subtraction(self, a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    """
    Performs subtraction of two numbers a and b in base BASE.
    Keeps track of borrow c and propagates it across all digits.

    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        c (SignAndMagnitude): The difference of a and b represented in sign and magnitude.
    """
    n = max(len(a.magnitude), len(b.magnitude))
    c = SignAndMagnitude(False, [0])
    carry = 0

    for i in range(len(a.magnitude)):
        # State the current digit for b
        if len(b.magnitude) > i:
            bi = b.magnitude[i]
        else:
            bi = 0

        # Compute the temporary c digit at position i
        ci = a.magnitude[i] - bi - carry

        # Handle borrow if underflow occurs
        if ci < 0:
            ci += BASE
            carry = 1
        else:
            carry = 0

        c.magnitude.append(ci)
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



def extended_euclidian_algorithm(self, a: SignAndMagnitude, b: SignAndMagnitude) -> tuple:
    """
    Performs the Extended Euclidean Algorithm on two numbers a and b.
    
    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        tuple: A tuple containing the greatest common divisor (gcd) of a and b,
    """
    # EEA requires absolute values of a and b, so we create copies of a and b with positive signs
    a_prime = SignAndMagnitude(False, a.magnitude)
    b_prime = SignAndMagnitude(False, b.magnitude)

    # Set up initial values for x and y
    x1, x2 = 1, 0
    y1, y2 = 0, 1

    # Perform the Extended Euclidean Algorithm
    while b_prime.magnitude != [0]:
        q, r = division(a_prime, b_prime)

        # Update a_prime and b_prime for the next iteration
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
        
    return gcd, x, y
    
