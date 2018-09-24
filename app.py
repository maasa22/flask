# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pandas as pd


app = Flask(__name__)


# Main
def picked_up():
    messages = [
        "やあ！どこの県庁所在地を知りたい？",
        "あなたの出身県を教えてね"
    ]
    return np.random.choice(messages)

# Routing
@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは"
    df = pd.read_csv('./prefecture.csv')

    if request.method == 'POST':
        name = request.form['name']
        df_row = df[df['prefecture'].str.contains(name)]
        if len(df_row.city.values) > 0:
            city = df_row.city.values[0]
        else:
            city = df_row.city.values
        return render_template('index.html',
                               input=name, name=city, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
