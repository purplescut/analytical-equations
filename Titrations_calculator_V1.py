import math
from quadratics import solve_quadratic
from Dissociations_calculator_V1 import polyprotic_dissociations

class Titration_Input_Error(Exception):
    #Another custom input error class
    pass

def solve_for_M1(M1, V1, M2, V2): #A function to contain the algebra to solve for a variable, in this case M1, from M1V1=M2V2
    M1 = M2*V2/V1
    return f"The concentration of your acid is {M2}*{V2}/{V1} which equals {M1} M"
def solve_for_V1(M1, V1, M2, V2): #A function to contain the algebra to solve for a different variable from the M1V1=M2V2 equation
    V1 = M2*V2/M1
    return f"The volume of your acid is {M2}*{V2}/{M1} which equals {V1} L"
def solve_for_M2(M1, V1, M2, V2): #A fuction to contain the algebra to solve for M2 from M1V1=M2V2
    M2 = M1*V1/V2
    return f"The concentration of your base is {M1}*{V1}/{V2} which equals {M2} M"
def solve_for_V2(M1, V1, M2, V2): #A function to contain the algebra to solve for V2 from M1V1=M2V2
    V2 = M1*V1/M2
    return f"The volume of your base is {M1}*{V1}/{M2} which equals {V2} L"

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
    if M1 == None: print (solve_for_M1(M1, V1, M2, V2)) # and calls the appropriate function whilst passing it the variables. 
    if V1 == None: print(solve_for_V1(M1, V1, M2, V2))
    if M2 == None: print(solve_for_M2(M1, V1, M2, V2))
    if V2 == None: print(solve_for_V2(M1, V1, M2, V2))

