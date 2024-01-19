def namefunc():
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
