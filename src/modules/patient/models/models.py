from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    name: str = Field(max_length=155)
    cpf: str = Field(max_length=11)
    email: str = Field(max_length=155)
    phone: str = Field(max_length=15)


class PatientModel(PatientCreate):
    id: int


class PatientUpdate(BaseModel):
    id: int
    name: str | None = Field(max_length=155)
    cpf: str | None = Field(max_length=11)
    email: str | None = Field(max_length=155)
    phone: str | None = Field(max_length=15)
