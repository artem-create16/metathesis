import os

from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user
from werkzeug.utils import secure_filename

from application import db
from application.ad.form import AdForm
from application.models import Ad, AdPhoto, Categories


upload_folder = "application/static/uploads/"


def create_ad():
    form = AdForm()
    form.category.choices = Categories
    if request.method == 'POST':
        new_ad = Ad(
            form.title.data,
            form.category.data,
            form.description.data,
            current_user.id
            )
        print('form.category.data ---->>', form.category.data, flush=True)
        db.session.add(new_ad)
        db.session.commit()
        return redirect(url_for('ad.upload_photo', ad_id=new_ad.id))
    return render_template('ad/creating.html', title='Creating ad', form=form)


def allowed_file(filename):
    allowed_extensions = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def save_file_in_static(file, file_name, ad_id):
    file_path = os.path.join(upload_folder + str(ad_id), file_name)
    file.save(file_path)


def upload_photo(ad_id):
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            print(file, flush=True)
            if file and allowed_file(file.filename):
                file_name = secure_filename(file.filename)
                try:
                    path = os.path.join(upload_folder, ad_id)
                    os.mkdir(path)
                    save_file_in_static(file, file_name, ad_id)
                except FileExistsError:
                    save_file_in_static(file, file_name, ad_id)
                finally:
                    file_path = '/uploads/' + str(ad_id) + '/' + file_name
                    print(file_path, "WAS SAVED", flush=True)
                    photo = AdPhoto(file_path, ad_id)
                    db.session.add(photo)
                    db.session.commit()
        return redirect(url_for('ad.show_ad', ad_id=ad_id))
    return render_template('ad/photo.html')


def show_ad(ad_id):
    ad = Ad.query.get(ad_id)
    return render_template('ad/show_ad.html', ad=ad, photos=ad.ad_photos, user=ad.user)


def edit_ad(ad_id):
    ad = Ad.query.get(ad_id)
    form = AdForm(request.form, obj=ad)
    if form.validate_on_submit():
        form.populate_obj(ad)
        db.session.commit()
        return render_template('ad/show_ad.html', ad=ad, photos=ad.ad_photos, user=ad.user)
    return render_template('ad/edit_ad.html', ad=ad, form=form)


def delete_ad(ad_id):
    ad = Ad.query.get(ad_id)
    db.session.delete(ad)
    db.session.commit()
    flash(f'The project {ad.title} has been deleted')
    return redirect(url_for('main.index'))

