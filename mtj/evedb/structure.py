from sqlalchemy.sql import select
from mtj.evedb.core import Db

CONTROL_TOWER_MARKET_GROUP = 478


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

    def getControlTowerResource(self, typeID):
        """
        Get the resource consumption for a tower type

        typeID
            The typeID for a control tower
        """

        invTypes = self.metadata.tables['invTypes']
        invCTRes = self.metadata.tables['invControlTowerResources']

        stmt = select(
                [invTypes.c.typeName, invCTRes], 
                invCTRes.c.controlTowerTypeID == typeID,
                invCTRes.join(invTypes, 
                    invTypes.c.typeID == invCTRes.c.resourceTypeID)
            )

        results = self.select(stmt)
        if not results:
            raise ValueError('typeid is not a control tower')

        return results
