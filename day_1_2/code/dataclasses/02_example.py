# No need to manually write __init__
# Auto-generates a user-friendly __repr__

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int

product = Product(name="Laptop", price=999.99, stock=20)
print(product)

##########################################################
# Adding Default Values to Fields

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int = 0  # default value for stock

product = Product(name="Smartphone", price=499.99)
print(product)

##########################################################
# Object comparison
# The __eq__ method is automatically generated, allowing for easy comparison.

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

product1 = Product(name="Laptop", price=999.99)
product2 = Product(name="Laptop", price=999.99)

print(product1 == product2)  # True

##########################################################

# Making Objects Immutable
# Frozen dataclasses cannot be modified after creation.
# Useful for creating hashable and immutable objects

from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    name: str
    price: float

product = Product(name="Laptop", price=999.99)
try:
    product.price= 10.00
except Exception as error:
    print(error)

##########################################################

# Post-init Processing
# __post_init__ runs after the __init__ method.
# Useful for validation or additional setup.

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price == 1000:
            raise ValueError("Price cannot be 1000")
try:
    product = Product(name="Laptop", price=1000)
except Exception as error:
    print(error)



