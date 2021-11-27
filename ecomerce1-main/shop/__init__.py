from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager
from .conf import Conf,basedir
from .database_conf import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Conf)

# migrate
Migrate(app, db)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u'Please login first'

from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes
 