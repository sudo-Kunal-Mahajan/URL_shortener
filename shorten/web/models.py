from flask_wtf import Form
from wtforms import URLField
from wtforms import validators
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Shorten_urls(db.Model):
    shorten_url = db.Column(db.String(10), primary_key=True) # primary keys are required by SQLAlchemy
    full_url = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100),default = "abc@gmail.com")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return f"Short: {self.shorten_url} \n Full {self.full_url} \n Email {self.email} \n Created {self.created_at}"
class NewShortendURL(Form):
    url = URLField('url',[validators.DataRequired()])

    
