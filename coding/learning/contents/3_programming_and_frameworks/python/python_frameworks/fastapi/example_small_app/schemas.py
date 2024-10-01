from pydantic import BaseModel


class ItemBase(BaseModel): # have common attributes while creating or reading data
    title: str
    description: str | None = None


class ItemCreate(ItemBase): # plus any additional data (attributes) needed for creation.
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True # read the data with data is not only a dict, it can be an atribute of the class


class UserBase(BaseModel): # have common attributes while creating or reading data
    email: str


class UserCreate(UserBase): # plus any additional data (attributes) needed for creation.
    password: str # the user will also have a password when creating it
    # But for security, the password won't be in other Pydantic models


class User(UserBase): # will be used when reading a user (returning it from the API) doesn't include the password.
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True # read the data even if it is not a dict
