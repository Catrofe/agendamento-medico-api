from pydantic import BaseModel, Field


class CreateDoctor(BaseModel):
    name: str = Field(max_length=155)
    crm: str = Field(max_length=10)
    email: str = Field(max_length=155)
    phone: str = Field(max_length=20)


class DoctorModel(CreateDoctor):
    id: int


class UpdateDoctor(BaseModel):
    id: int
    name: str | None = Field(max_length=155, default=None)
    crm: str | None = Field(max_length=10, default=None)
    email: str | None = Field(max_length=155, default=None)
    phone: str | None = Field(max_length=20, default=None)
