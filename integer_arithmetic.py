from radixConversion import SignAndMagnitude


BASE = 2 ** 16



def addition(a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    """
    Performs addition of two numbers a and b in base b.
    Keeps track of carry c and propagates it across all digits.
    
    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        SignAndMagnitude: The sum of a and b represented in sign and magnitude.
    """
    if a.is_negative != b.is_negative:
        if compare(a, b) >= 0:
            c = subtraction(a, b)
            c.is_negative = a.is_negative
        else:
            c = subtraction(b, a)
            c.is_negative = b.is_negative
        return c

    n = max(len(a.magnitude), len(b.magnitude)) 
    c = SignAndMagnitude(False, [])
    carry = 0

    for i in range(n):
        # Pad the shorter list with zeros to make them the same length
        ai = a.magnitude[i] if i < len(a.magnitude) else 0
        bi = b.magnitude[i] if i < len(b.magnitude) else 0

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

    c.is_negative = a.is_negative
    return c



def strip_zeros(a: SignAndMagnitude) -> list:
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

def subtraction(a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    """
    Performs subtraction of two numbers a and b in base BASE.
    Keeps track of borrow c and propagates it across all digits.

    Args:
        a (SignAndMagnitude): The first number represented in sign and magnitude.
        b (SignAndMagnitude): The second number represented in sign and magnitude.
    Returns:
        c (SignAndMagnitude): The difference of a and b represented in sign and magnitude.
    """
    c = SignAndMagnitude(False, [])
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







def primaryMultiplication(a: SignAndMagnitude, b: SignAndMagnitude,base)-> SignAndMagnitude:
    m=len(a.magnitude)
    n=len(b.magnitude)
    z = SignAndMagnitude( a.is_negative != b.is_negative,[0] * (m + n))
    for i in range(0, m):  
        c=0
        for j in range(0, n):  
          t = z.magnitude[i+j] + a.magnitude[i]*b.magnitude[j] + c
          c = t // base               
          z.magnitude[i + j] = t - c * base        
        z.magnitude[i + n] = c

    z = strip_zeros(z)
    if z.magnitude == [0]:       
        z.is_negative = False
    return z
 
 
def pad(a, n):
    #pad function, used for making a number a n digits long.
    return a + [0] * (n - len(a))

def karatsuba(a: SignAndMagnitude, b: SignAndMagnitude, n, base) -> SignAndMagnitude:
    if n == 1:
        return primaryMultiplication(a, b, base)

    if n % 2 == 1:                              
        n = n + 1
    
    a = pad(a.magnitude, n)
    b = pad(b.magnitude, n)
        
    h = n // 2
    a_low, a_high = SignAndMagnitude(False, a.magnitude[:h]), SignAndMagnitude(False, a.magnitude[h:])
    b_low, b_high = SignAndMagnitude(False, b.magnitude[:h]), SignAndMagnitude(False, b.magnitude[h:])

    z2 = karatsuba(a_high, b_high, h, base)              
    z0 = karatsuba(a_low, b_low, h, base)  

    sum_a = addition(a_high, a_low)
    sum_b = addition(b_high, b_low)      

    z1_recursive = karatsuba(sum_a, sum_b, h, base)
    z1 = subtraction(subtraction(z1_recursive, z0), z2)   

    shifted_z2 = SignAndMagnitude(False, [0] * n + z2.magnitude)
    shifted_z1 = SignAndMagnitude(False, [0] * h + z1.magnitude)
    
    z = addition(addition(shifted_z2, shifted_z1), z0)
 
    z = strip_zeros(z)
    z.is_negative = (a.is_negative != b.is_negative) and z.magnitude != [0]
    return z


def division(a: SignAndMagnitude, b: SignAndMagnitude) -> tuple:
    """
    Performs division of two numbers a and b in base BASE.

    Args:
        a (SignAndMagnitude): The dividend represented in sign and magnitude.
        b (SignAndMagnitude): The divisor represented in sign and magnitude.
    Returns:
        tuple: A tuple containing the quotient and remainder of the division.
    """
    # Initiate the positive copies of a and b
    a_abs = SignAndMagnitude(False, a.magnitude.copy())
    b_abs = SignAndMagnitude(False, b.magnitude.copy())

    m, n = len(a_abs.magnitude), len(b_abs.magnitude)
    k = m - n + 1   # Number of digits in the quotient

    r = a_abs.copy()
    q_digits = []
    q_digits = pad(q_digits, max(k, 1))

    for i in range(k - 1, -1, -1):
        shifted = SignAndMagnitude(False, [0] * i + b_abs.magnitude)   # b * BASE^i
        qi = 0
        while compare(r, shifted) != -1:   # while r >= b * BASE^i
            r = subtraction(r, shifted)
            qi += 1
        q_digits[i] = qi

    while len(q_digits) > 1 and q_digits[-1] == 0:   # strip leading zeros
        q_digits.pop()
    q = SignAndMagnitude(False, q_digits)

    # Sign fix so that 0 <= r < |b|
    if a.negative and r.magnitude != [0]:
        q = addition(q, SignAndMagnitude(False, [1]))
        r = subtraction(b_abs, r)

    q.negative = (a.negative != b.negative) and q.magnitude != [0]
    return q, r


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
    
