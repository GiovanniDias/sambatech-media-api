from datetime import datetime, date
from flask import make_response


def check_required_parameters(data):
    params = ['name', 'upload_date', 'duration', 'url']

    for param in params:
        if not bool(data.get(param)):
            raise KeyError({"arg": param})
                

def validate_date_format(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ValueError


def format_upload_date(upload_date):
    dt = datetime.strptime(upload_date, "%Y-%m-%d")
    return date(dt.year,dt.month,dt.day)


def error_message(message, status_code=400):
    return make_response(message, status_code)
    
