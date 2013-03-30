from os.path import abspath, dirname, join
import unittest

from mtj.evedb.core import init_db

path = lambda x: join(dirname(abspath(__file__)), x)


class TestCase(unittest.TestCase):

    def setUp(self):
        init_test_db()


def test_db_path():
    return 'sqlite:///' + path('ret107.slimtest.sqlite')

def init_test_db():
    init_db(test_db_path())
