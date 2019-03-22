"""Dylan Valmadre"""

min_length = 10

valid_pw = False
while not valid_pw:
    password = input(str("Enter password: "))
    if len(password) < min_length:
        valid_pw = False
        print("Password must contain at least 10 digits.")
    else:
        valid_pw = True
        for char in password:
            print("*", end=" ")
