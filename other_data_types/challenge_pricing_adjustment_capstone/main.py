#1 Dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}

#2 Check and Update Price
eggs_details = grocery_inventory.get("Eggs")
eggs_price = eggs_details[1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", 4.50, 30)})
else:
    print("The price of Eggs is reasonable.")

#3 Add new
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(grocery_inventory)

#4 Manage Stock
milk_stock = grocery_inventory.get("Milk")
milk_stock_num = milk_stock[2]
if milk_stock_num < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": ("Dairy", 3.50, 28)})
else:
    print("Milk has sufficient stock")

#5 Remove Item Based on Price
apples_details = grocery_inventory.get("Apples")
apples_price = apples_details[1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

#6 Final print
print(grocery_inventory)