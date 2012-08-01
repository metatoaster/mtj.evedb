from unittest import TestCase, TestSuite, makeSuite

from evedb.market import Group


class TestMarketGroup(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

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
