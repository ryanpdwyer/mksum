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

from __init__ import restructured_title
from nose.tools import eq_


def test_restructured_title():
    eq_(restructured_title("A title", "="), "A title\n=======")

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
"""
