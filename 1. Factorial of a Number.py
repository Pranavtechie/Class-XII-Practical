"""
Practical No: 1
Program to print a factorial of a number
"""

while True:

    user_input = input("Enter a number to get the factorial: ") # Getting user input (number)

    try:
        user_input = int(user_input) # Checking if the entered input in integer

        output = 0 # Initializing the output variable
        for i in range(1, user_input + 1):
            output *= i # Calculating the factorial using loop

        print(f"The Factorial of {user_input} is {output}") # Printing the output

        confirm = input("Do you want to calculate the factorial again (Y / N): ") # For running the code again

        if confirm == ['y','Y']: # Evaluating if True
            continue

        else: # Evaluating if False
            break

    except ValueError: # Handling exception if user enters and invalid value
        print("You have entered an invalid input.")
        continue
