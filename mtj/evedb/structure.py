from sqlalchemy.sql import select
from mtj.evedb.core import Db


class ControlTower(Db):

    def getControlTowerNames(self):
        """
        Get a list of all POS.
        """

        table = self.metadata.tables['invTypes']

        stmt = select(
                [table.c.typeID, table.c.typeName], 
                table.c.marketGroupID == 478,
            ).order_by(
                table.c.typeName)

        return self.execute(stmt)
