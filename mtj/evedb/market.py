from sqlalchemy.sql import select
from mtj.evedb.core import Db


class Group(Db):

    def getMarketGroups(self, parentGroupID=None):
        """\
        Get a list of market groups.

        parentGroupID
            Get all the market (sub)groups under this id.  If `None` is
            selected, the default group will be returned

            Default value: `None`

        """

        invMarketGroups = self.metadata.tables['invMarketGroups']

        stmt = select(
                [invMarketGroups], 
                invMarketGroups.c.parentGroupID == parentGroupID
            ).order_by(
                invMarketGroups.c.marketGroupName)

        return self.select(stmt)

    def getMarketGroupItems(self, marketGroupID):
        """\
        Get all items from a market group.

        marketGroupID
            Get all items from this market group.

        """

        invTypes = self.metadata.tables['invTypes']

        stmt = select(
                [invTypes], 
                invTypes.c.marketGroupID == marketGroupID
            ).order_by(
                invTypes.c.typeName)

        return self.select(stmt)

    def getType(self, typeID=None, typeName=None):
        """
        Get an item by typeID.

        typeID
            The item to get.

        """

        table = self.metadata.tables['invTypes']

        if typeID:
            condition = table.c.typeID == typeID
        elif itemName:
            condition = table.c.typeName == typeName
        else:
            raise TypeError('either typeID or typeName must be provided.')

        stmt = select(
            # skip decimal columns and other unimportant columns.
            [table.c.typeID, table.c.capacity, table.c.description,
                table.c.raceID, table.c.volume, table.c.typeName,
                table.c.mass, table.c.groupID, table.c.marketGroupID],
            condition)

        return self.selectUnique(stmt)

    def getItemID(self, typeID):
        """\
        Get an item by typeID.

        typeID
            The item to get.

        """

        invTypes = self.metadata.tables['invTypes']

        stmt = select(
                [invTypes], 
                invTypes.c.typeID == typeID,
            ).order_by(
                invTypes.c.typeName)

        return self.select(stmt)

    def getItemName(self, name):

        invTypes = self.metadata.tables['invTypes']

        stmt = select(
                [invTypes], 
                invTypes.c.typeName.like('%%%s%%' % name),
            ).order_by(
                invTypes.c.typeName)

        return self.select(stmt)
