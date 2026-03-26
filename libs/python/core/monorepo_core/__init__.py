"""
libs/python/core — Gemeinsame Basis für alle Python-Apps.

Enthält:
  - AppError: Generische Basis-Exception mit code + details
"""

from .exceptions import AppError

__all__ = ["AppError"]
