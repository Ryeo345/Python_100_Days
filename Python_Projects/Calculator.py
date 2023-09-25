import sys

sys.path.append("../Python_modules")
from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# interesting that you can put functions as values in a dictionary
def calculator():
    print(logo) # we add the logo inside the
    num1 = float(input("What is the first number?\n"))
    # num2 = int(input("What is the second number?\n"))

    # for operator in operations:
    #     print(operator)

    # operation_symbol = input("Pick a symbol from the line above: ")

    # calculation_function = operations[operation_symbol]
    #
    # answer = calculation_function(num1, num2)
    #
    # print(f"{num1} {operation_symbol} {num2} is {answer}")
    #
    # continue_calculation = input(f"Type 'y' to continue with {answer} or 'n' to exit.\n")

    # while continue_calculation == 'y':
    #     operation_symbol = input("Pick a symbol from the line above: ")
    #     calculation_function = operations[operation_symbol]
    #     next_num = int(input("What is the next number?\n"))
    #     new_answer = calculation_function(answer,next_num)
    #     print(f"{answer} {operation_symbol} {next_num} is {new_answer}")
    #     continue_calculation = input(f"Type 'y' to continue with {new_answer} or 'n' to exit.")

    should_continue = True # flag to check off

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]
        next_num = float(input("What is the next number?\n"))
        answer = calculation_function(num1, next_num)
        print(f"{num1} {operation_symbol} {next_num} is {answer}")
        if input(f"Type 'y' to continue with {answer} or 'n' to exit.\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
            # recursion the function calls itself so the calculate can keep running and refreshing the program after the calculation is done
            # to prevent the infinite loop there should be a condition to be meet for this recursion

calculator()
