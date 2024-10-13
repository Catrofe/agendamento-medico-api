from collections.abc import Sequence
from datetime import datetime, time, timedelta

from src.main.settings import ZONE_INFO
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
        self.current_time = datetime.now(tz=ZONE_INFO)
        self.limit_day = self.current_time + timedelta(days=days)

    async def generates_availability(
        self,
        default_schedule: Sequence[DoctorSchedule],
    ) -> list[DayScheduleDoctor]:
        days_doctor_schedule: list[
            DayScheduleDoctor
        ] = await self.__generate_future_schedules(
            await self.__get_next_day_doctor_schedule(default_schedule),
        )

        for day_doctor in days_doctor_schedule:
            await self.__generate_hours_schedule(day_doctor)

        return days_doctor_schedule

    async def __generate_future_schedules(
        self,
        days_doctor_schedule: list[DayScheduleDoctor],
    ) -> list[DayScheduleDoctor]:
        news_days = []
        for day_doctor in days_doctor_schedule:
            for idx in range((self.limit_day - self.current_time).days):
                future_day = day_doctor.appointment + timedelta(days=idx * 7)
                if future_day > self.limit_day:
                    break
                schedule_future = DayScheduleDoctor(**day_doctor.model_dump())
                schedule_future.appointment = future_day
                news_days.append(schedule_future)
        return news_days

    async def __get_next_day_doctor_schedule(
        self,
        default_schedule: Sequence[DoctorSchedule],
    ) -> list[DayScheduleDoctor]:
        schedule_doctor = []
        for doctor_schedule in default_schedule:
            days_to_add = (
                doctor_schedule.day_of_week - self.current_time.weekday()
            ) % 7 or 7
            hour = self.current_time.replace(
                hour=doctor_schedule.start_time.hour,
                minute=0,
                second=0,
                microsecond=0,
            )

            schedule_doctor.append(
                DayScheduleDoctor(
                    appointment=hour + timedelta(days=days_to_add),
                    **doctor_schedule.__dict__,
                    day_of_week_name=WEEK_DAYS[doctor_schedule.day_of_week],
                ),
            )
        return schedule_doctor

    async def __generate_hours_schedule(self, day_doctor: DayScheduleDoctor) -> None:
        for hour in range(day_doctor.start_time.hour, day_doctor.end_time.hour):
            day_doctor.hours.append(
                Hours(
                    start_time=time(hour=hour, minute=0, second=0),
                    status=await self.__get_status_hour(hour, day_doctor.appointment),
                ),
            )

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
