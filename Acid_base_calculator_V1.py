import math
from Titrations_calculator_V1 import strong_acid_titration_calculator, weak_acid_pH_calculator, calculate_equivalence_point
from Dissociations_calculator_V1 import monoprotic_acid_dissociation_calculator

class Acid_Base_Input_Error(Exception):
    #custom input error exception
    def __init__(self):
        pass

def type_of_equation_to_use():
    equation_type = input(
    "please type either 'strong acid' or 'strong base' for titrations with a strong acid and strong base. " 
    "For weak acid/base titrations enter 'monoprotic', 'diprotic', or 'triprotic'."
    "For calculating concentrations in dissociation reactions enter 'dissociations'"
    ).lower()
    if equation_type not in ["strong acid", "strong base", "monoprotic", "diprotic", "triprotic", "dissociations", "dissociation"]:
        raise Acid_Base_Input_Error( "ERROR: you do not need to include the '' quotation marks. " \
        "Please check your spelling. The input is not capitalization sensitive, but is spelling sensitive. ")
    if equation_type in ("strong acid", "strong base",):
        strong_acid_titration_calculator()
    if equation_type in ("dissociation", "dissociations",):
        monoprotic_acid_dissociation_calculator()
    if equation_type in ("monoprotic",):
        which_equation = input(f"Would you like to find the equivalence point, or do a titration reaction?\
                                       For equivalence point, enter 'equivalence' or for titration reaction enter 'titration'. ")
        if which_equation.lower() in ("titration"):
            weak_acid_pH_calculator()
        if which_equation.lower() in ("equivalence"):
            calculate_equivalence_point()
    
def main():
    type_of_equation_to_use()


if __name__ == "__main__":
    main()