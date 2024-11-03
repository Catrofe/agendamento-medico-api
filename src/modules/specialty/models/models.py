from pydantic import BaseModel, Field


class RegisterSpecialty(BaseModel):
    name: str = Field(max_length=155)
    description: str = Field(max_length=500)


class SpecialtyModel(BaseModel):
    id: int
    name: str
    description: str
    is_visible: bool
