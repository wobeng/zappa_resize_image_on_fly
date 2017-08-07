from io import BytesIO

from PIL import Image
from flask import Flask, send_file
from flask import make_response

from detect_face import detect_face


app = Flask(__name__)


@app.route('/world')
def hello_world():
    return 'Hello, World!'


@app.route('/example')
def example():
    """Serves raw image image."""

    with open("example", 'rb') as bites:
        return send_file(BytesIO(bites.read()),
                         attachment_filename='example.jpeg',
                         mimetype='image/jpg')


@app.route('/image/<name>/<int:width>x<int:height>.<ext>', methods=['GET'])
def image(name, width, height, ext):
    """Serves image image according to params."""

    face_box = detect_face(name)
    img = Image.open(name)
    if face_box:
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
    app.run()
