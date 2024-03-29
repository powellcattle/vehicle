import base64
import csv
import datetime
import io
import re

import gridfs
import pymongo
from PIL import Image
import matplotlib.pyplot as plt
from bson import Binary

from nosql.contact import Contact
from nosql.title import State, Title
from nosql.vehicle import Vehicle, Manufacture, Model
from os.path import exists as file_exists

from vehicle.util.util import parse_usd, parse_csv_date

conn_str = "mongodb://spowell:n2329w@localhost:27017/?authSource=vehicle_db"
cl = pymongo.MongoClient(conn_str)
db = cl['vehicle_db']


with open('./data/rodney - rodney inventory.csv') as csvfile:
    inventory_reader = csv.reader(csvfile, delimiter=',')
    next(inventory_reader)

    for row in inventory_reader:

        filename = None
        filename = row[7] + '.jpg'
        if file_exists('images/' + filename):
            fs = gridfs.GridFS(db)
            with open('images/' + filename, 'rb') as f:
                contents = f.read()
            fs.put(contents, filename=filename)
        else:
            filename = None

        v = Vehicle(
            _id=(None, int(row[0]))[row[0] is not None],
            purchase_date=parse_csv_date(row[1]),
            manufacture=row[2],
            model=row[3],
            year=(None, int(row[4]))[row[4] is not None],
            purchase_price=parse_usd(row[5]),
            shipping_cost=parse_usd(row[6]),
            vin=row[7],
            add_cost=parse_usd(row[8]),
            seller=None,
            title=None,
            vehicle_image_gridfs=filename
        )
        v.insert_one(db)

# contact = Contact(first_name='scot', last_name='powell')
# contact.insert_one(db)
# seller = contact.find_one(db, {'first_name': 'SCOT', 'last_name': 'POWELL'})
#
# fs = gridfs.GridFS(db)
# filename = 'C144FS151875.jpg'
# with open('images/c10.JPG', 'rb') as f:
#     contents = f.read()
# fs.put(contents, filename=filename)
#
# #
# for grid_out in fs.find({'filename': 'C144FS151875.jpg'}, no_cursor_timeout=True):
#     image = grid_out.read()
#
# pil_image = Image.open(io.BytesIO(image))
# byte_arr = io.BytesIO()
# pil_image.save(byte_arr, format='JPEG')
# encoded_image = base64.encodebytes(byte_arr.getvalue()).decode('ascii')
#
# pass
#
# im = io.StringIO(open('images/c10.JPG', 'rb').read())
# binary_im = Binary(im)
# im.show()
#
# with open("images/c10.JPG", "rb") as imageFile:
#     c10_bytes = base64.b64encode(imageFile.read())
#
# with open("images/title.JPG", "rb") as imageFile:
#     title_bytes = base64.b64encode(imageFile.read())

# atitle = Title(title_number='19600705023', state=State.TX, odometer=79, title_image=title_bytes)

# img = Image.open('images/c10.JPG')
# imgByteArr = io.BytesIO()
# img.save(imgByteArr, 'JPEG')
# imgByteArr = imgByteArr.getvalue()

# v = Vehicle(_id=1,
#             vin='C144FS151875',
#             manufacture=Manufacture.CHEVROLET,
#             model=Model.C10,
#             year=1965,
#             purchase_date=datetime.datetime(year=2021, month=6, day=27),
#             purchase_price=8250,
#             title=None,
#             seller=None,
#             vehicle_image_gridfs=filename,
#             shipping_cost=900,
#             add_cost=int(635.59)
#
#             )
# v.insert_one(db)

# pil_img = Image.open(io.BytesIO(v.vehicle['vehicle_image']))
# plt.imshow(pil_img)
# plt.show()

