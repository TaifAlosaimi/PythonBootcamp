import grades



def main():
    scores = [95, 85, 75, 65, 50]

    for score in scores:
        grade = grades.calculate_grade(score)
        print(f"Score: {score} → Grade: {grade}")


if __name__ == "__main__":
    main()
