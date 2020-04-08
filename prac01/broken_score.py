score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif 100 >= score >= 90:
    print("Excellent")
elif 90 > score >= 50:
    print("Passable")
else:
    print("Bad")