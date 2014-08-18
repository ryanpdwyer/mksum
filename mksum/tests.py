"""
2014 February 10-16
###################

:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary

Monday, February 10
===================


Tuesday, February 11
===================


Wednesday, February 12
======================


Thursday, February 13
=====================


Friday, February 14
===================


"""

from __init__ import (restructured_title, make_text_date, Formatter,
                      make_date_monday)
import datetime as dt
import unittest
from nose.tools import eq_, assert_raises
import os


def diff_lines(s1, s2):
    """Return a tuple of lines that are different
    between string 1 and string 2."""
    s1_lines = s1.splitlines()
    s2_lines = s2.splitlines()
    diff = [(s1i, s2i) for s1i, s2i in zip(s1_lines, s2_lines) if s1i != s2i]
    if diff != []:
        raise AssertionError("The lines:\n{}\nare different.".format(diff))


def test_diff_lines():
    a = "A title\nAn author"
    b = "A title\nAn auther"
    exp = [("An author", "An auther")]
    assert_raises(AssertionError, diff_lines, a, b)


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


class TestFormatter(unittest.TestCase):
    def setUp(self):
        self.f = Formatter(dt.date(2014, 2, 13))
        self.f.format()
        self.f_mar = Formatter(dt.date(2014, 3, 17))
        self.f_mar.format()
        self.filename = "content/summaries/201402_10-16-Weekly-Summary.rst"
        self.file_contents = """\
2014 February 10-16
###################

:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary

Monday, February 10
===================


Tuesday, February 11
====================


Wednesday, February 12
======================


Thursday, February 13
=====================


Friday, February 14
===================


"""

    def test_title_format(self):
        diff_lines("""2014 February 10-16
###################""", self.f.title)
        diff_lines("2014 March 17-23\n################", self.f_mar.title)

    def test_tags_format(self):
        exp = """\
:author: Ryan Dwyer
:date: 2014-02-10
:modified: 2014-02-10
:subtitle:  Weekly Summary
:tags: summary"""
        diff_lines(exp, self.f.tags)

    def test_days_format(self):
        exp = """\
Monday, February 10
===================


Tuesday, February 11
====================


Wednesday, February 12
======================


Thursday, February 13
=====================


Friday, February 14
===================


"""
        diff_lines(exp, self.f.days)

    def test_total_format(self):
        diff_lines(self.file_contents, self.f.result)

    def test_filename(self):
        eq_(self.f.filename, self.filename)

    def test_write_file(self):
        self.f.write_file()
        with open(self.filename, 'rb') as f:
            filedata = f.read()
        eq_(filedata, self.file_contents)
        os.remove(self.f.filename)


class TestFilenameExists(unittest.TestCase):
    def setUp(self):
        self.f = Formatter(dt.date(2014, 2, 10))
        self.f.format()
        open(self.f.filename, 'a').close()

    def tearDown(self):
        os.remove(self.f.filename)

    def test_raise_IO_error(self):
        assert_raises(IOError, self.f.write_file)


class TestFormatterFilename(unittest.TestCase):
    def setUp(self):
        self.f = Formatter(dt.date(2014, 2, 24))
        self.f.format()
        self.filename = ".test-201402_24-02-Weekly-Summary.rst"

    def test_filename_overlap_month(self):
        eq_(self.f.filename, self.filename)

    def tearDown(self):
        os.remove(self.filename)
