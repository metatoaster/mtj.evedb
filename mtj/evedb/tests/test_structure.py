from unittest import TestCase, TestSuite, makeSuite

from mtj.evedb.structure import ControlTower


class StructureTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0001_all_control_tower(self):
        pos = ControlTower()
        results = pos.getControlTowerNames()
        names = [i['typeName'] for i in results]
        self.assertTrue(u'Caldari Control Tower' in names)
        self.assertFalse(u'QA Fuel Control Tower' in names)

    def test_1001_control_tower_resource(self):
        pos = ControlTower()
        results = pos.getControlTowerResource(12235)
        self.assertEqual(len(results), 8)
        names = [i['typeName'] for i in results]
        self.assertTrue(u'Amarr Fuel Block' in names)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(StructureTestCase))
    return suite