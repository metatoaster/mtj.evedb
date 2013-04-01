import os
import logging

import sqlalchemy

MTJ_EVEDB_SRC = 'MTJ_EVEDB_SRC'


class Db(object):
    """\
    Core class.

    Creates a single persistent connection to the eve item db.
    """

    _conn = None
    _metadata = None
    _src = None

    def __init__(self, src=None):
        pass

    @property
    def conn(self):
        return Db._conn

    @property
    def metadata(self):
        return Db._metadata

    def execute(self, stmt):
        return self.conn.execute(stmt)

    def select(self, stmt, keys=None, key_replacements=None):
        results = self.execute(stmt)
        keys = keys or results.keys()

        if key_replacements:
            for k, v in key_replacements.iteritems():
                keys[k] = v

        data = []
        for row in results:
            data.append(dict(zip(keys, row)))
        return data

    def selectUnique(self, stmt, keys=None, key_replacements=None):
        data = self.select(stmt, keys, key_replacements)
        if not data:
            return None
        return data[0]

    def hasTables(self, *tables):
        """
        Validate for the presence of tables.
        """

        all_tables = self.metadata.tables.keys()
        results = [table in all_tables for table in tables]
        return False not in results


def init_db(src=None):
    if src is None:
        src = find_src()
    Db._src = src
    Db._conn = sqlalchemy.create_engine(src)
    Db._metadata = sqlalchemy.MetaData()
    # stop sqlalchemy from complaining about types (don't need them 
    # for now).
    logging.captureWarnings(True)
    Db._metadata.reflect(bind=Db._conn)
    logging.captureWarnings(False)

def find_src_from_env():
    return os.environ.get(MTJ_EVEDB_SRC)

def find_src():
    result = find_src_from_env()
    if result:
        return result

    # last ditch effort, find _any_ sqlite file in current working dir.
    cwd = os.getcwd()
    sqlite_prefix = 'sqlite:///%s/%s'
    filenames = os.listdir(cwd)
    for f in filenames:
        if f.endswith('.sqlite'):
            return sqlite_prefix % (cwd, f)
    raise ValueError('failure to locate suitable database file (%s)' % cwd)
