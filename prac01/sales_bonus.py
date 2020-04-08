sales = float(input("Enter sales: $ "))
while sales >= 0 :
    if 0 <= sales < 1000:
        bonus = sales * 0.10
        print("Your bonus is:" ,bonus)
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Your sales is :" ,bonus)
    else:
        print("You enter the wrong sales, Please enter again.")
    sales = float(input("Enter sales: $ "))