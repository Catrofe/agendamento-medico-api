from fastapi import APIRouter

from src.modules.patient.models.models import PatientCreate, PatientModel, PatientUpdate
from src.modules.patient.service.service import PatientService

router = APIRouter()

service = PatientService()


@router.post("/patient")
async def registry_paccient(patient: PatientCreate) -> PatientModel:
    return await service.create_patient(patient)


@router.get("/patient/{patient_id}")
async def get_patient_by_id(patient_id: int) -> PatientModel:
    return await service.get_patient_by_id(patient_id)


@router.put("/patient/{patient_id}")
async def update_patient(patient_id: int, patient: PatientUpdate) -> PatientModel:
    return await service.update_patient(patient_id, patient)


@router.delete("/patient/{patient_id}")
async def delete_patient(patient_id: int) -> None:
    await service.delete_patient(patient_id)
