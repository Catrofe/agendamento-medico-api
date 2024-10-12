from enum import Enum
from typing import Optional, List

from pydantic import BaseModel
from datetime import time, datetime, date


class EnumStatusSchedule(Enum):
    RESERVED = "RESERVED"
    AVAILABLE = "AVAILABLE"


class EnumWeekDays(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


WEEK_DAYS = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}


class Hours(BaseModel):
    start_time: time
    status: EnumStatusSchedule = EnumStatusSchedule.AVAILABLE


class DayScheduleDoctor(BaseModel):
    doctor_id: int
    day_of_week: int
    day_of_week_name: str
    start_time: time
    end_time: time
    appointment: datetime
    hours: List[Hours] = []


class RegisterSchedule(BaseModel):
    doctor_id: int
    patient_id: int
    schedule_date: date
    start_time: int


class ScheduleModel(BaseModel):
    doctor_id: int
    patient_id: int
    appointment: datetime
    status: EnumStatusSchedule = EnumStatusSchedule.RESERVED