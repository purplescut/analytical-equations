import math

def solve_quadratic(a = None, b = None, c = None):
    quadratics_outcomes_list = []
    try:
        if a == None: 
            a = input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'a': ")
        if b == None:
            b = input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'b': ")
        if c == None:
            c = input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'c': ")
    except ValueError:
        print("ERROR: please enter a number, '0' is not a valid input. ")
    try:
        x1 = (-b + math.sqrt(b^2-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b^2-4*a*c))/(2*a)
    except ZeroDivisionError:
        print("ERROR: cannot divide by 0. Please enter non-zero values only.")
    except ValueError:
        print("ERROR: please enter a number, '0' is not a valid input. ")
    quadratics_outcomes_list = [x1, x2]
    return print(quadratics_outcomes_list)



def main():
    solve_quadratic(6, -17, 12)

if __name__ == "__main__":
    main()
