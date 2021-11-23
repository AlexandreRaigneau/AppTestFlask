#!/usr/bin/python
# -*- Coding: Utf-8 -*-

from flask import Flask, render_template
import os

app = Flask(__name__)

# region Page Home de l'application
@app.route('/')
def index():

    # Dictionnaire de data utilisé dans le template index.html
    data = {'user' : 'Alexandre', 'machine' : 'L-4ZKGNV2'}

    # Affichage du templates index.html
    return render_template('index.html', title = 'Home', data = data)
# endregion

# region Page Folder de l'application
@app.route('/Folder')
def Folder():
    concaten = ""
    liste = []
    for parent, dnames, fnames in os.walk('files/'):
        for fname in fnames:
            filename = os.path.join(parent, fname)
            liste.append(filename)
    return render_template('machines.html', liste = liste)
# endregion

# region Page Folder de l'application
@app.route('/<path:path>')
def machines(path):
    contenu = []
    with open(path) as f:
        for line in f:
            contenu.append(line)
    return render_template('contenu.html', path = path, contenu = contenu)
# endregion

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)