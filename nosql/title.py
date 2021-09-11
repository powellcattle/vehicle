from enum import Enum

import pymongo.database


class State(Enum):
    AL = 1
    AK = 2
    AZ = 4
    AR = 5
    CA = 6
    CO = 8
    CT = 9
    DE = 10
    FL = 12
    GA = 13
    HI = 15
    ID = 16
    IL = 17
    IN = 18
    IA = 19
    KS = 20
    KY = 21
    LA = 22
    ME = 23
    MD = 24
    MA = 25
    MI = 26
    MN = 27
    MS = 28
    MO = 29
    MT = 30
    NE = 31
    NV = 32
    NH = 33
    NJ = 34
    NM = 35
    NY = 36
    NC = 37
    ND = 38
    OH = 39
    OK = 40
    OR = 41
    PA = 42
    RI = 44
    SC = 45
    SD = 46
    TN = 47
    TX = 48
    UT = 49
    VT = 50
    VA = 51
    WA = 53
    WV = 54
    WI = 55
    WY = 56


class Title:

    def __init__(self, title_number: str, state: State, odometer: int, title_image: bytes):
        self.title = dict()

        if title_number and type(title_number) == str:
            self.title['title_number'] = title_number
        else:
            raise ValueError('Title Number must have a value')

        if odometer and type(odometer) == int:
            self.title['odometer'] = odometer
        else:
            self.title['odometer'] = None

        if state and type(state) == State:
            self.title['state'] = state.name
        else:
            raise ValueError('State is an unknown value')

        if title_image and type(title_image) == bytes:
            self.title['image'] = title_image


def find(self):
    return NotImplemented()


def insert_one(self, db: pymongo.database.Database):
    col = db['titles']
    col.insert_one(self.atitle)


def delete(self):
    return NotImplemented()
