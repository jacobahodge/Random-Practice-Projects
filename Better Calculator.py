num1 = float(input("Please enter a number: "))
op = input("Please enter an operator for this math equation: ")
num2 = float(input("Please enter a second number for the equasion: "))

def calculator():
  if op == '+':
    print(num1 + num2)
  elif op =='-':
    print(num1 - num2)
  elif op == '*':
    print(num1 * num2)
  elif op == '/':
    print(num1 / num2)
  else:
      print("This calculator only supports addition, subtraction, multiplication and division of two numbers")
