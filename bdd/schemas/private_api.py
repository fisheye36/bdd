from typing import Any

from pydantic import BaseModel


class OpenOrdersResultSchema(BaseModel):
    open: dict[str, Any]


class OpenOrdersResponseSchema(BaseModel):
    result: OpenOrdersResultSchema
    error: list[str]


class ErrorResponseSchema(BaseModel):
    error: list[str]
