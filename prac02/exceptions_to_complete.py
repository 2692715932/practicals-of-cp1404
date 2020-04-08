"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        integer_from_user = int(input("Enter an integer:"))
        type_of_input = type(integer_from_user)
        if type_of_input == int:
            finished = True
            result = integer_from_user
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)