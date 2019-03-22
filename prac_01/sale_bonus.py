user_sales = float(input("Enter sales: $"))
while user_sales > 0:
    if user_sales < 1000:
        user_sales = user_sales + (user_sales * 0.1)
        print("Your total salary + bonus: ${:.2f}".format(user_sales))
        user_sales = float(input("Enter sales: $"))
    elif user_sales >= 1000:
        user_sales = user_sales + (user_sales * 0.15)
        print("Your total salary + bonus: ${:.2f}".format(user_sales))
        user_sales = float(input("Enter sales: $"))
print("Thank you.")
