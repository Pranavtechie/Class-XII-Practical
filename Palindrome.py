"""
Practical No: 2
Program to check a given string in palindrome or not
"""

while True:

    user_input = input("Enter a string to check whether is a palindrome: ") # taking user input

    string = user_input
    reverse_string = user_input[::-1] # Reversing a string

    """
    You can also reverse a string using the reverse() method of string
    or you can also write a for loop to reverse a string
    """

    if string == reverse_string: 
        print(f"{string} is a Palindrome")

    else:
        print(f"{string} is not a Palindrome")

    confirm = input("Do you want to check again (Y/N): ")

    if confirm in ['y', 'Y']:
        continue

    else:
        print("You chose to quit the Program!")
        break
