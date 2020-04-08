def main():
    password_of_user = get_password()
    length_of_password = len(password_of_user)
    print("*"*length_of_password)


def get_password():
    password_of_user = (input("Enter your password:"))
    return password_of_user


main()