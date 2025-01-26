# Install pydantic[email] before
# pip install pydantic[email]  or on MAC - pip install pydantic\[email\]

from pydantic import BaseModel, ValidationError, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

try:
    user = User(id=123, name='John', email='invalid-email')
except ValidationError as error:
    print(error)
