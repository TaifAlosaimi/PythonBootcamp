user_age = 25
has_permission = True

is_eligible = (user_age >= 18 and has_permission)

print(f"Eligibility status: {is_eligible}")