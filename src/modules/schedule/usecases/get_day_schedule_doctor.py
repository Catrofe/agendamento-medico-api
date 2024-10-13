from collections.abc import Sequence
from datetime import datetime, time, timedelta

from src.modules.doctor.entity.doctor_schedule import DoctorSchedule
from src.modules.schedule.entity.schedule import Schedule
from src.modules.schedule.models.models import (
    WEEK_DAYS,
    DayScheduleDoctor,
    EnumStatusSchedule,
    Hours,
)


class GetDayScheduleDoctor:
    def __init__(
        self,
        days: int,
        future_schedules: Sequence[Schedule] | None = None,
    ) -> None:
        self.future_schedules = future_schedules
        self.current_time = datetime.now()
        self.limit_day = self.current_time + timedelta(days=days)

    async def generates_availability(
        self,
        default_schedule: Sequence[DoctorSchedule],
    ) -> list[DayScheduleDoctor]:
        schedules = await self.__generate_schedules(default_schedule)

        for schedule in schedules:
            await self.__generate_hours_schedule(schedule)

        return schedules

    def calculate_days_to_add(self, day_of_week: int) -> int:
        return (day_of_week - self.current_time.weekday()) % 7 or 7

    async def __generate_schedules(
        self,
        default_schedule: Sequence[DoctorSchedule],
    ) -> list[DayScheduleDoctor]:
        schedules = []
        for doctor_schedule in default_schedule:
            base_day = self.current_time + timedelta(
                days=self.calculate_days_to_add(doctor_schedule.day_of_week),
            )
            base_time = base_day.replace(
                hour=doctor_schedule.start_time.hour,
                minute=0,
                second=0,
                microsecond=0,
            )

            while base_time <= self.limit_day:
                schedules.append(
                    DayScheduleDoctor(
                        appointment=base_time,
                        **doctor_schedule.__dict__,
                        day_of_week_name=WEEK_DAYS[doctor_schedule.day_of_week],
                    ),
                )
                base_time += timedelta(days=7)

        return sorted(schedules, key=lambda x: x.appointment)

    async def __generate_hours_schedule(self, day_doctor: DayScheduleDoctor) -> None:
        day_doctor.hours = [
            Hours(
                start_time=time(hour=hour, minute=0, second=0),
                status=await self.__get_status_hour(hour, day_doctor.appointment),
            )
            for hour in range(day_doctor.start_time.hour, day_doctor.end_time.hour)
        ]

    async def __get_status_hour(
        self,
        hour: int,
        appointment: datetime,
    ) -> EnumStatusSchedule:
        return next(
            (
                EnumStatusSchedule.RESERVED
                for schedule in self.future_schedules
                if schedule.appointment == appointment.replace(hour=hour)
            ),
            EnumStatusSchedule.AVAILABLE,
        )
