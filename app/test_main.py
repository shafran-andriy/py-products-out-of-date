from datetime import date
from unittest import mock

import pytest
from app.main import outdated_products


@pytest.mark.parametrize("current_product, expected_output",
                         [
                             pytest.param([
                                 {"name": "salmon",
                                  "expiration_date": date(2025, 1, 25),
                                  "price": 600},
                                 {"name": "chicken",
                                  "expiration_date": date(2025, 1, 30),
                                  "price": 120}],
                                 [],
                                 id="Expiration day today not outdated"),
                             pytest.param([
                                 {"name": "salmon",
                                  "expiration_date": date(2025, 1, 19),
                                  "price": 600}],
                                 ["salmon"],
                                 id="Expiration day yesterday outdated"),
                             pytest.param([
                                 {"name": "salmon",
                                  "expiration_date": date.today(),
                                  "price": 600}],
                                 ["salmon"],
                                 id="Expiration day today outdated")
                         ])
def test_outdated_products(current_product: list[dict],
                           expected_output: list[str]) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2025, 1, 20)
        assert outdated_products(current_product) == expected_output
