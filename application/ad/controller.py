import os

from PIL import Image
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user
from werkzeug.utils import secure_filename

from application import db
from application.ad.form import AdForm
from application.models import Ad, AdPhoto, Categories

upload_folder = "application/static/uploads/"


def save_ad(new_ad, files):
    db.session.add(new_ad)
    db.session.commit()
    upload_photo(new_ad.id, files)


def create_ad():
    form = AdForm()
    form.category.choices = Categories
    if request.method == 'POST':
        files = request.files.getlist('file')
        new_ad = Ad(
            form.title.data,
            form.category.data,
            form.description.data,
            current_user.id
        )
        save_ad(new_ad, files)
        return redirect(url_for('ad.show_ad', ad_id=new_ad.id))
    return render_template('ad/creating.html', title='Creating ad', form=form)


def allowed_file(filename):
    allowed_extensions = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def save_file_in_static(file, file_name, ad_id):
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


def upload_photo(ad_id, files):
    for file in files:
        print(file, flush=True)
        if file and allowed_file(file.filename):
            file_name = secure_filename(file.filename)
            if check_size(file) > 1024 * 1024 + 1:
                file = resize_image(file)
            try:
                path = os.path.join(upload_folder, str(ad_id))
                os.mkdir(path)
                save_file_in_static(file, file_name, str(ad_id))
            except FileExistsError:
                save_file_in_static(file, file_name, str(ad_id))
            finally:
                file_path = '/uploads/' + str(ad_id) + '/' + file_name
                photo = AdPhoto(file_path, ad_id)
                db.session.add(photo)
                db.session.commit()


def show_ad(ad_id):
    ad = Ad.query.get(ad_id)
    return render_template('ad/show_ad.html', ad=ad, photos=ad.ad_photos, user=ad.user)


def edit_ad(ad_id):
    print('00000000000000')
    ad = Ad.query.get(ad_id)
    print('111111111111111111')
    form = AdForm(request.form, obj=ad)
    print('222222222222222222222')
    form.category.choices = Categories
    print('FORM CATEGORY',form.category.data, flush=True)
    if request.method == 'POST':
        form.populate_obj(ad)
        db.session.commit()
        return render_template('ad/show_ad.html', ad=ad, photos=ad.ad_photos, user=ad.user)
    return render_template('ad/edit_ad.html', ad=ad, form=form)

# import shutil
# import stat

def delete_ad(ad_id):
    ad = Ad.query.get(ad_id)
    db.session.delete(ad)
    db.session.commit()
    flash(f'The project {ad.title} has been deleted')
    # shutil.rmtree("../static/uploads/101/back.jpg")
    return redirect(url_for('main.index'))

