from typing import List
from fastapi import FastAPI, Response,status  # ASGI
from beerlog.core import get_beer_from_db
from beerlog.serializers import BeerIn, BeerOut
from beerlog.database import get_session
from beerlog.models import Beer

api = FastAPI(title="Beerlog")


@api.get("/beers/", response_model=List[BeerOut])
async def list_beers():
    beers = get_beer_from_db()
    return beers


@api.post("/beers/", response_model=BeerOut)
async def add_beer(beer_in: BeerIn, response: Response):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    response.status_code = status.HTTP_201_CREATED
    return beer
