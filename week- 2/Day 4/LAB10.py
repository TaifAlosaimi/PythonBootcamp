membership = ["Admin", "Editor", "Viewer"]

current_membership = input("Enter your membership: ").strip().lower()

if current_membership.title() in membership:
    print("You are allowed to view the content")
    print(current_membership)

else:
    print("Please contact admin team")
    print(current_membership)