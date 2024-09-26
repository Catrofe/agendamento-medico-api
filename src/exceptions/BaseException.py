from typing import TYPE_CHECKING

from fastapi.responses import JSONResponse

if TYPE_CHECKING:
    from fastapi import Request


class BaseExceptionAppointment(Exception):
    """Base class for API exceptions."""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
    ) -> None:
        self.className = self.__class__.__name__
        self.message = message
        self.statusCode = status_code
        super().__init__(message)

    @staticmethod
    async def handler(_: "Request", exc: "BaseExceptionAppointment") -> JSONResponse:
        """Handle an API error."""
        return JSONResponse(
            status_code=exc.statusCode,
            content=exc.__dict__,
        )
