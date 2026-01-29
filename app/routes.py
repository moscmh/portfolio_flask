from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Mos')


@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')