from pydantic import BaseModel


class ServerTimeResultSchema(BaseModel):
    unixtime: int
    rfc1123: str


class ServerTimeResponseSchema(BaseModel):
    result: ServerTimeResultSchema
    error: list[str]
