import datetime


def time_finder():
    date = datetime.datetime.now()
    return date.strftime("%M")
