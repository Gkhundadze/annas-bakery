import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Conf:
    Debug = True
    Testing =True
    SECRET_KEY = "121dasdasd"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_REGISTERABLE = True # es gadasamowmebelia

