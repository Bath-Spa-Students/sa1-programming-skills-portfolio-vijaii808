correct_password = "12345"
while True:
    user_input = input("Please enter the password: ")

    if (user_input) == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password, please try again.")
