from src.exceptions.BaseException import BaseExceptionAppointment


class ConflictException(BaseExceptionAppointment):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message, 409)
