# zappa_resize_image_on_fly

Resize image on the fly using flask, zappa, pillow, opencv-python

you can change the width, height and image type on the fly

usage `/image/{filename}/full/{width pixels}x{height pixels}.{extension}`

usage for face box resize `/image/{filename}/face/{width pixels}x{height pixels}.{extension}`

examples:

https://jyhmaij1l4.execute-api.us-east-1.amazonaws.com/dev/image/example/200x200.jpg

https://jyhmaij1l4.execute-api.us-east-1.amazonaws.com/dev/image/example/350x350.png