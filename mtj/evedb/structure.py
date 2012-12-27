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
