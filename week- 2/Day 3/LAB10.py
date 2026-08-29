csv_text = "apple,orange,banana,cherry,dates"

splitted_text = csv_text.split(",")
print(splitted_text)

joined_text = "-".join(splitted_text)

print(f"""Your list is {csv_text}
Splitted like this {splitted_text}
rejoined like this {joined_text}""")