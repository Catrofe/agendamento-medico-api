from typing import List

from fastapi import APIRouter

from src.modules.schedule.models.models import DayScheduleDoctor, RegisterSchedule, ScheduleModel
from src.modules.schedule.service.service import ScheduleService

router = APIRouter()

service = ScheduleService()


@router.get("/schedule/doctor/{doctor_id}")
async def get_schedule_by_doctor(doctor_id: int) -> List[DayScheduleDoctor]:
    return await service.get_schedule_by_doctor(doctor_id)

@router.get("/schedule/doctor/{doctor_id}/days/{days}")
async def get_schedule_by_doctor(doctor_id: int, days: int) -> List[DayScheduleDoctor]:
    return await service.get_schedule_by_doctor(doctor_id, days)

@router.post("/schedule")
async def create_schedule(schedule: RegisterSchedule) -> ScheduleModel:
    return await service.create_schedule(schedule)