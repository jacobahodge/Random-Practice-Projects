def age_group():

    age = float(input("Please enter your age in years: "))

    if age >= 18: 
        print("You are an adult")
    elif age < 18 and age > 4:
        print("You are a child")
    else:
        print("You are a baby")

age_group()
