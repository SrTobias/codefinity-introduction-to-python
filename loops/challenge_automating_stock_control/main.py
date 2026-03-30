# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

#1 
for item in inventory:
    current_stock = inventory[item][0]
    min_stock = inventory[item][1]
    restock_stock = inventory[item][2]
    sale_status = inventory[item][3]
    