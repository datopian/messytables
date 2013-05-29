# -*- coding: utf-8 -*-
import os
import unittest

from nose.tools import assert_equal


def horror_fobj(name):
    fn = os.path.join(os.path.dirname(__file__), '..', 'horror', name)
    return open(fn, 'rb')

from messytables import *
from htmlfile import HTMLTableSet


class ReadTest(unittest.TestCase):
    def test_read_simple_csv(self):
        fh = horror_fobj('html.html')
        table_set = HTMLTableSet(fh)
        row_set = table_set.tables[0]
        assert_equal(200, len(list(row_set)))
        row = list(row_set.sample)[0]
        assert_equal(row[0].value.strip(), 'HDI Rank')
        assert_equal(row[1].value.strip(), 'Country')

        #TODO
        #for row in list(row_set):
        #    assert_equal(4, len(row))
        #    assert_equal(row[0].type, StringType())
