def main():
    numbers = []
    list_of_num = get_number(numbers)
    output_function(list_of_num)


def get_number(numbers):
    while len(numbers)<5:
        numbers_form_user = int(input("Number: "))
        numbers.append(numbers_form_user)
    return numbers


def output_function(list_of_num):
    print("The first number is {}" .format(list_of_num[0]))
    print("The last number is {} ".format(list_of_num[-1]))
    print("The samllest number is {} ".format(min(list_of_num)))
    print("The largest number is {} ".format(max(list_of_num)))
    print("The average of the numbers is {}".format(sum(list_of_num)/5))

main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name_ask = input("Enter your name")
if name_ask in usernames:
    print("Access granted")
else:
    print("Access denied")