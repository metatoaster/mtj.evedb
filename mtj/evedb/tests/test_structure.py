from unittest import TestSuite, makeSuite

from mtj.evedb.structure import ControlTower
from mtj.evedb.tests.base import TestCase


class StructureTestCase(TestCase):

    def test_0001_all_control_tower(self):
        pos = ControlTower()
        results = pos.getControlTowerNames()
        names = [i['typeName'] for i in results]
        self.assertTrue(u'Caldari Control Tower' in names)
        self.assertFalse(u'QA Fuel Control Tower' in names)

    def test_0002_control_tower(self):
        pos = ControlTower()
        result = pos.getControlTower(12235)
        self.assertEqual(result['typeName'], u'Amarr Control Tower')
        self.assertEqual(result['capacity'], 140000)

        result = pos.getControlTower(20062)
        self.assertEqual(result['typeName'], u'Caldari Control Tower Small')
        self.assertEqual(result['capacity'], 35000)

        result = pos.getControlTower(typeName='Gallente Control Tower Medium')
        self.assertEqual(result['typeID'], 20063)
        self.assertEqual(result['typeName'], u'Gallente Control Tower Medium')
        self.assertEqual(result['capacity'], 70000)

    def test_1001_control_tower_resource(self):
        pos = ControlTower()
        results = pos.getControlTowerResource(12235)
        self.assertEqual(len(results), 8)
        fueltypes = sorted([(i['typeName'], i['volume']) for i in results])
        self.assertTrue((u'Amarr Fuel Block', 5) in fueltypes)
        self.assertTrue((u'Strontium Clathrates', 3) in fueltypes)

    def test_1002_control_tower_stront(self):
        pos = ControlTower()
        results = pos.getControlTowerStrontCapacity(12235)
        self.assertEqual(results['capacitySecondary'], 50000)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(StructureTestCase))
    return suite
