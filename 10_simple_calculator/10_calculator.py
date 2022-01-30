from calculator_logo import logo
#print(logo)

# calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    continue_operations = True
    abc = False

    while continue_operations:
        if abc is False:
            num1 = float(input("What's the first number?: "))
        else:
            num1 = answer
        print("Pick one of operations below.")
        for key in operations:
            print(key, end=" ")
        operation = input('\n')
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        abc = True
        print(f"{num1} {operation} {num2} = {answer}")
        new_var = input(f"Type 'y' to continue calculating with {answer} == 'y', or type 'n' to start new calculator. ")
        if new_var == 'y':
            continue_operations = True
        elif new_var == 'n':
            abc = False
            calculator()
        else:
            continue_operations = False

calculator()