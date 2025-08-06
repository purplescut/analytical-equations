import math
from quadratics import solve_quadratic

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

def polyprotic_dissociations(HXA_conc = None, pka_list = None,):
    if pka_list == None:
        pka_list = []
        try:
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
    if HXA_conc == None:
        try:
            HXA_conc = float(input("Enter the concentration of the weak analyte in M. Only include the numerical value.: "))
            if HXA_conc == 0:
                raise Exception("ERROR: 0 is not a valid concentration. ")
        except ValueError:
            return print("ERROR: Please enter a numerical value only. 0 is not a valid concentration. ")
    try:
        roots = solve_quadratic(1, convert_pKa_to_Ka(pka_list[0]), -convert_pKa_to_Ka(pka_list[0])*HXA_conc)
        if not roots:
            return print("ERROR: No roots returned from solver.")
        positive_roots = max(r for r in roots if r>0)
        if not positive_roots:
            return print("ERROR: No positive roots found.")
        x = max(positive_roots)
        pH = -math.log10(x)
        print(f"pH = {pH:.2f}")
        return x, pH
    except Exception as e:
        return print(f"ERROR during quadratic solving: {e}")
    
def convert_pKa_to_Ka(pKa):
    return 10**-pKa


def main():
    polyprotic_dissociations()




if __name__ == "__main__":
    main()
