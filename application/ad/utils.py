import os

from PIL import Image
from flask import abort


def allowed_file(filename):
    allowed_extensions = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def save_file_in_static(file, file_name, ad_id):
    upload_folder = "application/static/uploads/"
    file_path = os.path.join(upload_folder + str(ad_id), file_name)
    file.save(file_path)


def check_size(file):
    if file.content_length:
        return file.content_length
    try:
        pos = file.tell()
        file.seek(0, 2)
        size = file.tell()
        file.seek(pos)
        return size
    except (AttributeError, IOError):
        abort(400)


def resize_image(file):
    image = Image.open(file)
    new_size = (1280, 720)
    ratio = min(float(new_size[0]) / image.size[0], float(new_size[1]) / image.size[1])
    w, h = int(image.size[0] * ratio), int(image.size[1] * ratio)
    resized_file = image.resize((w, h),)
    return resized_file
