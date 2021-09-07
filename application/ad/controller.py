import os

from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user
from werkzeug.utils import secure_filename

from application import db
from application.ad.form import AdForm
from application.ad.utils import check_size, resize_image, allowed_file, save_file_in_static
from application.admin import is_owner
from application.models import Ad, AdPhoto, Categories


def save_ad(new_ad, files):
    db.session.add(new_ad)
    db.session.commit()
    upload_photo(new_ad.id, files)


def create_ad():
    form = AdForm()
    form.category.choices = Categories
    if request.method == 'POST':
        files = request.files.getlist('file')
        print(form.connection.data, "CONNECTION", flush=True)
        new_ad = Ad(
            form.title.data,
            form.category.data,
            form.description.data,
            form.connection.data,
            current_user.id
        )
        save_ad(new_ad, files)
        return redirect(url_for('ad.show_ad', ad_id=new_ad.id))
    return render_template('ad/creating.html', title='Creating ad', form=form)


def upload_photo(ad_id, files):
    upload_folder = "application/static/uploads/"
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
    ad = Ad.query.get(ad_id)
    is_owner(ad)
    form = AdForm(request.form, obj=ad)
    form.category.choices = Categories
    if request.method == 'POST':
        files = request.files.getlist('file')
        form.populate_obj(ad)
        upload_photo(ad.id, files)
        db.session.commit()
        return render_template('ad/show_ad.html', ad=ad, photos=ad.ad_photos, user=ad.user)
    return render_template('ad/edit_ad.html', ad=ad, form=form)


def delete_ad(ad_id):
    ad = Ad.query.get(ad_id)
    is_owner(ad)
    db.session.delete(ad)
    db.session.commit()
    flash(f'The project {ad.title} has been deleted')
    return redirect(url_for('main.index'))


def delete_ad_photo(link_id):
    photo = AdPhoto.query.get(link_id)
    is_owner(photo.ad)
    tmp = photo.ad.id
    db.session.delete(photo)
    db.session.commit()
    flash(f'Photo has been deleted')
    return redirect(url_for('ad.edit_ad', ad_id=tmp))
