from sqlalchemy.sql import select
from evedb.core import Db


class Group(Db):

    def getMarketGroup(self, parentGroupID=None):

        invMarketGroups = self.metadata.tables['invMarketGroups']
        stmt = select(
                [invMarketGroups], 
                invMarketGroups.c.parentGroupID == parentGroupID
            ).order_by(
                invMarketGroups.c.marketGroupName)
        results = self.conn.execute(stmt)
        keys = results.keys()
        data = []
        for row in results:
            data.append(dict(zip(keys, row)))
        return data