#Below is a function to find the equivalence point in a monoprotic weak acid titration.
def get_weak_analyte_strong_titrant_equivalence_point():
        try:
            Ma=float(input("Enter the concentration of the weak analyte: ")) 
            Va=float(input("Enter the volume of the weak analyte: "))       
            Mb=float(input("Enter the concentration of the strong titrant: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for concentration and volume. ")
            return
        if Mb == 0:
            return print("ERROR: You cannot enter 0 as the titrant concentration. ")
        decimals =input("Enter the amount of decimal places you want the answer rounded to. Enter 'none' for the non-rounded answer: ")
        if decimals.lower() == "none":
            print(f"The equivalence point will be reached at {Ma*Va/Mb} L of titrant added. ")
            return
        else:
            try:
                decimals = int(float(decimals))
                print(f"The equivalence point will be reached at {Ma*Va/Mb:.{decimals}f} L of titrant added. ")
                return
            except ValueError:
                print("Invalid input. Please enter a number or 'none'. ")
                return

def calculate_initial_pH(analyte_concentration = None, analyte_Ka_value = None,): #A function to hold the math for calculating initial pH, and 
    if analyte_concentration==None:                                               #allowing it to be called for user inputs.
        analyte_concentration=float(input(f"Enter the concentration of your analyte: "))
    if analyte_Ka_value==None:
        analyte_Ka_value=float(input(f"Enter the Ka value for your anayte here: "))
    pH = -math.log10(math.sqrt(analyte_concentration*analyte_Ka_value))
    return f"The initial pH is {pH}. This is calculated by \
                 solving for x in Ka = x^2/({analyte_concentration}-x) \
                     where x is negligible. This can be rearranged\
        as x = sqrt({analyte_concentration}*{analyte_Ka_value}). Then pH is the -log(x), which in this case, \
            is {pH}. "
#Below is a function to calculate the equivalence point. Making it modular to allow it to be called elsewhere also. 
def calculate_equivalence_point(analyte_concentration = None, analyte_volume = None, analyte_Ka_value = None, titrant_concentration = None, titrant_volume = None,):
    if analyte_concentration==None:                                               
        analyte_concentration=float(input(f"Enter the concentration of your analyte in M: "))
    if analyte_volume==None:
        analyte_volume=float(input(f"Enter the volume of your analyte in L: "))
    if analyte_Ka_value==None:
        analyte_Ka_value=float(input(f"Enter the Ka value for your anayte here: "))
    if titrant_concentration==None:
        titrant_concentration=float(input(f"Enter the concentration of your titrant in M: "))
    if titrant_volume==None:
        titrant_volume=float(input(f"Enter the volume of your titrant in L: "))
    pH = 14-(-math.log10(math.sqrt((analyte_concentration*analyte_volume)/(analyte_volume+titrant_volume)*1e-14/analyte_Ka_value)))
    print(f"The pH is {pH}.")
    print(f"This is the equivalence point. At the equivalence point there is no weak analyte left, and no strong titrant left after the reaction completes.")
    print(f"This means the conjugate is all that is left. To get the pH then you must calculate the dissociation of the weak conjugate.") 
    print(f"Since the starting analyte was an acid, the conjugate is a weak base. To do this, you have to calculate the Kb of the conjugate using the equation...")
    print(f"Kb = 1e-14/Ka. The dissociation of a weak base gives a pOH result that must be converted to a pH by the equation 14-pOH = pH. ")
    return

def weak_acid_pH_calculator(analyte_volume = None, analyte_concentration = None, titrant_volume = None, titrant_concentration = None, pKa = None,): #This function should be able to handle doing titrations of a weak monoprotic acid (and potentially later on with a weak base also)
    try:
        if analyte_volume == None:
            analyte_volume = float(input("Enter the volume of the analyte in L: "))
        if analyte_concentration == None:
            analyte_concentration = float(input("Enter the concentration of the analyte in M: "))
        if titrant_volume == None:
            titrant_volume = float(input("Enter the volume of titrant being added in L"
                                    "If you want the initial dissociation, with no titrant added, enter '0': "))
        if titrant_concentration == None:
            titrant_concentration = float(input("Enter the concentration of titrant in M: "))
        if pKa == None:
            analyte_Ka_value = float(input("Enter the Ka for your analyte here. Scientific notation is acceptable in the format of X.Ye-x: "))
            pKa = -math.log10(analyte_Ka_value)
        if analyte_concentration <= 0 or titrant_concentration <= 0:
            return print("Input Error: Concentrations must be positive numbers.")
    except ValueError:
        print("Input Error: Please enter numerical values only. Check your units and make sure your input is in the correct units. ")
        return
    if titrant_volume == 0:
        print(calculate_initial_pH(analyte_concentration, analyte_Ka_value))
    if (analyte_concentration*analyte_volume) == (titrant_concentration*titrant_volume):
        print(calculate_equivalence_point(analyte_concentration, analyte_volume, analyte_Ka_value, titrant_concentration, titrant_volume,))
    if abs((titrant_concentration * titrant_volume) - 0.5 * (analyte_concentration * analyte_volume)) < 1e-6:
        print(f"The pH is {pKa}. This is the half equivalence point. The half equivalence point for this reaction is at {(1/2)*titrant_volume}.")
        print(f"At the half equivalence point pH is always equal to pKa.")
        return
    if (analyte_concentration*analyte_volume) < (titrant_concentration*titrant_volume):
        pH = 14-(-math.log10(((titrant_concentration*titrant_volume)-(analyte_concentration*analyte_volume))/(titrant_volume+analyte_volume)))
        print(f"The pH is {pH}.")
        print(f"This is after the equivalence point so the pH is mainly dictated by the concentration of the left-over strong titrant.")
        print(f"This can be calculated by determining the moles of titrant, subtracting the moles of analyte, and dividing the remaining moles of")
        print(f"titrant by the volume of the solution, which is the volume of analyte plus the volume of titrant. Then the -log of that concentration is pH")
        return
    if(analyte_concentration * analyte_volume) > (titrant_concentration * titrant_volume):
        pH = pKa + math.log10((titrant_concentration*titrant_volume)/((analyte_concentration*analyte_volume)-(titrant_volume*titrant_concentration)))
        print(f"The pH is {pH}.")
        print(f"This is calculated by determining the moles of acid present, {analyte_concentration} * {analyte_volume}, subtracting from that the moles of base added,")
        print(f"{titrant_concentration} * {titrant_volume}, which gives {(analyte_concentration*analyte_volume)-(titrant_volume*titrant_concentration)}.")
        print(f"Then the Henderson-Hasselbalch equation can be used where [A-] is the moles of base added and [HA] is the moles of acid left.")
        return

def polyprotic_titrations_calculator():
    pka_list = []
    try:
        weak_analyte_conc = float(input("Enter the concentration of the weak analyte, in M, here: "))
        if weak_analyte_conc == 0:
            raise Exception("ERROR: You cannot use 0 as the concentration of the weak analyte. ")
        weak_analyte_vol = float(input("Enter the volume of the weak analyte, in L, here: "))
        if weak_analyte_vol == 0:
            raise Exception("ERROR: You cannot use 0 as the volume of weak analyte. ")
        strong_titrant_conc = float(input("Enter the concentration of the strong titrant, in M, here: "))
        if strong_titrant_conc == 0:
            raise Exception("ERROR: You cannot use 0 as the concentration of strong titrant. ")
        strong_titrant_vol = float(input("Enter the volume of the strong titrant, in L, here: "))
        num_pkas = int(input("How many pKa values would you like to enter? If you would like to enter Ka values instead, enter '0' "))
        if num_pkas == 0:
            num_pkas = int(input("How many Ka values would you like to enter? "))
            if num_pkas == 0:
                raise Exception("You cannot enter 0 Ka values and 0 pKa values. Please enter an amount of pKa's or Ka's. ")
            for i in range(1, num_pkas+1):
                pka = -math.log10(float(input(f"Enter Ka{i}: ")))
                pka_list.append(pka)     
        else:
            for i in range(1, num_pkas+1):
                pka = float(input(f"Enter pKa{i}: "))
                pka_list.append(pka)
    except ValueError:
        return print("ERROR: Please enter a numerical value. Scientific notation is acceptable in the format of X.ye-x. ")
    moles_titrant = strong_titrant_conc*strong_titrant_vol
    moles_analyte = weak_analyte_conc*weak_analyte_vol
    if strong_titrant_vol == 0:
        print("\n --- No titrant added ---")
        print(polyprotic_dissociations(HXA_conc = weak_analyte_conc, pka_list = pka_list))
        return
    if moles_titrant < moles_analyte and moles_titrant > 0:
        print("\n --- Before first equivalence point --- ")
        print(weak_acid_pH_calculator(
            analyte_volume = weak_analyte_vol, 
            analyte_concentration = weak_analyte_conc, 
            titrant_volume = strong_titrant_vol, 
            titrant_concentration = strong_titrant_conc, 
            pKa = pka_list[0],
            ))
        return

        

def main():
   polyprotic_titrations_calculator()

if __name__ == "__main__":
    main()
