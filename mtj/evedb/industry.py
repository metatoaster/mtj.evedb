from sqlalchemy import and_
from sqlalchemy.sql import select

from mtj.evedb.core import Db
from mtj.evedb.types import name_to_typeID


class Industry(Db):

    # XXX see if typeName is actually required argument here
    @name_to_typeID
    def getActivity(self, typeID=None, typeName=None):
        """
        Get the available activities for a given typeID or typeName

        This function typically apply to blueprints, relics and other
        materials that have industry activities associated with it.
        For final products, try to use the manufacture method from this
        class.
        """

        table = self.metadata.tables['industryActivity']
        condition = table.c.typeID == typeID
        stmt = select([table], condition)

        return self.select(stmt)

    def getActivityMaterials(self, typeID, activityID):
        """
        Collect the manifest of material requirements for a given
        typeID.
        """

        table = self.metadata.tables['industryActivityMaterials']
        condition = ((table.c.typeID == typeID) &
            (table.c.activityID == activityID))
        stmt = select([table], condition)
        return self.select(stmt)

    # this is a subset function
    @name_to_typeID
    def getBlueprintFor(self, typeID=None, typeName=None, activityID=1):
        table = self.metadata.tables['industryActivityProducts']
        condition = ((table.c.productTypeID == typeID) &
            (table.c.activityID == activityID))
        stmt = select([table.c.typeID], condition)
        r = self.selectUnique(stmt)
        return r.get('typeID')

    @name_to_typeID
    def material_requirements_for(self, typeID=None, typeName=None,
            activityID=1):
        """
        Get the manifest of direct material requirements that are needed
        to manufacture the given item.
        """

        targetTypeID = self.getBlueprintFor(typeID, activityID)

        if not targetTypeID:
            return None

        return self.getActivityMaterials(targetTypeID, activityID)
