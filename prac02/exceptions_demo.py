"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the content of the input is not a valid number, such as input "number" or";'."
Nor can other similar special digital PI.
2. When will a ZeroDivisionError occur?
When denominator == 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))  #Perform error checking where the denominator cannot be zero
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#  The error message here is no longer necessary
print("Finished.")