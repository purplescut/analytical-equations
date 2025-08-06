import math
from quaqdratics import solve_quadratic

stored_Ka_values_dictionary = {} #A dictionary to potentially add and store Ka values in to provice 
                                 #to the user for the purpose of building them a custom database of sorts for common
                                 #values they will need to use and/or access repeatedly


class Dissociations_Input_Error(Exception):
    #A custom error for incorrect user inputs
    pass

def calculate_A(H, HA, Ka):
    A = HA*Ka/H #A function to perform simple algebra for repeated use
    return f"The concentration of [A-], is {A}. Which is calculated by [A-] = {HA}*{Ka}/{H}. "
def calculate_H(A, HA, Ka):
    H =HA*Ka/A #A function to perform simple algebra for repeated use
    return f"The concentration of [H+] is {H}. Which is calculated by [H+] = {HA}*{Ka}/{A}. "
def calculate_HA(A, H, Ka):
    HA = H*A/Ka #A function to perform simple algebra for repeated use
    return f"The concentration of the weak acid being dissociated is {HA}. Which is calculated by [HA] = {H}*{A}/{Ka}. "
def calculate_Ka(A, H, HA):
    Ka = H*A/HA #A function to perform simple algebra for repeated use
    return f"The value of Ka for this dissociation is {Ka}. Which is calculated by Ka = {H}*{A}/{HA}"

def determine_monoprotic_acid_dissociation_equation(H, HA, A, Ka): # a function for deciding which algebra function to use for monoprotic dissociations
    if [H, HA, A, Ka].count(None) != 1:
        raise Dissociations_Input_Error("ERROR: Please enter 'None' for exactly one variable.")
    if H == None: return calculate_H(A, HA, Ka)
    if A == None:return calculate_A(H, HA, Ka)
    if HA == None:return calculate_HA(A, H, Ka)
    if Ka == None:return calculate_Ka(A, H, HA)
    
def is_unknown(variable): #A function to use for detemermining which variable is the unknown and converting the user inputted string into a None type python value
    return None if variable.strip().lower() == "none" else float(variable)

def monoprotic_acid_dissociation_calculator(): #The meat of the calculator for a monoprotic acid dissociation equation. 
    unknown = "If this is your unknown enter 'None'.: "      #This will take the user inputs and push them to the appropriate functions as needed
    dissociated = "Enter the concentration of the dissociated "
    print("For your unknown, or the variable you wish to calculate, enter 'None' when asked to enter its value")
    H = input(f"{dissociated}H, or, '[H+]' here. {unknown}")
    A = input(f"{dissociated}conjugate acid, or, '[A-]' here. {unknown}")
    HA = input(f"Enter the initial concentration of the undissociated acid (HA): {unknown}")
    Ka = input(f"Enter the value for the dissociation constant, or, Ka, for the weak acid here. {unknown}")
    try:
        print(determine_monoprotic_acid_dissociation_equation(*list(map(is_unknown, [H, A, HA, Ka]))))
    except ValueError:
        raise Dissociations_Input_Error(
            "ERROR: Invalid input! Please only enter numeric values for any known values. Enter 'None' for any values that are unknown. " 
            "Scientific notation can be used in the format of X.Ye-x"
        )

def polyprotic_dissociations():
    ka1 = input("Enter the ka1 of your analyte here. If provided pka1 instead, enter 'pka1' then type the value of the given pka. " \
    "The calculator will compute your ka1 and give it to you.: ")
    ka2 = input("Enter the ka2 of your analyte here. If provided pka2 instead, enter 'pka2' then type the value of the given pka. " \
    "The calculator will compute your ka2 and give it to you.: ")
    H2A = input("Enter the concentration of the diprotic acid in M. Only include the numerical value.: ")
    try:
        if ka1.lower() == "pka1":
            ka1 = float(input("Enter the given pka1: "))
            ka1 = 10**(-ka1)
            print(ka1)
        else:
            ka1 = float(ka1)
        if ka2.lower() == "pka2":
            ka2 = float(input("Enter the given pka2: "))
            ka2 = 10**(-ka2)
            print(ka2)
        else:
            ka2 = float(ka2)
        H2A = float(H2A)
        if ka1 <= 0 or ka2 <= 0 or H2A <= 0:
            return print("ERROR: Ka values and concentration must be greater than 0. ")
    except ValueError:
        return print("ERROR: Invalid input. Please enter a numerical value for Ka, pKa, and concentration of H2A. ")
    try:
        roots = solve_quadratic(1, ka1, -ka1*H2A)
        x = max(r for r in roots if r>0)
        pH = -math.log10(x)
        print(f"pH = {pH: .2f}")
        return x, pH
    except Exception as e:
        print(f"ERROR during quadratic solving: {e}")
    



def main():
    polyprotic_dissociations()




if __name__ == "__main__":
    main()
