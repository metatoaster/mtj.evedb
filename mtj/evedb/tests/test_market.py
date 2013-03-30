from unittest import TestSuite, makeSuite

from mtj.evedb.market import Group
from mtj.evedb.tests.base import TestCase


class TestMarketGroup(TestCase):

    def test_0001_groupnames(self):
        group = Group()
        results = group.getMarketGroups()
        names = [i['marketGroupName'] for i in results]
        self.assertTrue(u'Blueprints' in names)
        self.assertTrue(u'Drones' in names)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestMarketGroup))
    return suite
