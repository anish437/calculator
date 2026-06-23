
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
   print("Welcome to the calculator!")
   should_continue = True
   n1 = float(input("Enter the first number: "))
   while should_continue:
       for operator in operations:
          print(operator)
       operator = input("Enter an operator: ")
       n2 = float(input("Enter the next number: "))
       result = operations[operator](n1, n2)
       print(f"{n1} {operator} {n2} = {result}")

       choice= input("Type 'y' to continue calculating with the result, or type 'n' to exit: ")

       if choice == 'y':
         n1 = result
       else:
         should_continue = False
         print("\n" * 20)
calculator()

       
   
