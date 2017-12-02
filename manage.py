"""Migrations script to handle changes in data models."""

from app import db, app
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from wsp.models import SongsToGlory, Songs, Lyrics # noqa
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
        wb = open_workbook("wsp2.xlsx")
        stg = wb.sheets()[1]
        songs = wb.sheets()[0]
        lyrix = wb.sheets()[2]
        i = 0
        text = ''
        for row in range(0, 21):
            for line in range(60):
                    if lyrix.row(line+4)[i].value == '':
                        text += '$$'
                    else:
                        text += lyrix.row(line+4)[i].value
                    text += '%%'
            i += 1
            lyrics_obj = Lyrics(title=lyrix.row(2)[row].value,
                                lyrics=text)
            text = ''
            db.session.add(lyrics_obj)
            db.session.commit()
            lyrics_obj = ''
        for row in range(2, stg.nrows):
            stg_obj = SongsToGlory(title=stg.row(row)[2].value,
                                   origin="STG",
                                   album=stg.row(row)[4].value,
                                   tempo=stg.row(row)[5].value,
                                   category=stg.row(row)[1].value,
                                   language=stg.row(row)[6].value,
                                   )
            songs_obj = Songs(title=songs.row(row)[2].value,
                              origin=songs.row(row)[3].value,
                              message=songs.row(row)[6].value,
                              tempo=songs.row(row)[4].value,
                              category=songs.row(row)[1].value,
                              language=songs.row(row)[5].value,
                              )

            db.session.add(stg_obj)
            db.session.add(songs_obj)
            db.session.commit()
            stg_obj = ''
            songs_obj = ''

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