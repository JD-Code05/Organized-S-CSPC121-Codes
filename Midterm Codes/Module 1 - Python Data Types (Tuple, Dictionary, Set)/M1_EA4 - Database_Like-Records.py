#Simulating Database-Like Records
#BCS13 - Ubungen
products = {
    1: ("Laptop", 999.99, 5),
    2: ("Smartphone", 499.50, 10),
    3: ("Headphones", 79.99, 25)
}
for product_name, products in products.items():
    print(f"Product {product_name}: {products[0]}, Price: ${products[1]}, Stock: {products[2]}")