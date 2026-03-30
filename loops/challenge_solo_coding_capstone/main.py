# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item in inventory:
    current_stock = inventory[item][0]
    regular_price = inventory[item][1]
    discounted_price = inventory[item][2]
    print(f"{item}: Current stock is {current_stock} and price is {regular_price}")