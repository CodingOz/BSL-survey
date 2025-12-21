from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

@app.template_filter("getattr")
def jinja_getattr(obj, attr):
    return getattr(obj, attr)

from app import views
