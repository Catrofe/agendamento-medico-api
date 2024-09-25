from fastapi import FastAPI
import logging

def create_app() -> FastAPI:
    logging.info("Startup Application")
    return FastAPI(title="Medical Appointment", version="0.1.0", redoc_url=None)