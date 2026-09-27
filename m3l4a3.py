valid = False
while not valid:
    try:
        age = int(input("enter your age: "))
        print(f"you are {age} years old.")
        valid = True
    except ValueError:
        print("invalid input. please enter a valid integer for age.")