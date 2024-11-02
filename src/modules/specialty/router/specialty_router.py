from fastapi import APIRouter

from src.modules.specialty.models.models import RegisterSpecialty, SpecialtyModel
from src.modules.specialty.service.specialty_service import SpecialtyService

router = APIRouter()


service = SpecialtyService()


@router.post("/specialty", status_code=201)
async def create_specialty(request: RegisterSpecialty) -> SpecialtyModel:
    return await service.create_specialty(request)


@router.get("/specialty/{specialty_id}")
async def get_specialty_by_id(specialty_id: int) -> SpecialtyModel:
    return await service.get_specialty_by_id(specialty_id)


@router.get("/specialty")
async def get_all_specialties() -> list[SpecialtyModel]:
    return await service.get_all_specialties()


@router.patch("/specialty/{specialty_id}")
async def update_visibility_specialty(specialty_id: int) -> SpecialtyModel:
    return await service.update_visibility_specialty(specialty_id)


@router.delete("/specialty/{specialty_id}")
async def delete_specialty(specialty_id: int) -> None:
    return await service.delete_specialty(specialty_id)
