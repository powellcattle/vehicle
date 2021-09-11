from enum import Enum
import datetime

import bson.objectid
import pymongo.database

from nosql.title import Title


class Manufacture(Enum):
    CHEVROLET = 1
    GMC = 2
    PONTIAC = 3
    OLDSMOBILE = 4
    CADILLAC = 5
    FORD = 10
    MERCURY = 11
    DODGE = 20
    PLYMOUTH = 21
    TOYOTA = 30


class Model(Enum):
    CORVETTE = 1
    F250 = 2
    JIMMY = 3
    BLAZER = 4
    K10 = 5
    C10 = 6
    F1 = 7
    F2 = 8
    F3 = 9
    F100 = 10
    F150 = 150


class Vehicle:

    def __init__(self,
                 _id: int,
                 vin: str,
                 manufacture: Manufacture,
                 model: Model,
                 year: int,
                 vehicle_image_gridfs: str,
                 purchase_date: datetime,
                 purchase_price: int,
                 title: Title,
                 seller: bson.objectid.ObjectId,
                 shipping_cost: int,
                 add_cost: int):
        self.vehicle = dict()
        if _id and type(_id) == int:
            self.vehicle['_id'] = _id
        else:
            raise ValueError('Stock Number must have a value')

        if vin and type(vin) == str:
            self.vehicle['vin'] = vin
        else:
            raise ValueError('VIN must have a value')

        if manufacture and type(manufacture) == Manufacture:
            self.vehicle['manufacture'] = manufacture.name
        else:
            raise ValueError('Manufacture is an unknown value')

        if model and type(model) == Model:
            self.vehicle['model'] = model.name
        else:
            raise ValueError('Model is an unknown value')

        if year and type(year) == int:
            self.vehicle['year'] = year
        else:
            raise ValueError('Year is an unknown value')

        if seller and type(seller) == bson.objectid.ObjectId:
            self.vehicle['seller'] = seller
        else:
            self.vehicle['seller'] = None

        if vehicle_image_gridfs and type(vehicle_image_gridfs) == str:
            self.vehicle['vehicle_image_gridfs'] = vehicle_image_gridfs
        else:
            self.vehicle['vehicle_image_gridfs'] = None

        if purchase_date and type(purchase_date) == datetime.datetime:
            self.vehicle['purchase_date'] = purchase_date
        else:
            raise ValueError('Purchase Date is an unknown value')

        if purchase_price and type(purchase_price) == int:
            self.vehicle['purchase_price'] = purchase_price
        else:
            raise ValueError('Purchase Date is an unknown value')

        if title and type(title) == Title:
            self.vehicle['title'] = title.title
        else:
            self.vehicle['title'] = None

        if shipping_cost and type(shipping_cost) == int:
            self.vehicle['shipping_cost'] = shipping_cost
        else:
            self.vehicle['shipping_cost'] = None

        if add_cost and type(add_cost) == int:
            self.vehicle['add_cost'] = add_cost
        else:
            self.vehicle['add_cost'] = None

    def find(self):
        # with open("test2.jpg", "wb") as fimage:
        # fimage.write(str.decode('base64'))
        return NotImplemented()

    def insert_one(self, db: pymongo.database.Database):
        col = db['vehicles']
        col.insert_one(self.vehicle)

    def delete(self):
        return NotImplemented()
