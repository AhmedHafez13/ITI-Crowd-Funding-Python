import re
from datetime import datetime

email_validation_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
date_validation_regex = r'\d{2}-\d{2}-\d{4}'


def is_valid_email(text):
    return re.fullmatch(email_validation_regex, text)


def is_valid_date(text):
    if bool(re.fullmatch(date_validation_regex, text)):
        try:
            return bool(datetime.strptime(text, "%d-%m-%Y"))
        except ValueError:
            return False
    else:
        return False
