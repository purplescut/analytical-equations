import math


"""
for debugging purposes. to make it easy to get a print statement showing each 
line is working properly without having to use "yay" each time.
"""
yay = "yay"

class Titration_Input_Error(Exception):
    #Another custom input error class
    pass


def solve_for_M1(M1, V1, M2, V2): #A function to contain the algebra to solve for a variable, in this case M1, from M1V1=M2V2
    M1 = M2*V2/V1
    return print (f"The concentration of your acid is {M2}*{V2}/{V1} which equals {M1} M")
def solve_for_V1(M1, V1, M2, V2): #A function to contain the algebra to solve for a different variable from the M1V1=M2V2 equation
    V1 = M2*V2/M1
    return print (f"The volume of your acid is {M2}*{V2}/{M1} which equals {V1} L")
def solve_for_M2(M1, V1, M2, V2): #A fuction to contain the algebra to solve for M2 from M1V1=M2V2
    M2 = M1*V1/V2
    return print (f"The concentration of your base is {M1}*{V1}/{V2} which equals {M2} M")
def solve_for_V2(M1, V1, M2, V2): #A function to contain the algebra to solve for V2 from M1V1=M2V2
    V2 = M1*V1/M2
    return print (f"The volume of your base is {M1}*{V1}/{M2} which equals {V2} L")

def strong_acid_titration_calculator(): #The code for the calculator to do the simple strong acid with strong base calculations
    variable_inputs = [] #An empty list to propagate with the user inputs
    M1 = input(
        "Enter the concentration of the acid (in M) here. Only include the numeric value."
        " If this is your unknown enter 'None'.: "
        )
    V1 = input(
        "Enter the volume of the acid (in Liters) here. Only include the numeric value."
        " If this is your unknown enter 'None'.: "
        )
    M2 = input(
        "Enter the concentration of the base (in M) here. Only include the numeric value."
        " If this is your unknown enter 'None'.: "
        )
    V2 = input(
        "Enter the volume of the base (in Liters) here. Only include the numeric value."
        " If this is your unknown enter 'None'.: "
        )
    variable_inputs = [M1, V1, M2, V2] #the list of variables propagated with the user inputs
    floated_variable_inputs = [] #an empty list to be filled with the variables after turning them into floats
    for variable in variable_inputs: # a loop to turn each user input into a float and propagate the new lost with those floats. The user entered None type is the variable to be solved for.
        try:
            if variable == "None":
                variable = None
                floated_variable_inputs.append(variable)
            elif variable != None:
                floated_variable_inputs.append(float(variable))
        except ValueError:
            raise Titration_Input_Error(
                "ERROR: Invalid input. Please enter a numeric value only for concentration. Or 'None' if it is the unknown. "
                "You can use scientific notation in the format of X.Ye-x"
            ) #this should be caught and handled in the main.py form in the main function to tell the user if they have made an expected error and guide them towards how to correct it
    solve_simple_algebra(*floated_variable_inputs)
    
def solve_simple_algebra(M1, V1, M2, V2): #This function accepts 4 integers or floats as inputs and then decides which variable needs to be solved for 
    if M1 == None: solve_for_M1(M1, V1, M2, V2) # and calls the appropriate function whilst passing it the variables. 
    if V1 == None: solve_for_V1(M1, V1, M2, V2)
    if M2 == None: solve_for_M2(M1, V1, M2, V2)
    if V2 == None: solve_for_V2(M1, V1, M2, V2)

#Below is a function to find the equivalence point in a monoprotic weak acid titration.
def get_weak_analyte_strong_titrant_equivalence_point():
        try:
            Ma=float(input("Enter the concentration of the weak analyte: ")) 
            Va=float(input("Enter the volume of the weak analyte: "))       
            Mb=float(input("Enter the concentration of the strong titrant: "))
        except ValueError:
            return print("Invalid input. Please enter numeric values for concentration and volume. ")
        if Mb == 0:
            return print("ERROR: You cannot enter 0 as the titrant concentration. ")
        decimals =input("Enter the amount of decimal places you want the answer rounded to. Enter 'none' for the non-rounded answer: ")
        if decimals.lower() == "none":
            return print(f"The equivalence point will be reached at {Ma*Va/Mb} L of titrant added. ")
        else:
            try:
                decimals = int(float(decimals))
                return print(f"The equivalence point will be reached at {Ma*Va/Mb:.{decimals}f} L of titrant added. ")
            except ValueError:
                return print("Invalid input. Please enter a number or 'none'. ")


