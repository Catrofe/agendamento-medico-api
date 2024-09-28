from src.modules.paccient.repository.repository import PaccientRepository


class PaccientService:
    def __init__(self) -> None:
        self.pacient_repository = PaccientRepository()
