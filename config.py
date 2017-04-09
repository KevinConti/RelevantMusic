import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Constant required by Flask-SQLAlchemy extension
#Declares path to database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#Folder where SQLAlchemy-migrate database files are stored
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
