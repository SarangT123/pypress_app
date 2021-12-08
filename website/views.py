from website import app
from flask import render_template, url_for, flash, redirect, session, request


@app.route('/')
def home():
    return render_template('home.html')
