from sqlalchemy.sql import select
from mtj.evedb.core import Db


class Map(Db):

    def getCelestial(self, itemID=None, itemName=None):
        """
        Get the celestial name by its id or name.
        """

        table = self.metadata.tables['mapDenormalize']

        if itemID:
            condition = table.c.itemID == itemID
        elif itemName:
            condition = table.c.itemName == itemName
        else:
            raise TypeError('either itemID or itemName must be provided.')

        stmt = select([table], condition)

        return self.selectUnique(stmt)

    def getSolarSystem(self, solarSystemID=None, solarSystemName=None):
        """
        Get a solar system by its id or name.

        solarSystemID
            the id of the solar system.
        solarSystemName
            the name of the solar system.

        solarSystemID takes precedence.
        """

        table = self.metadata.tables['mapSolarSystems']

        if solarSystemID:
            condition = table.c.solarSystemID == solarSystemID
        elif solarSystemName:
            condition = table.c.solarSystemName == solarSystemName
        else:
            raise TypeError('either solarSystemID or solarSystemName must be '
                            'provided.')

        stmt = select([table], condition)

        return self.selectUnique(stmt)
