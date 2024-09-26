from fastapi import APIRouter

from src.modules.doctor.models.models import CreateDoctor, DoctorModel
from src.modules.doctor.service.service import DoctorService

router = APIRouter()

service = DoctorService()


@router.post("/doctor", status_code=201)
async def create_doctor(doctor: CreateDoctor) -> DoctorModel:
    return await service.create_doctor(doctor)


@router.get("/doctor")
async def get_doctor() -> dict[str, str]:
    return {"message": "Doctor retrieved successfully."}


@router.put("/doctor")
async def update_doctor() -> dict[str, str]:
    return {"message": "Doctor updated successfully."}


@router.delete("/doctor")
async def delete_doctor() -> dict[str, str]:
    return {"message": "Doctor deleted successfully."}
