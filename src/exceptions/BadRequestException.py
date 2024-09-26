from src.exceptions.BaseException import BaseExceptionAppointment


class BadRequestException(BaseExceptionAppointment):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message, 400)
