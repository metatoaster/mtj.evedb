from unittest import TestCase, TestSuite, makeSuite

from evedb.market import Group


class TestMarketGroup(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_original_adapter(self):
        group = Group()
        results = group.getMarketGroup()
        self.assertEqual(results[2]['marketGroupName'], u'Blueprints')
        self.assertEqual(results[3]['marketGroupName'], u'Drones')


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestMarketGroup))
    return suite
