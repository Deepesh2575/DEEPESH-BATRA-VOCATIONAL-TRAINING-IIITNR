# Create a tuple containing five product names
products = ("Laptop", "Mouse", "Keyboard", "Monitor", "Headphones")

# Display all products
print("Original Tuple:")
print(products)

# Convert the tuple into a list
products_list = list(products)

# Add a new product
products_list.append("Webcam")

# Convert it back into a tuple
products = tuple(products_list)

# Display the updated tuple
print("\nUpdated Tuple:")
print(products)
