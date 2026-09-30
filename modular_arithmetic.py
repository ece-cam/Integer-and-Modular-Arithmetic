from integer_arithmetic import (
    SignAndMagnitude, 
    addition, 
    primaryMultiplication, 
    subtraction, 
    division, 
    compare,
    BASE
)


def modular_reduction(a: SignAndMagnitude, b: SignAndMagnitude) -> SignAndMagnitude:
    q, r = division(a, b)
    return r

def modular_addition(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    sum_ab = addition(a, b)
    return modular_reduction(sum_ab, m)

def modular_subtraction(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    diff_ab = subtraction(a, b)
    return modular_reduction(diff_ab, m)

def modular_multiplication(a: SignAndMagnitude, b: SignAndMagnitude, m: SignAndMagnitude) -> SignAndMagnitude:
    prod_ab = primaryMultiplication(a, b, BASE)
    return modular_reduction(prod_ab, m)