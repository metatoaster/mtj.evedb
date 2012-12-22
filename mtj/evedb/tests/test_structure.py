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


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(StructureTestCase))
    return suite
