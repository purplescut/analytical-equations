import math
from Titrations_calculator_V1 import strong_acid_titration_calculator, Titration_Input_Error

class Acid_Base_Input_Error(Exception):
    #custom input error exception
    pass

def type_of_eqaution_to_use():
    equation_type = input(
    "please type either 'strong acid' or 'strong base' for titrations with a strong acid and strong base. " 
"For weak acid/base titrations enter 'monoprotic', 'diprotic', or 'triprotic'."
)
    if equation_type not in ["strong acid", "strong base", "monoprotic", "diprotic", "triprotic"]:
        raise Acid_Base_Input_Error( 
            "ERROR: you do not need to include the '' quotation marks. " 
            "Check your spelling and please enter as all lower case exactly as you see in the prompt. "
            
        )
    if equation_type in ("strong acid", "strong base"):
        try:
            strong_acid_titration_calculator()
        except Exception as e:
            print(e)
        except Titration_Input_Error as e:
            print (e)
