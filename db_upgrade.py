#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))

#When you run the above script, the database will be upgraded
# to the latest revision, by applying the migration scripts
# stored in the database repository.

#Obtained from:
#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database