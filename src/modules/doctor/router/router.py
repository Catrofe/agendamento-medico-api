from fastapi import APIRouter

from src.modules.doctor.models.models import CreateDoctor, DoctorModel, UpdateDoctor
from src.modules.doctor.service.service import DoctorService

router = APIRouter()

service = DoctorService()


@router.post("/doctor", status_code=201)
async def create_doctor(doctor: CreateDoctor) -> DoctorModel:
    return await service.create_doctor(doctor)


@router.get("/doctor/{doctor_id}", status_code=200)
async def get_doctor(doctor_id: int) -> DoctorModel:
    return await service.get_doctor_model(doctor_id)


@router.put("/doctor", status_code=200)
async def update_doctor(doctor: UpdateDoctor) -> DoctorModel:
    return await service.update_doctor(doctor)


@router.delete("/doctor/{doctor_id}", status_code=204)
async def delete_doctor(doctor_id: int) -> None:
    await service.delete_doctor(doctor_id)
