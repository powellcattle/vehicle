import base64
import io
import re

import gridfs
from PIL import Image
import datetime

# def date_encoder( date_time : datetime):
#     return date_time.datetime.

def gridfs_bytes(_db,_file_name : str,_format : str):
    fs = gridfs.GridFS(_db)
    image = None
    for grid_out in fs.find({'filename': _file_name}, no_cursor_timeout=True):
        image = grid_out.read()

    pil_image = Image.open(io.BytesIO(image))
    MAX_SIZE = (60, 60)
    pil_image.thumbnail(MAX_SIZE)
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format=_format)

    return base64.encodebytes(byte_arr.getvalue()).decode('ascii')

def parse_usd(value: str):
    pattern = r'[\$,]'
    if value:
        return int(re.sub(pattern,'',value))
    else:
        return None

def parse_csv_date(value: str):
    if value:
        return datetime.datetime.strptime(value,'%m/%d/%Y')
    else:
        return

