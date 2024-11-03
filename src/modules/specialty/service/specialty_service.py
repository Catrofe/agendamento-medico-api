import logging

from src.exceptions.ConflictException import ConflictException
from src.exceptions.NotFoundException import NotFoundException
from src.modules.specialty.entity.specialty import Specialty
from src.modules.specialty.models.models import RegisterSpecialty, SpecialtyModel
from src.modules.specialty.repository.specialty_repository import SpecialtyRepository


class SpecialtyService:
    def __init__(self) -> None:
        self._repository = SpecialtyRepository()

    async def create_specialty(self, request: RegisterSpecialty) -> SpecialtyModel:
        logging.info("Creating specialty")
        if await self._repository.verify_if_specialty_exists(request.name):
            logging.info("Specialty already exists")
            raise ConflictException("Specialty already exists")

        specialty = Specialty(**request.model_dump())
        await self._repository.save_entity(specialty)

        return SpecialtyModel(**specialty.__dict__)

    async def get_specialty_by_id(self, specialty_id: int) -> SpecialtyModel:
        logging.info("Getting specialty by id")
        specialty = await self._repository.get_entity_by_id(specialty_id)

        if not specialty:
            logging.info("Specialty not found")
            raise NotFoundException("Specialty not found")

        return SpecialtyModel(**specialty.__dict__)

    async def get_all_specialties(self) -> list[SpecialtyModel]:
        logging.info("Getting all specialties")
        specialties = await self._repository.get_all_entities()

        return [SpecialtyModel(**specialty.__dict__) for specialty in specialties]

    async def update_visibility_specialty(self, specialty_id: int) -> SpecialtyModel:
        logging.info("Updating visibility specialty")

        specialty = await self._repository.update_visibility_specialty_with_lock(
            specialty_id,
        )

        if not specialty:
            logging.info("Specialty not found")
            raise NotFoundException("Specialty not found")

        return SpecialtyModel(**specialty.__dict__)

    async def delete_specialty(self, specialty_id: int) -> None:
        logging.info("Deleting specialty")
        specialty = await self._repository.get_entity_by_id(specialty_id)

        if not specialty:
            logging.info("Specialty not found")
            raise NotFoundException("Specialty not found")

        await self._repository.delete_entity(specialty)
