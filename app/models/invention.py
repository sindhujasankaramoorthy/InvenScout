from pydantic import BaseModel


class InventionRequest(BaseModel):
    idea: str