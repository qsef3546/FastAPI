from pydantic import BaseModel
from sqlconnect import myuser
class patch_user(myuser):
    age: float