import math

stored_Ka_values_dictionary = {} # a dictionary to potentially add and store Ka values in to provice 
                                 # to the user for the purpose of building them a custom database of sorts for common
                                 # values they will need to use and/or access repeatedly


class Dissociations_Input_Error(Exception):
    #A custom error for incorrect user inputs
    pass

def calculate_A(H, HA, Ka):
    return HA*Ka/H # a function to perform simple algebra for repeated use

def calculate_H(A, HA, Ka):
    return HA*Ka/A # a function to perform simple algebra for repeated use

def calculate_HA(A, H, Ka):
    return H*A/Ka # a function to perform simple algebra for repeated use

def calculate_Ka(A, H, HA):
    return H*A/HA # a function to perform simple algebra for repeated use

def determine_monoprotic_acid_dissociation_equation(H, HA, A, Ka): # a function for deciding which algebra function to use for monoprotic dissociations
    if H == None:
        return calculate_H(A, HA, Ka)
    if A == None:
        return calculate_A(H, HA, Ka)
    if HA == None:
        return calculate_HA(A, H, Ka)
    if Ka == None:
        return calculate_Ka(A, H, HA)
    
def is_unknown(variable): # a function to use for detemermining which variable is the unknown and converting the user inputted string into a None type python value
    return None if variable.strip().lower() == "none" else float(variable)

def monoprotic_acid_calculator(): # the meat of the calculator for a monoprotic acid dissociation equation. 
    unknown = "If this is your unknown enter 'None'."      # This will take the user inputs and push them to the appropriate functions as needed
    dissociated = "Enter the concentration of the dissociated "
    print("For your unknown, or the variable you wish to calculate, enter 'None' when asked to enter its value")
    H = input(f"{dissociated}H, or, '[H+]' here. {unknown}")
    A = input(f"{dissociated}conjugate acid, or, '[A-]' here. {unknown}")
    HA = input(f"Enter the concentration of the acid you are beginning with before the dissociated, or, '[HA]' here. {unknown}")
    Ka = input(f"Enter the value for the dissociation constant, or, Ka, for the weak acid here. {unknown}")
    try:
        print(determine_monoprotic_acid_dissociation_equation(*list(map(is_unknown, [H, A, HA, Ka]))))
    except ValueError:
        raise Dissociations_Input_Error(
            "ERROR: Invalid input! Please only enter numeric values for any known values. Enter 'None' for any values that are unknown. " 
            "Scientific notation can be used in the format of X.Ye-x"
        )



def main():
    monoprotic_acid_calculator()




if __name__ == "__main__":
    main()
