is_active = True
is_verified = True
role = "editor"
is_blocked = False

if is_active and is_verified:
    print("Account is ready")

if role == "admin" or role == "editor":
    print("User can edit")

if not is_blocked:
    print("User is not blocked")

else:
    print("User is blocked")