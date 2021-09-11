import base64
import io

import gridfs
import matplotlib.pyplot as plt
from PIL import Image
from PIL.features import codecs
from bson import json_util
from bson.json_util import loads, dumps
from flask import Flask, render_template, jsonify
from flask import request
from flask import send_file
from pymongo import response

from nosql import mongo_startup

app = Flask(__name__)


@app.before_first_request
def startup():
    global db
    db = mongo_startup.global_init()


@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html')


@app.route('/findit')
def findit():  # put application's code here
    vehicles = db.vehicles

    v = vehicles.find_one({'vin': '97507329'})

    # html = '<IMG SRC='
    #

    if v['vehicle_image_gridfs']:
        fs = gridfs.GridFS(db)
        image = None
        for grid_out in fs.find({'filename': v['vehicle_image_gridfs']}, no_cursor_timeout=True):
            image = grid_out.read()

        pil_image = Image.open(io.BytesIO(image))
        byte_arr = io.BytesIO()
        pil_image.save(byte_arr, format='JPEG')
        v['vehicle_image_gridfs'] = base64.encodebytes(byte_arr.getvalue()).decode('ascii')




    return jsonify([v.vehicle])


@app.route('/_find')
def find_vehicle():  # put application's code here
    vehicles = db.vehicles
    v = vehicles.find_one({'vin': '97507329'})

    # html = '<IMG SRC='
    #

    if v['vehicle_image_gridfs']:
        fs = gridfs.GridFS(db)
        image = None
        for grid_out in fs.find({'filename': v['vehicle_image_gridfs']}, no_cursor_timeout=True):
            image = grid_out.read()


        pil_image = Image.open(io.BytesIO(image))
        MAX_SIZE=(60,60)
        pil_image.thumbnail(MAX_SIZE)
        byte_arr = io.BytesIO()
        pil_image.save(byte_arr, format='JPEG')
        v['vehicle_image_gridfs'] = base64.encodebytes(byte_arr.getvalue()).decode('ascii')
    data_list = list()
    data_list.append(v)
    data_str = dumps(data_list)

    return data_str


if __name__ == '__main__':
    app.run()
