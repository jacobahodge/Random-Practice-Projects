# 1.) Name Function with name as function variable. 
def namefunc1(name):
    print("Hello, " + name + "!")

namefunc1("Bob") #Returns: Hello, Bob!

# 2.) Name function that assigns the user's input as a local variable to generate the name. Then uses a concatenation print statement. 
def namefunc2():
    name = input("Please enter your first name: ")
    result = ("Hello, " +  name + "!")
    return print(result)

namefunc2() # First will ask the user to enter their first name and then will say: Hello, <user_entered_name>.

# 3.) Similar to number 2 but prints the user's name by calling the user's input value with an "f: string instead of concatenation. 

def namefunc3():
    fname = input("Please enter your first name: ")
    print(f"Hello, {fname}!") # NOTE - you need an "f" string to be able to pull in values to a print statement. 

namefunc3() # First will ask the user to enter their first name and then will say: Hello, <user_entered_name>.

# 4.) Advanced Name function. Splits a first and second name from a string into separate values. Also has some checks in place. 
def namefunc3():
    full_name = input("Enter your full name: ")
    full_name_dict = full_name.split(' ')
    
    if full_name == '':
        print("Please enter your full name")
    elif len(full_name_dict) < 2:
        print("Please enter your full name with a space inbetween your first and last name")
    else:
        fname = full_name_dict[0]
        lname = full_name_dict[1]
        print(f"Hello, {fname} {lname}!")

namefunc()
