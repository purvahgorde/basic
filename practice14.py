correct_password = "secret123"
attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    if password == correct_password:
        print("You have successfully logged in.")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")
else:
    print("You have been use 3 access.")