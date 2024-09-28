from src.exceptions.BadRequestException import BadRequestException
from src.modules.patient.entity.patient import Patient
from src.modules.patient.models.models import PatientCreate, PatientModel, PatientUpdate
from src.modules.patient.repository.repository import PatientRepository


class PatientService:
    def __init__(self) -> None:
        self.__repository = PatientRepository()

    async def create_patient(self, new_patient: PatientCreate) -> PatientModel:
        if self.__repository.patient_exists(new_patient):
            raise BadRequestException("Pattient already exists")
        patient = Patient(**new_patient.model_dump())
        patient = await self.__repository.save_patient(patient)
        return PatientModel(**patient.__dict__)

    async def get_patient_by_id(self, patient_id: int) -> PatientModel:
        patient = await self.__repository.get_patient_by_id(patient_id)
        if not patient:
            raise BadRequestException("Patient not found")

        return PatientModel(**patient.__dict__)

    async def update_patient(
        self,
        patient_id: int,
        patient_model: PatientUpdate,
    ) -> PatientModel:
        patient: Patient = await self.__repository.get_patient_by_id(patient_id)
        if not patient:
            raise BadRequestException("Patient not found")

        patient.update(**patient_model.model_dump())
        patient = await self.__repository.save_patient(patient)
        return PatientModel(**patient.__dict__)

    async def delete_patient(self, patient_id: int) -> None:
        patient = await self.__repository.get_patient_by_id(patient_id)
        if not patient:
            raise BadRequestException("Patient not found")

        await self.__repository.delete_patient(patient)
