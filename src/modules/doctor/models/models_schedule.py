from pydantic import BaseModel, Field


class ScheduleCreate(BaseModel):
    doctor_id: int
    day_of_week: int
    start_time: int = Field(examples=["8"])
    end_time: int = Field(examples=["12"])
