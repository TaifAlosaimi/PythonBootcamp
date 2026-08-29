memberships = ["Admin", "Editor", "Viewer"]
current_membership = ["Editor"]

if current_membership[0] in memberships:
    print("Welcome")
else:
    print("Go Home")