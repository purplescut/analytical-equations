import math
from Titrations_calculator_V1 import strong_acid_titration_calculator, Titration_Input_Error
from Acid_base_calculator_V1 import type_of_eqaution_to_use, Acid_Base_Input_Error
from Dissociations_calculator_V1 import monoprotic_acid_calculator, Dissociations_Input_Error

def main():
    try:
        type_of_eqaution_to_use()
    except Acid_Base_Input_Error as e:
        print(e)
    except Titration_Input_Error as e:
        print(e)
    except Dissociations_Input_Error as e:
        print(e)
    except ZeroDivisionError as e:
        print(f" ERROR: cannot do {e}")
    except Exception as e:
        print(f" ERROR: cannot {e}")

main()
