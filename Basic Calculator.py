def add():
  a = float(input("Please enter a number: "))
  b = float(input(f"Please enter a second number to add to {a}: "))
  c = a + b
  print(f"{a} + {b} = {c}")

def subtract():
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be subtracted from {a} : "))
    c = a - b 
    print(f"{a} - {b} = {c}")

def multiply():
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be multipled from {a} : "))
    c = a * b 
    print(f"{a} * {b} = {c}")

def divide():
    a = float(input("Please enter a number: "))
    b = float(input(f"Please enter a number to be divided from {a} : "))
    c = a / b 
    print(f"{a} / {b} = {c}")
