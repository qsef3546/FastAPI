from pydantic import BaseModel

class insert_user(BaseModel):
    name: str
    age: float