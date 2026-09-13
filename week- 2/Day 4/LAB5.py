account_active = True
has_permission = False

if account_active:                             #nested if: if statment inside another if statment
    if has_permission:
        print("Access Granted")
    else:
        print("Access denied")

else:
    print("account is not active")