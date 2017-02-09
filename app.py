from flask import Flask


import base64
import cStringIO

from PIL import Image
from flask import make_response

from detect_face import detect_face

app = Flask(__name__)

@app.route('/image/<name>/<int:width>x<int:height>.<ext>', methods=['GET'])
def image(name, width, height, ext):
    face = detect_face(name)
    img = Image.open(name)
    if face:
        img2 = img.crop((face))
        img = img2

    if width == 0 and height != 0:
        hpercent = (height / float(img.size[1]))
        width = int((float(img.size[0]) * float(hpercent)))
    elif width != 0 and height == 0:
        wpercent = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(wpercent)))
    elif width == 0 and height == 0:
        width = img.size[0]
        height = img.size[1]

    img = img.resize((width, height), Image.ANTIALIAS)
    buffer = cStringIO.StringIO()
    img.save(buffer, format=ext.replace("jpg", "jpeg").capitalize())

    response = make_response(base64.b64encode(buffer.getvalue()))
    response.headers['Content-Type'] = "image/" + ext
    return response
