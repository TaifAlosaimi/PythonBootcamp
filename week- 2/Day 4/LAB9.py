is_score_valid = False

score_text = input("Enter a number between 0 and 100: ")

if score_text.isdigit():
    score_x = int(score_text)

    if score_x >= 0 and score_x <= 100:
        print("Valid score")
        is_score_valid = True

    else:
        print("Score is invalid")

else:
    print("Please enter a number")