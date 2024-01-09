import re


def password_validator(func):
    def wrapper():
        while True:
            print(
                " The password must include: \n"
                " - at least 1 digit\n"
                " - 1 letter and 1 special character,\n"
                " - at least 8 characters in length, \n"
                " - no spaces allowed")

            password = func()
            if password is None:
                print("The password cannot contain space characters or tabs!")
                continue
            if len(password) >= 8 and re.search(r"\d", password) and re.search(r"[A-Za-z]", password) and re.search(
                    r"\W", password):
                print("Great, password is correct!")
                # print("Your password is:", password)
                return password
            else:
                print("The password does not match the requirements. Please try again.")

    return wrapper


@password_validator
def new_password():
    password = input("Please input your password: ")
    if " " in password or "\t" in password or password == "":
        return None
    else:
        return password


new_password()
