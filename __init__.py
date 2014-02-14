import datetime as dt


def restructured_title(string, title_char):
    underline = title_char * len(string)
    return "{string}\n{underline}".format(string=string, underline=underline)


def make_text_date(date):
    return date.strftime("%A, %B %d")


def make_date_monday(date):
    tdelta = dt.timedelta(date.weekday())
    return date - tdelta


class Formatter(object):
    def __init__(self, year, month, day):
        self.date = make_date_monday(dt.date(year, month, day))
