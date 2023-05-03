from flask import Blueprint,render_template,request,flash
from shorten.web.models import NewShortendURL,Shorten_urls

web = Blueprint('web', __name__)

@web.route('/',methods=['GET','POST'])
def home():
    print(Shorten_urls.query.all())
    form = NewShortendURL(request.form)
    if request.method=='POST' and form.validate:
        user_url = request.form['url']
        return render_template('success.html')
    else:
        return render_template('home.html',form=form)

