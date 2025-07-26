import math
from Titrations_calculator_V1 import strong_acid_titration_calculator
from main import main


def type_of_eqaution_to_use():
    equation_type = input(
    "please type either 'strong acid' or 'strong base' for titrations with a strong acid and strong base. " 
"For weak acid/base titrations enter 'monoprotic', 'diprotic', or 'triprotic'."
)
    if equation_type != "strong acid" and "strong base" and "monoprotic" and "diprotic" and "triprotic":
        raise Exception(
        "you do not need to include the '' quotation marks." 
        " Please enter as all lower case exactly as you see in the prompt."
        )
    if equation_type == "strong acid":
        strong_acid_titration_calculator()

main()