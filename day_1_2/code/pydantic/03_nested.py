from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str
    age: int
    address: Address

user = User(name='Alice', age=30, address={'city': 'New York', 'state': 'NY'})
print(user.address.city)  # New York
