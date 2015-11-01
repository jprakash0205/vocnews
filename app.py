
"""VOC News App"""
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)

bootstrap = Bootstrap(app) #BootStrap Instance

port = int(os.getenv("PORT"))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',e=e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)