from integer_arithmetic import (
    SignAndMagnitude,
    integer_addition,
    integer_division,
    integer_multiplication,
    integer_subtraction,
)


def modular_reduction(a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    q, r = integer_division(a, b)
    return r

def modular_addition(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    sum_ab = integer_addition(a, b)
    return modular_reduction(sum_ab, m)

def modular_subtraction(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    diff_ab = integer_subtraction(a, b)
    return modular_reduction(diff_ab, m)

def modular_multiplication(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    prod_ab = integer_multiplication(a, b)
    return modular_reduction(prod_ab, m)