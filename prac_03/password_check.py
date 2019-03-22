"""Dylan Valmadre"""


def main():
    min_length = 10
    valid_pw = False
    get_password(min_length, valid_pw)


def get_password(min_length, valid_pw):
    while not valid_pw:
        password = input(str("Enter password: "))
        if len(password) < min_length:
            valid_pw = False
            print("Password must contain at least 10 digits.")
        else:
            valid_pw = True
            display_asterisk(password)


def display_asterisk(string):
    for char in string:
        print("*", end=" ")


main()