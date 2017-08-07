import os
from PIL import Image
from flask import Flask, send_file
from flask import make_response
from io import BytesIO

from detect_face import detect_face

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
pic_path = os.path.join(dir_path, 'example')


@app.route('/example')
def example():
    """Serves raw image image."""
    with open(os.path.join(dir_path, 'example'), 'rb') as bites:
        return send_file(BytesIO(bites.read()),
                         attachment_filename='example.jpg',
                         mimetype='image/jpg')


@app.route('/image/<face_only>/<int:width>x<int:height>.<ext>', methods=['GET'])
def image(face_only, width, height, ext, name=pic_path):
    """Serves image image according to params."""

    face_box = detect_face(name)
    img = Image.open(name)
    if face_box and face_only == 'face':
        img2 = img.crop(face_box)
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

    buffer = BytesIO()
    image_format = "jpeg" if ext == "jpg" else ext
    img.save(buffer, format=image_format.capitalize())

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = "image/" + ext
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
