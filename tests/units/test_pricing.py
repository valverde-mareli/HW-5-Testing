import pytest
from pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

@pytest.mark.parametrize("text, expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == expected


@pytest.mark.parametrize("text", [
    "",
    "abc",
])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)

@pytest.mark.parametrize("value, expected", [
    (1, "$1.00"),
    (1.2, "$1.20"),
    (1.234, "$1.23"),
    (1.235, "$1.24"),  
])
def test_format_currency_rounding(value, expected):
    assert format_currency(value) == expected

def test_apply_discount_zero_percent():
    assert apply_discount(100.0, 0) == 100.0


def test_apply_discount_negative_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)

def test_add_tax_default_rate():
    assert add_tax(100.0) == pytest.approx(107.0)


def test_add_tax_custom_rate():
    assert add_tax(100.0, 0.10) == pytest.approx(110.0)


def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(100.0, -0.01)

def test_bulk_total_simple_no_discount_no_tax():
    prices = [10.0, 5.0, 2.5]
    assert bulk_total(prices, discount_percent=0, tax_rate=0) == 17.5


def test_bulk_total_with_discount_and_tax():
    prices = [10.0, 20.0]
    total = bulk_total(prices, discount_percent=10, tax_rate=0.10)
    assert pytest.approx(total, rel=1e-9) == 29.7

