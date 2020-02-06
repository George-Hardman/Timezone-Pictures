import datetime

# The aim of this module is to eventually return the timezone where it is currently 8pm


def time_finder():
    date = datetime.datetime.now()
    return date.strftime("%M")
