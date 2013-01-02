from sqlalchemy import and_
from sqlalchemy.sql import select

from mtj.evedb.core import Db

CONTROL_TOWER_MARKET_GROUP = 478
CONTROL_TOWER_CAPACITY_SECONDARY = 1233


class ControlTower(Db):

    def getControlTowerNames(self):
        """
        Get a list of all POS.
        """

        table = self.metadata.tables['invTypes']

        stmt = select(
                [table.c.typeID, table.c.typeName], 
                table.c.marketGroupID == CONTROL_TOWER_MARKET_GROUP,
            ).order_by(
                table.c.typeName)

        return self.select(stmt)

    def getControlTower(self, typeID=None, typeName=None):
        """
        Get a control tower

        typeID
            typeID of a control tower.
        """

        table = self.metadata.tables['invTypes']

        if typeID:
            condition = table.c.typeID == typeID
        elif typeName:
            condition = table.c.typeName == typeName
        else:
            raise TypeError('either typeID or typeName must be provided.')

        stmt = select(
                # skip decimal columns and other unimportant columns.
                [table.c.typeID, table.c.capacity, table.c.description,
                    table.c.raceID, table.c.volume, table.c.typeName,
                    table.c.mass, table.c.groupID, table.c.marketGroupID],
                and_(condition,
                    table.c.marketGroupID == CONTROL_TOWER_MARKET_GROUP)
            )

        return self.selectUnique(stmt)

    def getControlTowerStrontCapacity(self, typeID):

        table = self.metadata.tables['dgmTypeAttributes']

        stmt = select(
                [table.c.valueFloat],
                and_(
                    table.c.typeID == typeID,
                    table.c.attributeID == CONTROL_TOWER_CAPACITY_SECONDARY,
                )
            )

        return self.selectUnique(stmt, keys=['capacitySecondary'])


    def getControlTowerResource(self, typeID):
        """
        Get the resource consumption for a tower type

        typeID
            The typeID for a control tower
        """

        invTypes = self.metadata.tables['invTypes']
        invCTRes = self.metadata.tables['invControlTowerResources']

        stmt = select(
                [invTypes.c.typeName, invTypes.c.volume, invCTRes],
                invCTRes.c.controlTowerTypeID == typeID,
                invCTRes.join(invTypes, 
                    invTypes.c.typeID == invCTRes.c.resourceTypeID)
            )

        results = self.select(stmt)
        if not results:
            raise ValueError('typeid is not a control tower')

        return results
