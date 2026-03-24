# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# count
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

# find
banana_index = shelf.index("bananas")
print("First Banana index:", banana_index)

# check
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Count
