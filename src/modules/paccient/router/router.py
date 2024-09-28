from fastapi import APIRouter

from src.modules.paccient.service.service import PaccientService

router = APIRouter()

service = PaccientService()
