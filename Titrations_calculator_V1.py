import math


"""
for debugging purposes. to make it easy to get a print statement showing each 
line is working properly without having to use "yay" each time.
"""
yay = "yay"

class Titration_Input_Error(Exception):
    #another custom input error class
    pass

"""
Below is the basic code for getting the input of 1 variable, making sure it is a float, and giving the user the
appropriate error if they give an incorrect input and guiding them towards being able to provide a correct input. Now to make it iterable 
to utilize a simplified code block to handle all 4 variable inputs. I am thinking by making the user's inputs propagate a list.

def strong_acid_titration_calculator():
    print (yay)

    #the basic algebra is M1V1 = M2V2.... now to write code that can make use of that without 
    #guaranteeing what the unknown is with each iteration. We want to be able to solve for X with X being
    #any of the 4 variables and potentially changing each time. 

    M1 = input(
        "Enter the concentration of the acid in M here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    try:
        M1 = float(M1)
    except ValueError:
        raise Titration_Input_Error(
            "ERROR: Invalid input. Please enter a numeric value for concentration, or 'None' if unknown. "
            "You can use scientific notation in the format of X.Ye-x"
            )
    print (yay)
"""

def strong_acid_titration_calculator():
    print (yay)
    variable_inputs = []
    M1 = input(
        "Enter the concentration of the acid in M here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    V1 = input(
        "Enter the volume of the acid in L here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    M2 = input(
        "Enter the concentration of the base in M here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    V2 = input(
        "Enter the volume of the base in L here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    variable_inputs = [M1, V1, M2, V2]
    floated_variable_inputs = variable_inputs.copy()
    for variable in variable_inputs:
        try:
            if variable == "None":
                variable = None
                floated_variable_inputs.append(variable)
            if variable != None:
                floated_variable_inputs.append(float(variable))
        except ValueError:
            raise Titration_Input_Error(
                "ERROR: Invalid input. Please enter a numeric value for concentration, or 'None' if unknown. "
                "You can use scientific notation in the format of X.Ye-x"
            )
    print (variable_inputs)
    print (floated_variable_inputs)
