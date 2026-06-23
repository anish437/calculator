import streamlit as st
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
   st.write("Welcome to the calculator!")
   should_continue = True
   n1 = st.number_input("Enter the first number: ")
   while should_continue:
       for operator in operations:
          st.write(operator)
       operator = st.text_input("Enter an operator: ")
       n2 = st.number_input("Enter the next number: ")
       result = operations[operator](n1, n2)
       st.write(f"{n1} {operator} {n2} = {result}")

       choice= st.text_input("Type 'y' to continue calculating with the result, or type 'n' to exit: ")

       if choice == 'y':
         n1 = result
       else:
         should_continue = False
         st.write("\n" * 20)
calculator()

       
   