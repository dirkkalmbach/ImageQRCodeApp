import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# To-Do: put into separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from project.qrcode.views import qrcode_blueprint
from project.userdata.views import userdata_blueprint

app.register_blueprint(qrcode_blueprint,url_prefix="")
app.register_blueprint(userdata_blueprint,url_prefix='/userdata')