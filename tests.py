"""
2014 February 10-16
###################

:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary

Weekly Summary
==============


Daily Summaries
===============


Monday, February 10
-------------------


Tuesday, February 11
--------------------


Wednesday, February 12
----------------------


Thursday, February 13
---------------------


Friday, February 14
-------------------


"""

from __init__ import (restructured_title, make_text_date, Formatter,
                      make_date_monday)
import datetime as dt
import unittest
from nose.tools import eq_


def test_restructured_title():
    eq_(restructured_title("A title", "="), "A title\n=======")


def test_make_text_date():
    eq_(make_text_date(dt.date(2014, 2, 10)), "Monday, February 10")


def test_make_date_monday():
    days = [dt.date(2014, 2, 10) + dt.timedelta(i) for i in xrange(7)]
    exp_results = [dt.date(2014, 2, 10)] * 7
    results = [make_date_monday(day) for day in days]
    for exp, r in zip(exp_results, results):
        eq_(exp, r)


class testFormatter(unittest.TestCase):
    def setUp(self):
        self.f = Formatter(2014, 2, 13)
        self.f.format()

    def test_title_format(self):
        eq_("""2014 February 10-16
###################""", self.f.title)

    def test_tags_format(self):
        exp = """\
:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary"""
        eq_(exp, self.f.tags)

    def test_days_format(self):
        exp = """Monday, February 10
-------------------


Tuesday, February 11
--------------------


Wednesday, February 12
----------------------


Thursday, February 13
---------------------


Friday, February 14
-------------------


"""
        eq_(exp, self.f.days)

    def test_total_format(self):
        exp = """\
2014 February 10-16
###################

:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary

Weekly Summary
==============


Daily Summaries
===============


Monday, February 10
-------------------


Tuesday, February 11
--------------------


Wednesday, February 12
----------------------


Thursday, February 13
---------------------


Friday, February 14
-------------------


"""
        eq_(exp, self.f.result)

    def test_make_filename(self):
        eq_(self.f.filename(), "/content/summaries/201402_10-16-Weekly-Summary.rst")
