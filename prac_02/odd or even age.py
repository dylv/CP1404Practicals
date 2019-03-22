# Odd / Even

age = 0
valid_age = False
while not valid_age:
    try:
        age = int(input("Enter age: "))
        if age < 0:
            valid_age = False
            print("Nice try, but you can't be THAT young...")
        else:
            valid_age = True
    except ValueError:
        print("Invalid, try again.")

if age % 2 == 0:
    print("Your age ({}) is even!".format(age))
else:
    print("Your age ({}) is odd!".format(age))

