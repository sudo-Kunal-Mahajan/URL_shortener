from flask import Blueprint,render_template,request,flash,redirect,jsonify
from shorten.web.models import NewShortendURL
import shorten.utils.sql_utils as sql_utl

web = Blueprint('web', __name__)

@web.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

@web.route('/',methods=['GET','POST'])
def home():
    form = NewShortendURL(request.form)
    if request.method=='POST' and form.validate:
        user_url = request.form['url']
        is_shortened = sql_utl.get_shortened_url(user_url)
        if(is_shortened is None):
            new_short_url = sql_utl.add_new_mapping(user_url)
            flash(f"URL Shortened successfully {request.base_url +new_short_url}","success")
        else:
            flash(f"URL already shortened earlier {request.base_url +is_shortened}","warning")

        return render_template('home.html',form=form,all_mappings = sql_utl.get_all_url_mappings(),base_url = request.base_url)
    else:
        return render_template('home.html',form=form,all_mappings = sql_utl.get_all_url_mappings(),base_url = request.base_url )

@web.route('/<short_url>')
def go_to_url(short_url):
    mapping = sql_utl.get_long_url(short_url)
    if mapping is None:
        return render_template("error.html"),404
    else:
        return redirect(mapping)