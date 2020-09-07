from datetime import datetime


def check_required_parameters(data):
    params = ['name', 'upload_date', 'duration', 'url']

    for param in params:
        if not bool(data.get(param)):
            raise KeyError({"arg": param})
        elif param == 'upload_date':
            try:
                datetime.strptime(data.get(param), "%Y-%m-%d")
            except (TypeError, ValueError):
                raise ValueError

