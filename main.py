def add(n1, n2):
  return n1 + n2

def substruct(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substruct,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = float(input("What is your first number?: "))
  for key in operations:
    print(key)
  
  should_continue = True
  while should_continue:
    
    operation_symbol = input("Pick an operator: ")
    num2 = float(input("What is your next number?: "))
    culculator_function = operations[operation_symbol]
    answer = culculator_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type Y to continue with culculating with {answer}, or N to exit: ") == "Y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()