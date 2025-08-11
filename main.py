import math
from Titrations_calculator_V1 import Titration_Input_Error
from Acid_base_calculator_V1 import type_of_equation_to_use, Acid_Base_Input_Error
from Dissociations_calculator_V1 import Dissociations_Input_Error

def main():
    while True:
        try:
            type_of_equation_to_use()
            break #Exit after successful run
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

if __name__ == "__main__":
    main()

    