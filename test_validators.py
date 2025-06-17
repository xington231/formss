import pytest
from validators import validate_email, validate_phone, validate_date, detect_field_type

@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("user.name+tag@domain.co.uk", True),
    ("invalid@", False),
    ("@domain.com", False),
    ("noatsign.com", False),
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected

@pytest.mark.parametrize("phone,expected", [
    ("+7 123 456 78 90", True),
    ("+7 000 000 00 00", True),
    ("8 123 456 78 90", False),
    ("+71234567890", False),
    ("+7 123 456 78", False),
])
def test_validate_phone(phone, expected):
    assert validate_phone(phone) == expected

@pytest.mark.parametrize("date,expected", [
    ("31.12.2023", True),
    ("01.01.1970", True),
    ("2023-12-31", True),
    ("1970-01-01", True),
    ("31/12/2023", False),
    ("2023/12/31", False),
    ("not a date", False),
])
def test_validate_date(date, expected):
    assert validate_date(date) == expected

@pytest.mark.parametrize("value,expected", [
    ("31.12.2023", "date"),
    ("+7 123 456 78 90", "phone"),
    ("test@example.com", "email"),
    ("plain text", "text"),
])
def test_detect_field_type(value, expected):
    assert detect_field_type(value) == expected