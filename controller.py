from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)


@app.route('/portfolio')
def home_page():
    return render_template('index.html')


app.run(port=5000,debug=False,host='0.0.0.0')
