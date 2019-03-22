MENU = """Y - Yes
N - No"""
print("Welcome to The Shop, would you like to make a purchase?")
print(MENU)
choice = input(">>> ").upper()
while choice != "N":
    user_item = float(input("Please enter the price: $"))
    if user_item > 100:
        price = int(user_item + (user_item * 0.1))
        print("Another purchase?")
        print(MENU)
        choice = input(">>> ").upper()
    elif user_item <= 0:
        print("Invalid pricing.")
    else:
        price = (int(user_item))
        print("Another purchase?")
        print(MENU)
        choice = input(">>> ").upper()
# NOTE: Order is crucial when using logical expressions!
        for i in range(price):
            total = int(price)
            print("Price of item: ${:.2f}".format(total))
