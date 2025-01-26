from dataclasses import dataclass, field

# Define the Product dataclass
@dataclass
class Product:
    name: str
    price: float

# Define the ShoppingCart dataclass
@dataclass
class ShoppingCart:
    items: list[Product] = field(default_factory=list)  # Initializes with an empty list of products
    total: float = 0.0

    # Method to add a product to the cart and update the total
    def add_product(self, product: Product):
        self.items.append(product)
        self.total += product.price

    # Method to remove a product from the cart and update the total
    def remove_product(self, product: Product):
        if product in self.items:
            self.items.remove(product)
            self.total -= product.price

    # Method to display the cart's contents
    def display_cart(self):
        for product in self.items:
            print(f"Product: {product.name}, Price: {product.price}")
        print(f"Total: {self.total}")

# Example usage
product1 = Product(name="Laptop", price=999.99)
product2 = Product(name="Smartphone", price=599.99)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.display_cart()
