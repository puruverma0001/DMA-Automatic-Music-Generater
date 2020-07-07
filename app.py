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

# The entry Point
@app.route('/')
def home():
    return render_template('index.html')


# Initializing the model (This will be automactically called from the templates index.html)
@app.route('/dashboard',methods=['GET'])
def dashboard():
    musicGenerator.setupModel();
    return render_template('dashboard.html')


# Downloading the generated music
@app.route('/generatemusic',methods=['GET'])
def generateMusic():
    musicGenerator.generateMusic(musicGenerator.X_test,
                                musicGenerator.y_test,
                                musicGenerator.no_of_timesteps,
                                musicGenerator.unique_x)
    path = 'music.mid'
    return send_file(path, as_attachment=True)



app.run(port=5000)
