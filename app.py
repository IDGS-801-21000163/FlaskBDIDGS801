from flask import Flask, render_template
from flask_wtf import CSRFProtect

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/alumno')
def alumno():
	return render_template('alumno.html')

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(port=4000, debug=True)
