##
# 2WF90 Algebra for Security -- Software Assignment 1 
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:
# 56
#
# Author names and student IDs:
# Fabrizio Bulzinetti (2322234) 
# Eda Gunes (2246945)
# Defne Aydin (2284553)
# Ece Camurlu (2244098)
##

# Import built-in json library for handling input/output 
import json
from radixConversion import decode, encode, BASE, SignAndMagnitude
from integer_arithmetic import extended_euclidian_algorithm, integer_division, integer_karatsuba, strip_zeros, integer_addition, integer_subtraction, integer_multiplication



def strToSignAndMagnitude(num_str: str, radix: int) -> SignAndMagnitude:
    return decode(num_str, radix)

def signAndMagnitudeToStr(num: SignAndMagnitude, radix: int) -> str:
    if num.is_negative:
        if strip_zeros(num).magnitude == [0]:
            return "0"
        return "-" + encode(num.magnitude, BASE, radix)
    return encode(num.magnitude, BASE, radix)




def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###
    answer = {"answer": None}


    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            # Solve integer arithmetic addition exercise
            integer_addition()
        elif exercise["operation"] == "subtraction":
            # Solve integer arithmetic subtraction exercise
            integer_subtraction()
        elif exercise["operation"] == "multiplication_primary":
            # Solve integer arithmetic multiplication exercise
            integer_multiplication()
        elif exercise["operation"] == "multiplication_karatsuba":
            # Solve integer arithmetic karatsuba multiplication exercise
            integer_karatsuba()
        elif exercise["operation"] == "extended_euclidean_algorithm":
            # Solve integer arithmetic extended euclidean algorithm exercise
            extended_euclidian_algorithm()
        # et cetera
    else: # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to solve
        if exercise["operation"] == "reduction":
            # Solve modular arithmetic reduction exercise
            pass
        # et cetera


    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)

# You can call your function from here
# Please do not *run* code outside this block
# You can however define other functions or constants
if __name__ == '__main__':
    solve_exercise('Simple/Exercises/exercise0.json', 'Simple/Answers/answer0.json')