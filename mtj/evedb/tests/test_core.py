from unittest import TestSuite, makeSuite

from sqlalchemy.sql import select

from mtj.evedb.core import Db
from mtj.evedb.tests.base import TestCase


class CoreTestCase(TestCase):

    def test_0001_test_core(self):
        db = Db()
        self.assertTrue(db.hasTables('invTypes'))
        self.assertTrue(db.hasTables('invTypes', 'mapDenormalize'))
        self.assertFalse(db.hasTables('invTypes', 'mapDenormalize', 'aDummy'))

    def test_0100_test_select(self):
        db = Db()
        table = db.metadata.tables['mapDenormalize']
        stmt = select([table], table.c.itemID == 10000058)
        results = db.select(stmt)
        self.assertEqual(len(results), 1)

        result = results[0]

        self.assertTrue(result['itemID'], 10000058)
        self.assertTrue(result['itemName'], 'Fountain')

        result = db.selectUnique(stmt, key_replacements={1: 'id'})
        self.assertTrue(result['id'], 10000058)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(CoreTestCase))
    return suite
