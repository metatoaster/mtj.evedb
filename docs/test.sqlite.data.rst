Producing a slim set of test data
=================================

I used the retribution database dump, and then used the sqlite3 to
create the slimmed down dataset for testing purposes.  A dump can be
produced like this::

    $ cat '.dump' | sqlite3 ret107.sqlite

Initially I created a dump of all the data, sort of see what might be
needed.  However a better way is to just use schema instead to extract
all the tables and indexes::

    $ echo '.schema' | sqlite3 ret107.sqlite

To save space, I only extracted the tables I needed::

    $ echo -e '.schema dgmTypeAttributes' \
           '\n.schema invTypes' \
           '\n.schema invMarketGroups' \
           '\n.schema invControlTowerResources' \
           '\n.schema invTypeReactions' \
           '\n.schema mapSolarSystems' \
           '\n.schema mapDenormalize' | \
            sqlite3 ret107.sqlite > schema.sql

Then I extracted all the table creation statements along with
the index and passed that into sqlite3::

    $ cat schema.sql | sqlite3 ret107.slimtest.sqlite

Once the required tables are created, just open the new sqlite file with
sqlite3 and then attach the original database file::

    sqlite> attach database 'ret107.sqlite' as orig;

For the core data::

    sqlite>
    begin transaction;
    -- Tower strontium bay sizes.
    insert into main.dgmTypeAttributes select * from orig.dgmTypeAttributes
        where attributeID=1233;
    -- The towers themselves.
    insert into main.invTypes select * from orig.invTypes
        where marketGroupID=478;
    -- Silo contents for moon mining and reactions.
    insert into main.invTypes select * from orig.invTypes
        where groupID=427;
    insert into main.invTypes select * from orig.invTypes
        where groupID=428;
    insert into main.invTypes select * from orig.invTypes
        where groupID=429;
    -- Fuels would be nice.
    insert into main.invTypes select * from orig.invTypes
        where typeID in (4051, 4246, 4247, 4312, 16275, 24592, 24593, 24594,
        24595, 24596, 24597);
    -- A couple market groups don't hurt (used in mtj.evedb tests also)
    insert into main.invMarketGroups select * from orig.invMarketGroups
        where marketGroupID in (2, 4, 150, 157, 478);
    -- The rest are not too terribly big.
    insert into main.invControlTowerResources select * from
        orig.invControlTowerResources;
    insert into main.invTypeReactions select * from orig.invTypeReactions;
    commit;

For the simple testing that the mtj.eve.tracker needs, the most basic
solarsystem and denormalized map information are needed.  Just execute
these statements within the same sqlite shell::

    sqlite>
    begin transaction;
    -- Includes Deklein, Fountain, Delve and Aridia.
    insert into main.mapSolarSystems select * from orig.mapSolarSystems
        where regionID=10000058;
    insert into main.mapSolarSystems select * from orig.mapSolarSystems
        where regionID=10000054;
    insert into main.mapSolarSystems select * from orig.mapSolarSystems
        where regionID=10000035;
    insert into main.mapSolarSystems select * from orig.mapSolarSystems
        where regionID=10000060;
    -- Just the selected systems needed and used by the tracker tests.
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14 and solarSystemID=30002904;
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14 and solarSystemID=30004608;
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14 and solarSystemID=30004751;
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14 and solarSystemID=30004267;
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14 and solarSystemID=30004268;
    commit;

Of course, a full set of data will be required for day-to-day running of
a pos tracker at this point in time.  Instead of just having explicit
regions and systems, just do this::

    sqlite>
    begin transaction;
    insert into main.mapSolarSystems select * from orig.mapSolarSystems;
    -- Just the moons are needed.
    insert into main.mapDenormalize select * from orig.mapDenormalize
        where typeID=14;
    commit;
