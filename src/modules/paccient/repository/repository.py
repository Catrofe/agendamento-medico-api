from src.modules.base.repository import ContextRepository


class PaccientRepository:
    def __init__(self) -> None:
        self.__connection = ContextRepository.session_maker()
