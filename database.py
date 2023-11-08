from peewee import *

db = SqliteDatabase('prices.db')
class Prices(Model):
        date = DateTimeField()
        kindle11 = FloatField()
        paperwhite = FloatField()
        paperwhiteSE = FloatField()
        oasis = FloatField()

        class Meta:
            database = db

def create_db():

    db.connect()
    db.create_tables([Prices])

if __name__ == "__main__":
    create_db()