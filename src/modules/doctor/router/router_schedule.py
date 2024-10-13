from fastapi import APIRouter

from src.modules.doctor.models.models_schedule import ScheduleCreate, ScheduleModel
from src.modules.doctor.service.service_schedule import DoctorScheduleService

router = APIRouter()

service = DoctorScheduleService()


@router.post("/doctor/schedule", status_code=201)
async def create_doctor(schedule: ScheduleCreate) -> ScheduleModel:
    return await service.create_schedule(schedule)


@router.get("/doctor/schedule/{schedule_id}", status_code=200)
async def get_schedule_by_id(schedule_id: int) -> ScheduleModel:
    return await service.get_schedule_by_id(schedule_id)


@router.get("/doctor/schedule/{doctor_id}", status_code=200)
async def get_schedule_by_doctor_id(doctor_id: int) -> list[ScheduleModel]:
    return await service.get_schedule_by_doctor_id(doctor_id)


@router.delete("/doctor/schedule/{schedule_id}", status_code=204)
async def delete_schedule_by_id(schedule_id: int) -> None:
    return await service.delete_schedule_by_id(schedule_id)
