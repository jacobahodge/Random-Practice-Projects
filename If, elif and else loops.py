def age_group():

    age = float(input("Please enter your age in years: "))

    if age >= 18: 
        print("You are an adult")
    elif age < 18 and age > 4:
        print("You are a child")
    else:
        print("You are a baby")

def longest_name(name1, name2, name3):
    print("name1 = " + name1)
    print("name2 = " + name2)
    print("name3 = " + name3)
    if len(name1) > len(name2) and len(name1) > len(name3):
        return name1
    elif len(name2) > len(name1) and len(name2) > len(name3):
        return name2
    elif len(name3) > len(name1) and len(name3) > len(name2):
        return name3
    elif len(name1) == len(name2):
        print(name1 + " is the same length as " + name2)
    elif len(name2) == len(name3):
        print(name2 + " is the same length as " + name3)
    elif len(name1) == len(name3):
        print(name1 + " is the same length as " + name3)
    else:
        print("error")

