import math


"""
for debugging purposes. to make it easy to get a print statement showing each 
line is working properly without having to use "yay" each time.
"""
yay = "yay"

class Titration_Input_Error(Exception):
    #another custom input error class
    pass


def strong_acid_titration_calculator(): #The code for the calculator to do the simple strong acid with strong base calculations
    variable_inputs = [] #An empty list to propagate with the user inputs
    M1 = input(
        "Enter the concentration of the acid (in M) here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    V1 = input(
        "Enter the volume of the acid (in Liters) here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    M2 = input(
        "Enter the concentration of the base (in M) here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    V2 = input(
        "Enter the volume of the base (in Liters) here. Only include the numeric value."
        " If this is your unknown enter 'None'."
        )
    variable_inputs = [M1, V1, M2, V2] #the list of variables propagated with the user inputs
    floated_variable_inputs = [] #an empty list to be filled with the variables after turning them into floats
    for variable in variable_inputs: # a loop to turn each user input into a float and propagate the new lost with those floats. The user entered None type is the variable to be solved for.
        try:
            if variable == "None":
                variable = None
                floated_variable_inputs.append(variable)
            if variable != None:
                floated_variable_inputs.append(float(variable))
        except ValueError:
            raise Titration_Input_Error(
                "ERROR: Invalid input. Please enter a numeric value only for concentration. Or 'None' if it is the unknown. "
                "You can use scientific notation in the format of X.Ye-x"
            ) #this should be caught and handled in the main.py form in the main function to tell the user if they have made an expected error and guide them towards how to correct it
    M1 = floated_variable_inputs[0]
    V1 = floated_variable_inputs[1]
    M2 = floated_variable_inputs[2]
    V2 = floated_variable_inputs[3]
    #Below is the code of the algebra to solve for X for the 4 variables that can potentially be unknown. 
    if M1 == None:
        M1 = M2*V2/V1
        print (f"The concentration of your acid is {M2}*{V2}/{V1} which equals {M1}")
    if V1 == None:
        V1 = M2*V2/M1
        print (f"The volume of your acid is {M2}*{V2}/{M1} which equals {V1}")
    if M2 == None:
        M2 = M1*V1/V2
        print (f"The concentration of your base is {M1}*{V1}/{V2} which equals {M2}")
    if V2 == None:
        V2 = M1*V1/M2
        print (f"The volume of your base is {M1}*{V1}/{V2} which equals {V2}")




