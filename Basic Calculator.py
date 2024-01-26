def add():
  print("This function adds two inputs number together")
  a = float(input("Please enter a number: "))
  b = float(input(f"Please enter a second number to add to {a}: "))
  c = a + b
  print(f"{a} + {b} = {c}")

def subtract():
    print("This function subtracts the second input number from the first")
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be subtracted from {a} : "))
    c = a - b 
    print(f"{a} - {b} = {c}")

def multiply():
    print("This function multiplies two numbers")
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be multipled from {a} : "))
    c = a * b 
    print(f"{a} * {b} = {c}")

def divide():
    print("This function divides the second input number from the first")
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be divided from {a} : "))
    c = a / b 
    print(f"{a} / {b} = {c}")

