from app import app
from flask import render_template, url_for
# import pandas as pd
# import json
# import plotly
# import plotly.express as px


@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html", title="Main Page", header="Mos")