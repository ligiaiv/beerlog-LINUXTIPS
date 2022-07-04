from unittest import result
from beerlog.core import get_beer_from_db, add_beer_to_db


def test_add_beer_to_dataset():
    assert add_beer_to_db("Blue Moon", "Witbier", 10, 3, 6)


def test_get_beer_from_db():
    # Arrange
    add_beer_to_db("Blue Moon", "Witbier", 10, 3, 6)
    # Act
    results = get_beer_from_db()
    # Assert
    assert len(results) > 0
