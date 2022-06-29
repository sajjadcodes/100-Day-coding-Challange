 
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2

def multiple():
    return n1 * n2

def divide():
    return n1 / n2


operations  = {
     "+": add,
     "-": substract,
     "*": multiple,
     "/": divide,
    }


num1 = int(input("What's the first number?:"))
num2 = int(input("What is the second number"))

for operator in operations:
    print(operator)
operation_symbol = input("Pick an operation from the line above")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")