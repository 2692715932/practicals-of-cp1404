"""
CP1404/CP5632 Practical - Suggested Solution
stores users' emails (unique keys) and names (values) in a dictionary.
"""

EMAILS = {}


def main():
    email = str(input("Email: "))
    while email != "":
        name_of_user = email.split('@')[0]
        name_of_user = name_of_user.title()
        name_of_user.join(name_of_user)
        name_of_user = name_of_user.replace('.', ' ')
        print("Is your name {}?".format(name_of_user))
        answer = input("Y/n").upper()
        if answer == "Y":
            EMAILS[name_of_user] = email
            email = str(input("Email: "))
        elif answer == "NO":
            name_of_user = str(input("Name: "))
            EMAILS[name_of_user] = email
    if email == '':
        print(EMAILS.items())


if __name__ == '__main__':
    main()