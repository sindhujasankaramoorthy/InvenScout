from pydantic import BaseModel


class Patent(BaseModel):
    title: str
    publication_number: str | None = None
    filing_date: str | None = None
    snippet: str | None = None
    link: str | None = None