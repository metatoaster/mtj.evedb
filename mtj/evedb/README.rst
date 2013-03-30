Usage Example
=============

While the intention of this package is to enable database agnostic
access to the CCP EVE data dumps, the development is based around the
sqlite dumps provided at http://pozniak.pl/dbdump/.

For a quick demonstration (as it will take time to acquire one of those
full datadumps), a limited subset of data is provided within the test
module::

    >>> from mtj.evedb.tests import base
    >>> sqlite_path = base.test_db_path()
    >>> sqlite_path
    'sqlite:///...ret107.slimtest.sqlite'

To make use of this (or any other data sources), import from the core
module and call the init_db with the database path::

    >>> from mtj.evedb import core
    >>> core.init_db(sqlite_path)

Now any import from other evedb modules will return some useful data::

    >>> from mtj.evedb.map import Map
    >>> map = Map()
    >>> system = map.getSolarSystem(solarSystemName='K-6K16')
    >>> system['solarSystemID']
    30004751
