username = "lolo"
password = "epic"

login = False

while (not login):
    input_user = input("user")
    input_pass = input("pass")

    if (input_user == username and input_pass == password):
        login = True
    else:
        print("Username or password is incorrect.")


print("Logged in!")