def calculate_initial_pH(analyte_concentration = None, analyte_Ka_value = None,): #A function to hold the math for calculating initial pH, and 
    if analyte_concentration==None:                                               #allowing it to be called for user inputs.
        analyte_concentration = float(input(f"Enter the concentration of your analyte: "))
    if analyte_Ka_value==None:
        analyte_Ka_value=float(input(f"Enter the Ka value for your anayte here: "))
    return print(f"The initial pH is {-math.log10(math.sqrt(analyte_concentration*analyte_Ka_value))}. This is calculated by \
                 solving for x in Ka = x^2/({analyte_concentration}-x) \
                     where x is negligible. This can be rearranged\
        as x = sqrt({analyte_concentration}*{analyte_Ka_value}). Then pH is the -log(x), which in this case, \
            is {-math.log10(math.sqrt(analyte_concentration*analyte_Ka_value))}. ")



def weak_acid_pH_calculator(): #This function should be able to handle doing titrations of a weak acid (and potentially later on with a weak base also)
    try:
        analyte_volume = float(input("Enter the volume of the analyte in L: "))
        analyte_concentration = float(input("Enter the concentration of the analyte in M: "))
        titrant_volume = float(input("Enter the volume of titrant being added in L"
                                    "If you want the initial dissociation, with no titrant added, enter '0': "))
        titrant_concentration = float(input("Enter the concentration of titrant in M: "))
        analyte_Ka_value = float(input("Enter the Ka for your analyte here. Scientific notation is acceptable in the format of X.Ye-x: "))
        pKa = -math.log10(analyte_Ka_value)
        if analyte_concentration <= 0 or titrant_concentration <= 0:
            return print("Input Error: Concentrations must be positive numbers.")
    except ValueError:
        return print("Input Error: Please enter numerical values only. Check your units and make sure your input is in the correct units. ")
    if titrant_volume == 0:
        calculate_initial_pH(analyte_concentration, analyte_Ka_value)
    if (analyte_concentration*analyte_volume) == (titrant_concentration*titrant_volume):
        return print(
                    f"The pH is {14-(-math.log10(math.sqrt((analyte_concentration*analyte_volume)/(analyte_volume+titrant_volume)*1e-14/analyte_Ka_value)))}. This is the \
                     equivalence point. At the equivalence point there is no weak analyte left, and no strong titrant left after the reaction completes.\
                      This mean the conjugate is all that is left. To get the pH then you must calculate the dissociation of the weak conjugate. Since the\
                        starting analyte was an acid, the conjugate is a weak base. To do this, you have to calculate the Kb of the conjugate using the equation \
                         Kb = 1e-14/Ka. The dissociation of a weak base gives a pOH result that must be converted to a pH by the equation 14-pOH = pH. "
                    )
    if abs((titrant_concentration * titrant_volume) - 0.5 * (analyte_concentration * analyte_volume)) < 1e-6:
        return print(f"The pH is {pKa}. This is the half equivalence point. The half equivalence point for this reaction is at {(1/2)*titrant_volume}. \
                     At the half equivalence point pH is always equal to pKa.")
    if (analyte_concentration*analyte_volume) < (titrant_concentration*titrant_volume):
        return print(f"The pH is {14-(-math.log10(((titrant_concentration*titrant_volume)-(analyte_concentration*analyte_volume))/(titrant_volume+analyte_volume)))}. This is\
                     after the equivalence point so the pH is mainly dictated by the concentration of the left-over strong titrant. \
                     This can be calculated by determining the moles of titrant, subtracting the moles of analyte, and dividing the remaining moles of \
                     titrant by the volume of the solution, which is the volume of analyte plus the volume of titrant. Then the -log of that concentration is pH")
    if(analyte_concentration * analyte_volume) > (titrant_concentration * titrant_volume):
        return print(f"The pH is {pKa + math.log10((titrant_concentration*titrant_volume)/((analyte_concentration*analyte_volume)-(titrant_volume*titrant_concentration)))}. \
                     This is calculated by determining the moles of acid present, {analyte_concentration} * {analyte_volume}, subtracting from that the moles of base added, \
                        {titrant_concentration} * {titrant_volume}, which gives {(analyte_concentration*analyte_volume)-(titrant_volume*titrant_concentration)}. Then the \
                             Henderson-Hasselbalch equation can be used where [A-] is the moles of base added and [HA] is the moles of acid left. ")
    

    



def main():
   pass

if __name__ == "__main__":
    main()
