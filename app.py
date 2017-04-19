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

@app.route('/flourine')
def flourine():
	return render_template('flourine.html')

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

@app.route('/page3')
def page3():
	return render_template('page3.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')


if __name__ == '__main__':
	app.run() # Run application