from website import *
from website import admin
path = op.join(op.dirname(__file__), '')

admin.add_view(File_admin_ext(path, 'templates', name='Extensions'))
from extensions import home_url
