import re
from datetime import datetime

def validate_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, value))

def validate_phone(value):
    if re.fullmatch(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return True
    if re.fullmatch(r'^\+7\d{10}$', value):
        return True
    if re.fullmatch(r'^\+7[\(\s-]?\d{3}[\)\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$', value):
        return True
    return False

def validate_date(value):
    for fmt in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            continue
    return False

def detect_field_type(value):
    if validate_date(value):
        return 'date'
    if validate_phone(value):
        return 'phone'
    if validate_email(value):
        return 'email'
    return 'text'