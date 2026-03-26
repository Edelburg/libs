"""
Generische Basis-Exception für alle Apps im Monorepo.

Verwendung:
    from libs.python.core import AppError

    class MyAppError(AppError):
        pass

    class NotFoundError(AppError):
        def __init__(self, resource_id: str) -> None:
            super().__init__(
                message=f"Resource not found: {resource_id}",
                code="NOT_FOUND",
                details={"id": resource_id},
            )

Error-Codes Konvention (aus techstack.yaml):
    ERR_NOT_FOUND          → 404-äquivalent
    ERR_UNAUTHORIZED       → 401-äquivalent
    ERR_VALIDATION         → 422-äquivalent
    ERR_TIMEOUT            → 504-äquivalent
    ERR_SERVICE_UNAVAILABLE→ 503-äquivalent
    ERR_DUPLICATE          → Duplikat erkannt
    ERR_INTERNAL           → unerwarteter Fehler (default)
"""

from __future__ import annotations


class AppError(Exception):
    """
    Basis-Exception für alle Apps.

    Jede App leitet ihre eigene Hierarchie davon ab:
        HomeDesk → HomeDeskError(AppError)
        SolBot   → BotError(AppError)
    """

    def __init__(
        self,
        message: str,
        code: str = "ERR_INTERNAL",
        details: dict | None = None,
    ) -> None:
        self.message = message
        self.code = code
        self.details: dict = details or {}
        super().__init__(message)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(code={self.code!r}, message={self.message!r})"
