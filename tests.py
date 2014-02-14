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



# def testFormatter():
#     exp_result = """
# 2014 February 10-16
# ###################

# :author: Ryan Dwyer
# :date: 2014-02-10
# :modified: 2014-02-10
# :subtitle:  Weekly Summary
# :tags: summary

# Weekly Summary
# ==============


# Daily Summaries
# ===============


# Monday, February 10
# -------------------


# Tuesday, February 11
# --------------------


# Wednesday, February 12
# ----------------------


# Thursday, February 13
# ---------------------


# Friday, February 14
# -------------------


# """
#     f = Formatter(2014, 2, 10)
#     eq_(exp_result, f.format())

"""
A title
=======
"""

"""
2014 February {self.start}-{self.end}
#############################

:author: Ryan Dwyer
:date: {self.start}
:modified: {self.start}
:subtitle:  Weekly Summary
:tags: summary

Weekly Summary
==============


Daily Summaries
===============

{self.monday}

{self.tuesday}

{self.wednesday}

{self.thursday}

{self.friday}
"""
