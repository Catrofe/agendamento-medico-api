from fastapi import APIRouter

from src.modules.schedule.models.models import (
    DayScheduleDoctor,
    RegisterSchedule,
    ScheduleModel,
)
from src.modules.schedule.service.service import ScheduleService

router = APIRouter()

service = ScheduleService()


@router.get("/schedule/doctor/{doctor_id}/avaliability")
async def get_schedule_by_doctor(
    doctor_id: int,
    days: int = 30,
) -> list[DayScheduleDoctor]:
    return await service.get_schedule_by_doctor(doctor_id, days)


@router.get("/schedule/doctor/{doctor_id}/")
async def get_schedule_reserved(
    doctor_id: int,
    days: int = 30,
    past_appointments: bool = False,
) -> list[ScheduleModel]:
    return await service.get_schedule_reserved(
        doctor_id,
        days,
        past_appointments=past_appointments,
    )


@router.post("/schedule")
async def create_schedule(schedule: RegisterSchedule) -> ScheduleModel:
    return await service.create_schedule(schedule)


@router.get("/schedule/patient/{patient_id}")
async def get_schedule_patient(
    patient_id: int,
    past_appointments: bool = False,
) -> list[ScheduleModel]:
    return await service.get_schedule_patient(
        patient_id,
        past_appointments=past_appointments,
    )
