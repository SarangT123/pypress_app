from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,UserMixin,current_user
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.base import BaseView
import os.path as op
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

access_levels={
    'owner':0,
    'admin':1,
    'moderator':2
}

from website import views
from website import auth
from website.models import User,Admin_users
from website import error_handler
from website import cli

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if Admin_users.query.filter_by(user_id=current_user.id).first() != None:
                return True
            else:
                return False
        else:
            return False
admin = Admin(app,index_view=MyAdminIndexView())

class ModeratorView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            user = Admin_users.query.filter_by(user_id=current_user.id).first()
            if  user!= None:
                if user.access <= access_levels['moderator']:
                    return True
        return False

class AdminView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            user = Admin_users.query.filter_by(user_id=current_user.id).first()
            if  user!= None:
                if user.access <= access_levels['admin']:
                    return True
        return False

class OwnerView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            user = Admin_users.query.filter_by(user_id=current_user.id).first()
            if  user!= None:
                if user.access <= access_levels['owner']:
                    return True
        return False

class File_admin(FileAdmin):
    def is_accessible(self):
        if current_user.is_authenticated:
            user = Admin_users.query.filter_by(user_id=current_user.id).first()
            if  user!= None:
                if user.access <= access_levels['admin']:
                    return True
        return False

path = op.join(op.dirname(__file__), 'static')

admin.add_view(AdminView(User, db.session))
admin.add_view(OwnerView(Admin_users, db.session))
admin.add_view(File_admin(path, '/static/', name='Static Files'))
