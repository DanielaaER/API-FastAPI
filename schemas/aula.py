
from pydantic import BaseModel, EmailStr
from typing import Optional


class Aula(BaseModel):
    id: Optional[int]
    nombre: str
    id_edificio: int
    password : Optional[str]
    id_aula : Optional[str]