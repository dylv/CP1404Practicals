cost = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    cost += price
if cost > 100:
    cost *= 0.9
print("Total price for {} items is ${:.2f}".format(number, cost))
