from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db, DB_URL

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# @app.cli.command('resetdb')
# def resetdb_command():
#     """Destroys and creates the database + tables."""
#
#     from sqlalchemy_utils import database_exists, create_database, drop_database
#     if database_exists(DB_URL):
#         print('Deleting database.')
#         drop_database(DB_URL)
#     if not database_exists(DB_URL):
#         print('Creating database.')
#         create_database(DB_URL)
#
#     print('Creating tables.')
#     db.create_all()
#     print('Shiny!')

if __name__ == '__main__':
    manager.run()
