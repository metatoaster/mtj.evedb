from unittest import TestCase, TestSuite, makeSuite

from mtj.evedb.map import Map


class MapTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_0001_get_celestial(self):
        evemap = Map()
        result = evemap.getCelestial(40300803)
        self.assertEqual(result['itemName'], u'K-6K16 V')
        result = evemap.getCelestial(itemName=u'K-6K16 V')
        self.assertEqual(result['itemID'], 40300803)
        self.assertRaises(TypeError, evemap.getCelestial)

    def test_0001_get_solar_system(self):
        evemap = Map()
        result = evemap.getSolarSystem(30004751)
        self.assertEqual(result['solarSystemName'], u'K-6K16')
        result = evemap.getSolarSystem(solarSystemName=u'K-6K16')
        self.assertEqual(result['solarSystemID'], 30004751)
        self.assertRaises(TypeError, evemap.getSolarSystem)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(MapTestCase))
    return suite
