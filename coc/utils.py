import datetime


def last_month_str():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    dt = last_month.strftime('%Y%m')
    return dt


def current_month_str():
    return datetime.date.today().strftime('%Y%m')
