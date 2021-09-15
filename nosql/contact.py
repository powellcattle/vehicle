from enum import Enum

import pymongo.database


class PhoneType(Enum):
    MOBILE = 1
    WORK = 2
    HOME = 3
    OTHER = 4


class Contact:

    def __init__(self, first_name: str, last_name: str, phone_number: str, phone_type: PhoneType):
        self.contact = dict()

        if first_name and type(first_name) == str:
            self.contact['first_name'] = first_name.upper()
        else:
            raise ValueError("A valid First Name must be provided.")

        if last_name and type(last_name) == str:
            self.contact['last_name'] = last_name.upper()
        else:
            raise ValueError("A valid Last Name must be provided.")

        if phone_number and type(phone_number) == str:
            self.contact['last_name'] = phone_number.upper()
        else:
            raise ValueError("A valid Phone Number must be provided.")

        if phone_type and type(phone_type) == PhoneType:
            self.contact['phone_type'] = PhoneType.name
        else:
            raise ValueError("A valid Phone Type must be provided.")

    def find_one(self, db: pymongo.database.Database, query: dict):
        return db['contacts'].find_one(query)

    def insert_one(self, db: pymongo.database.Database):
        col = db['contacts']
        col.insert_one(self.contacts)

    def delete(self):
        return NotImplemented()
