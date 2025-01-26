from pydantic import BaseModel, field_validator

class User(BaseModel):
    id: int
    name: str

    @field_validator('name')
    def name_must_be_longer(cls, v):
        if len(v) < 3:
            raise ValueError('name must be longer than 2 characters')
        return v

try:
    user = User(id=1, name='To')
except ValueError as error:
    print(error)
