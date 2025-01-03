import logging

from fastapi import FastAPI

from src.exceptions.BaseException import BaseExceptionAppointment
from src.main._lifespan import lifespan
from src.modules.doctor.router.router import router as doctor_router
from src.modules.doctor.router.router_schedule import router as doctor_schedule_router
from src.modules.patient.router.router import router as patient_router
from src.modules.schedule.router.router import router as schedule_router
from src.modules.specialty.router.specialty_router import router as specialty_router


def create_app() -> FastAPI:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:     %(message)s - DateTime: %(asctime)s",
    )
    app = FastAPI(
        title="Medical Appointment",
        version="0.1.0",
        redoc_url=None,
        lifespan=lifespan,
        exception_handlers={BaseExceptionAppointment: BaseExceptionAppointment.handler},
        swagger_ui_parameters={"displayRequestDuration": True},
    )

    logging.info("Creating routes...")
    create_routers(app)
    return app


def create_routers(app: FastAPI) -> None:
    app.include_router(doctor_router, tags=["Doctor"])
    app.include_router(doctor_schedule_router, tags=["Doctor Schedule"])
    app.include_router(patient_router, tags=["Patient"])
    app.include_router(schedule_router, tags=["Schedule"])
    app.include_router(specialty_router, tags=["Specialty"])
