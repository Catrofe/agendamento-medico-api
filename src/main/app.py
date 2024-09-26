from fastapi import FastAPI
from src.main._lifespan import lifespan
import logging

def create_app() -> FastAPI:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:     %(message)s - DateTime: %(asctime)s",
    )
    return FastAPI(title="Medical Appointment", version="0.1.0", redoc_url=None, lifespan=lifespan)