import datetime
from unittest import mock

from app.main import outdated_products


def test_outdated_products_single_outdated() -> None:
    fake_today = datetime.date(2022, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["duck"]


def test_all_products_outdated() -> None:
    fake_today = datetime.date(2022, 2, 10)
    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 30
        },
        {
            "name": "cheese",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 80
        },
    ]

    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["milk", "cheese"]


def test_no_products_outdated() -> None:
    fake_today = datetime.date(2022, 1, 1)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120},
    ]

    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        mock_datetime.date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == []
