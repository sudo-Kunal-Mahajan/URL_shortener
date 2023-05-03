from shorten.web.models import Shorten_urls
from shorten.web.models import db
import shorten.utils.code_utils as utls

def get_all_url_mappings():
    return Shorten_urls.query.all()

def get_shortened_url(url):
    shortened = Shorten_urls.query.filter_by(full_url=url).first()
    if shortened:
        return shortened.shorten_url
    else:
        return None

def get_long_url(short_url):
    org_url = Shorten_urls.query.filter_by(shorten_url=short_url).first()
    if org_url:
        return org_url.full_url
    else:
        return None

def add_new_mapping(full_url):

    short_url = utls.generate_new_shortened_url()
    while get_long_url(short_url) is not None:
        short_url = utls.generate_new_shortened_url()

    new_url = Shorten_urls(shorten_url=short_url, full_url=full_url) #
    # add the new user to the database
    db.session.add(new_url)
    db.session.commit()
    return short_url