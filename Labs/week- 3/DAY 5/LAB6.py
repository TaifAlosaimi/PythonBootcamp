scores = [45, 55, 65, 75, 85, 95]

passing_score = [
    "Pass" if score >= 60 else "Faild"
    for score in scores
]
print(passing_score)