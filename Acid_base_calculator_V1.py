import math
from Titrations_calculator_V1 import strong_acid_titration_calculator, Titration_Input_Error
from Dissociations_calculator_V1 import monoprotic_acid_dissociation_calculator, Dissociations_Input_Error

class Acid_Base_Input_Error(Exception):
    #custom input error exception
    def __init__(self):
        pass

def type_of_eqaution_to_use():
    equation_type = input(
    "please type either 'strong acid' or 'strong base' for titrations with a strong acid and strong base. " 
    "For weak acid/base titrations enter 'monoprotic', 'diprotic', or 'triprotic'."
    "For calculating the concentration of dissociations enter 'dissociations'"
    ).lower()
    if equation_type not in ["strong acid", "strong base", "monoprotic", "diprotic", "triprotic", "dissociations", "dissociation"]:
        raise Acid_Base_Input_Error( 
            "ERROR: you do not need to include the '' quotation marks. " \
            "Please check your spelling. The input is not capitalization sensitive, but is spelling sensitive. " 
        )
    if equation_type in ("strong acid", "strong base"):
        strong_acid_titration_calculator()

    if equation_type in ("dissociation", "dissociations"):
        monoprotic_acid_dissociation_calculator()
    else:
        return print("yay")

def main():
    type_of_eqaution_to_use()


if __name__ == "__main__":
    main()