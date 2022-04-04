import datetime


def is_date(date):
    format = "%d-%m-%Y"
    try:
        datetime.datetime.strptime(date, format)
        return True
    except ValueError:
        return False


def is_sexe(sex):
    sex = sex.upper()
    if sex == "F" or sex == "M":
        return True
    else:
        return False


def is_time(time):
    format = "%H-%M"
    try:
        datetime.datetime.strptime(time, format)
        return True
    except ValueError:
        return False
