from integer_arithmetic import (
    SignAndMagnitude,
    integer_addition,
    integer_division,
    integer_multiplication,
    integer_subtraction,
    BASE
)


def modular_reduction(a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    q, r = integer_division(a, b)
    return r

def modular_addition(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    sum_ab = integer_addition(a, b)
    return modular_reduction(sum_ab, m)

def modular_subtraction(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    neg_b = SignAndMagnitude(not b.is_negative, b.magnitude.copy())
    diff_ab = integer_subtraction(a, b)
    return modular_reduction(diff_ab, m)

def modular_multiplication(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    prod_ab = integer_multiplication(a, b)
    return modular_reduction(prod_ab, m)

def modular_inversion(a, m) -> SignAndMagnitude:
    """
    Computer the modular inversion of a modulo m using the Extended Euclidean Algorithm 

    Args:
        a (SignAndMagnitude): The number to invert
        m (SignAndMagnitude): The modulus
    Returns:
        SignAndMagnitude: The inverse of a mod m, in {0, ..., m-1}
    Raises:
        ValueError: If gcd(a, m) != 1, so no inverse exists.
    """

    # Work on the copies so the original inputs are untouched
    a_prime = SignAndMagnitude(False, a.magnitude.copy())
    m_prime = SignAndMagnitude(False, m.magnitude.copy())

    # Set up initial values of x1 and x2
    x1 = SignAndMagnitude(False, [1])
    x2 = SignAndMagnitude(False, [0])

    # Run the Euclidean algorithm until the remainder is 0
    while m_prime.magnitude != [0]:
        # q is the quotient and r is the remainder
        q, r = division(a_prime / m_prime)
        a_prime, m_prime = m_prime, r 
        # the old divisor becomes the dividend
        # the remainder becomes the new divisor

        qx2 = primaryMultiplication(q, x2, BASE)
        if qx2.magnitude != [0]: 
            qx2.is_negative = not qx2.is_negative
        x3 = addition(x1, qx2)

        x1, x2 = x2, x3 

    # a_prime now holds gcd(a, m)
    # the inverse only exists if it is 1
    if a_prime.magnitude != [1]:
        raise ValueError("inverse does not exist")

    # x1 can be negative or larger than m, so reduce it into {0, ..., m-1}
    return reduction(x1, m)
