import math
from Titrations_calculator_V1 import strong_acid_titration_calculator, Titration_Input_Error
from Acid_base_calculator_V1 import type_of_eqaution_to_use, Acid_Base_Input_Error

def main():
    try:
        type_of_eqaution_to_use()
    except Acid_Base_Input_Error as e:
        print (e)
    except Titration_Input_Error as e:
        print (e)

main()