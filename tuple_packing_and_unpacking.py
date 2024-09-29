
def display_format(customer_orders):
    for tuples in customer_orders:
        name, product, quantity = tuples
        formatted_order = f"Customer: {name} ordered a quantity of {quantity} {product}"
        print(formatted_order)

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]


display_format(orders)