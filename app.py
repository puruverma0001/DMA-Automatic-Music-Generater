# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:03:31 2020

@author: puruv
"""

from flask import *
from Automatic_Music_Generator import *

app = Flask(__name__)

# Importing Automatic Music Generator
musicGenerator = AutomaticMusicGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard',methods=['GET'])
def dashboard():
    musicGenerator.setupModel();
    return render_template('dashboard.html')

@app.route('/generatemusic',methods=['GET'])
def generateMusic():
    musicGenerator.generateMusic(musicGenerator.X_test,
                                musicGenerator.y_test,
                                musicGenerator.no_of_timesteps,
                                musicGenerator.unique_x)
    #return render_template('playmusic.html')
    path = 'D:/Python/music.mid'
    return send_file(path, as_attachment=True)

# @app.route('/download')
# def downloadMusic():
#    path = ''
#    return send_file(path, as_attachment=True)

app.run(port=5000)
