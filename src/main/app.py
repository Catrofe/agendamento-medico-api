import logging

from fastapi import FastAPI

from src.exceptions.BaseException import BaseExceptionAppointment
from src.main._lifespan import lifespan


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
    )

    logging.info("Creating routes...")
    create_routers(app)
    return app


def create_routers(app: FastAPI) -> None:
    from src.modules.doctor.router.router import router as doctor_router

    app.include_router(doctor_router)
