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

    base_title = """2014 February {self.start.day}-{self.end.day}""".format
    base_tags = """
:author: Ryan Dwyer
:date: {self.start_iso}
:modified: {self.start_iso}
:subtitle:  Weekly Summary
:tags: summary""".format
    base_days = """\
{self.day_strings[0]}


{self.day_strings[1]}


{self.day_strings[2]}


{self.day_strings[3]}


{self.day_strings[4]}


""".format
    base = """
{self.title}

{self.tags}

Weekly Summary
==============


Daily Summaries
===============

{self.days}""".format

    def __init__(self, year, month, day):
        self.start = make_date_monday(dt.date(year, month, day))
        self.start_iso = self.start.isoformat()
        self.end = self.start + dt.timedelta(6)
        self.day_strings = [restructured_title(make_text_date(self.start
                            + dt.timedelta(i)), '-') for i in range(5)]

    def format(self):
        self.title = restructured_title(Formatter.base_title(self=self), "#")
        self.tags = Formatter.base_tags(self=self)
        self.days = Formatter.base_days(self=self)
        self.base(self=self)
