from fastapi import APIRouter

from src.modules.doctor.models.models_schedule import ScheduleCreate
from src.modules.doctor.service.service_schedule import DoctorScheduleService

router = APIRouter()

service = DoctorScheduleService()


@router.post("/schedule", status_code=201)
async def create_doctor(schedule: ScheduleCreate) -> ScheduleCreate:
    return await service.create_schedule(schedule)


@router.get("/schedule/{schedule_id}", status_code=200)
async def get_schedule_by_id(schedule_id: int) -> ScheduleCreate:
    return await service.get_schedule_by_id(schedule_id)


@router.get("/schedule/{doctor_id", status_code=200)
async def get_schedule_by_doctor_id(doctor_id: int) -> list[ScheduleCreate]:
    return await service.get_schedule_by_doctor_id(doctor_id)


@router.delete("/schedule/{schedule_id}", status_code=204)
async def delete_schedule_by_id(schedule_id: int) -> None:
    return await service.delete_schedule_by_id(schedule_id)
