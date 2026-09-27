try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError as ex:
    print(f"Invalid input: {ex}. Please enter a valid integer for age.")
    