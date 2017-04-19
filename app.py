from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/actinide')
def actinide():
	return render_template('actinide.html')

@app.route('/alkalimetal')
def alkalimetal():
	return render_template('alkalimetal.html')

@app.route('/alkalineearthmetal')
def alkalineearthmetal():
	return render_template('alkalineearthmetal.html')

@app.route('/argon')
def argon():
	return render_template('argon.html')

@app.route('/cadmium')
def cadmium():
	return render_template('cadmium.html')

@app.route('/calcium')
def calcium():
	return render_template('calcium.html')

@app.route('/element')
def element():
	return render_template('element.html')

@app.route('/family')
def family():
	return render_template('family.html')

@app.route('/fluorine')
def fluorine():
	return render_template('fluorine.html')

@app.route('/gas')
def gas():
	return render_template('gas.html')

@app.route('/gold')
def gold():
	return render_template('gold.html')

@app.route('/halogen')
def halogen():
	return render_template('halogen.html')

@app.route('/helium')
def helium():
	return render_template('helium.html')

@app.route('/iron')
def iron():
	return render_template('iron.html')

@app.route('/lanthanides')
def lanthanides():
	return render_template('lanthanides.html')

@app.route('/liquid')
def liquid():
	return render_template('liquid.html')

@app.route('/lithium')
def lithium():
	return render_template('lithium.html')

@app.route('/mercury')
def mercury():
	return render_template('mercury.html')

@app.route('/noblegas')
def noblegas():
	return render_template('noblegas.html')

@app.route('/phase')
def phase():
	return render_template('phase.html')

@app.route('/sodium')
def sodium():
	return render_template('sodium.html')

@app.route('/solid')
def solid():
	return render_template('solid.html')

@app.route('/transitionmetal')
def transitionmetal():
	return render_template('transitionmetal.html')


if __name__ == '__main__':
	app.run() # Run application