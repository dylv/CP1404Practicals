age = 0
valid_age = False
while not valid_age:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Impossible! Try again...")
        else:
            valid_age = True
    except ValueError:
        print("Error... try again.")

print("You are {} years old.".format(age))







