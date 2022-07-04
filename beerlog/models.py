from sqlmodel import SQLModel, Field
from sqlmodel import select
from typing import Optional
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)
    # toda vez que receber esses valores vai testar
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    # toda vez que objeto for criado ou alterado roda isso
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=4, cost=8)
