from unittest import TestSuite, makeSuite

from mtj.evedb.map import Map
from mtj.evedb.tests.base import TestCase


class MapTestCase(TestCase):

    def test_0001_get_celestial(self):
        evemap = Map()
        result = evemap.getCelestial(40300804)
        self.assertEqual(result['itemName'], u'K-6K16 V - Moon 1')
        result = evemap.getCelestial(itemName=u'K-6K16 V - Moon 1')
        self.assertEqual(result['itemID'], 40300804)
        self.assertRaises(TypeError, evemap.getCelestial)

    def test_0001_get_solar_system(self):
        evemap = Map()
        result = evemap.getSolarSystem(30004751)
        self.assertEqual(result['solarSystemName'], u'K-6K16')
        self.assertEqual(result['regionName'], u'Delve')
        result = evemap.getSolarSystem(solarSystemName=u'K-6K16')
        self.assertEqual(result['solarSystemID'], 30004751)
        self.assertRaises(TypeError, evemap.getSolarSystem)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(MapTestCase))
    return suite
