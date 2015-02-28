from functools import wraps

from sqlalchemy.sql import select


def name_to_typeID(f):

    def wrapper(self, typeID=None, typeName=None, *a, **kw):
        if typeID is None and typeName:
            col = self.metadata.tables['invTypes'].c
            r = self.selectUnique(select([col.typeID], col.typeName==typeName))
            if r is not None:
                typeID = r.get('typeID')

        return f(self, typeID, typeName, *a, **kw)

    return wrapper
