from enum import Enum

import pymongo.database

class Contact:

    def __init__(self, **kwargs):
        self.contacts = dict()

        for key, value in kwargs.items():
            print('%s %s', key, value)

            if value and type(value) == str:
                self.contacts[key] = value.upper()
                continue
            else:
                raise ValueError('Value must have a value')

        #
        # if company and type(company) == str:
        #     self.contacts['company'] = company.upper()
        # else:
        #     company = None
        pass

    def find_one(self, db: pymongo.database.Database, query: dict):
        return db['contacts'].find_one(query)

    def insert_one(self, db: pymongo.database.Database):
        col = db['contacts']
        col.insert_one(self.contacts)

    def delete(self):
        return NotImplemented()
