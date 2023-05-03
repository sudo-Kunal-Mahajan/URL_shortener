from flask import Flask
from flask_wtf import CSRFProtect
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile("app_configs.py")

from shorten.web.views import web
app.register_blueprint(web)
csrf = CSRFProtect(app)
from shorten.web.models import db
db.init_app(app)
with app.app_context():
    db.create_all()