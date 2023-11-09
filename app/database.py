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
    db.close()

def get_last_price():
    prices = Prices.select().order_by(Prices.id.desc())
    last_price = prices.get().__dict__.get("__data__")

    return last_price

create_db()