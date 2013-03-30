from unittest import TestCase, TestSuite, makeSuite

from mtj.evedb.core import Db


class MapTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0001_get_celestial(self):
        db = Db()
        self.assertTrue(db.hasTables('invTypes'))
        self.assertTrue(db.hasTables('invTypes', 'mapDenormalize'))
        self.assertFalse(db.hasTables('invTypes', 'mapDenormalize', 'aDummy'))


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(MapTestCase))
    return suite
