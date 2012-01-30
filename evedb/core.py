from os.path import dirname
import logging

import sqlalchemy



sqllite_src = 'sqlite:///%s/cru110-sqlite3-v1.db' % dirname(__file__)


class Db(object):
    """\
    Core class.

    Creates a single persistent connection to the eve item db.
    """

    _conn = None
    _metadata = None

    def __init__(self, src=None):
        """\
        Initializes a database connection to the provider.
        """

        init_db(src)

    @property
    def conn(self):
        return Db._conn

    @property
    def metadata(self):
        return Db._metadata


def init_db(src=None):
    if src is None:
        src = sqllite_src
    Db._conn = sqlalchemy.create_engine(src)
    Db._metadata = sqlalchemy.MetaData()
    # stop sqlalchemy from complaining about types (don't need them 
    # for now).
    logging.captureWarnings(True)
    Db._metadata.reflect(bind=Db._conn)
    logging.captureWarnings(False)
