from pydantic import BaseModel, Field


class CreateDoctor(BaseModel):
    name: str = Field(max_length=155)
    crm: str = Field(max_length=10)
    email: str = Field(max_length=155)
    phone: str = Field(max_length=20)


class DoctorModel(CreateDoctor):
    id: int
