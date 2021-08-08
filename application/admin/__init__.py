from flask import redirect, url_for, request, abort
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from functools import wraps

from application.models import Ad


def is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.role.name != 'admin':
            abort(403)
        return func(*args, **kwargs)

    return decorated_function


def is_owner(ad):
    if not ad.user_id == current_user.id:
        abort(403)


class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.sign_in', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass
