import math

def solve_quadratic(a = None, b = None, c = None):
    try:
        if a == None: 
            a = float(input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'a': "))
        if b == None:
            b = float(input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'b': "))
        if c == None:
            c = float(input("From the standard quadratic equation ax^2 +bx +c = 0, please enter the value of 'c': "))
        if a == 0:
            raise ZeroDivisionError("Coefficiant 'a' cannot be 0 for a quadratic equation. If there is no number before X^2 enter '1'. ")
    except ValueError:
        return print("ERROR: please enter a number, '0' is not a valid input. ")
    try:
        sqrt = b**2 - 4*a*c
        if sqrt < 0: 
            raise ValueError("The equation has no real roots. ")
        x1 = (-b + math.sqrt(sqrt)) / (2*a)
        x2 = (-b - math.sqrt(sqrt)) / (2*a)
        return [x1, x2]
    except ZeroDivisionError:
        return print("ERROR: cannot divide by 0. Please enter non-zero values only.")
    except ValueError:
        return print("ERROR: please enter a number, '0' is not a valid input. ")
    



def main():
    solve_quadratic(6, -17, 12)

if __name__ == "__main__":
    main()
