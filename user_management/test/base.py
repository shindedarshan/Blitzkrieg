# user_management/test/base.py

from flask_testing import TestCase

from user_management.src.const import Constant
from user_management.src import app, db

class BaseTestCase(TestCase):
    """ Base test cases """
    
    def create_app(self):
        app.config.from_object(Constant.APP_SETTINGS)
        return app
    
    def setUp(self):
        db.create_all()
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()