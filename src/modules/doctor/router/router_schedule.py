from fastapi import APIRouter

from src.modules.doctor.models.models_schedule import ScheduleCreate
from src.modules.doctor.service.service_schedule import DoctorScheduleService

router = APIRouter()

service = DoctorScheduleService()


@router.post("/schedule", status_code=201)
async def create_doctor(schedule: ScheduleCreate) -> ScheduleCreate:
    return await service.create_schedule(schedule)
