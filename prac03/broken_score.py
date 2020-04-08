def main():
        score = float(input("Enter score: "))
        result = output_result(score)
        score = random_score(score)
        result = output_result(score)

def output_result(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    else:
        if 100 > score >= 90:
            output = print("Excellent")
        elif 90 > score >= 50:
            output = print("Passable")
        elif score < 50:
            output = print("Bad")
        return output

def random_score(score):
    import random
    score = random.randint(0,100)
    print(score)
    return score

main()

