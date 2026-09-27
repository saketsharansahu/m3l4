try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"num1 divided by num2 is {result}.")
except ZeroDivisionError:
    print("we cannot divide by zero because it is undefined.")
except ValueError :
    print("Invalid input. Please enter valid integers for both numbers.")
else:
    print("Division operation completed successfully.")
finally:
    print("i am finally block and i will always execute.")