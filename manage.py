"""Migrations script to handle changes in data models."""

from app import db, app
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from wsp.models import Observation, Stgs # noqa
from xlrd import open_workbook

# Manager instance
manager = Manager(app)

# Set up migrate commands
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def initdb():
    """Create all tables."""
    db.create_all()
    print('Initialised the database')


@manager.command
def dropdb():
    """Clear all the data in the tables."""
    if prompt_bool("Are you sure you want to loose all your data?"):
        db.drop_all()
        print("Dropped the database")


@manager.command
def populatedb():
    """Populate all the data in the tables."""
    if prompt_bool("Are you sure you want to add the data?"):
        wb = open_workbook("wsp.xlsx")
        sheet = wb.sheets()[1]
        for row in range(2, sheet.nrows):
            obj = Stgs(title=sheet.row(row)[2].value,
                       origin="STG",
                       album=sheet.row(row)[4].value,
                       tempo=sheet.row(row)[5].value,
                       category=sheet.row(row)[1].value,
                       language=sheet.row(row)[6].value,
                       )

            db.session.add(obj)
            db.session.commit()
            obj = ''

        print("Database Populated")


@manager.command
def migratedb():
    """Migrates the DB."""
    if prompt_bool("Are you sure you want to lmigrate all data"):
        dropdb()
        initdb()
        populatedb()
        print("Database Migrated")


if __name__ == "__main__":
    manager.run()
