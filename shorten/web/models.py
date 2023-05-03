from flask_wtf import Form
from wtforms import EmailField
from wtforms import validators
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Shorten_urls(db.Model):
    shorten_url = db.Column(db.String(10), primary_key=True) # primary keys are required by SQLAlchemy
    full_url = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100),default = "abc@gmail.com")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class NewShortendURL(Form):
    url = EmailField('email',[validators.DataRequired()])

    
