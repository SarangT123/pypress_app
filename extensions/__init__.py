from pypress import *
from pypress import admin, app
import pypress
path = op.join(op.dirname(__file__), '')

admin.add_view(File_admin_ext(path, 'templates', name='Extensions'))

from extensions import home_url, installer, manupulator_api