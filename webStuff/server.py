from flask import Flask, render_template, url_for, request
import os
import csv

app = Flask(__name__)

def readtextfile(x):
    Teams = {}
    with open('static/Games/game'+str(x)+'Bare.out','r') as inf:
        Teams = eval(inf.read())
    return Teams

@app.route('/', methods=['GET', 'POST'])
def Reservations():
    print("Future of Forestry Reservations")

    x = "Future of Forestry Reservations"

    return render_template('Homepage.html', x=x)

'''
@app.route('/results/', methods=['GET', 'POST'])
def results():
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args

	query = data.get('searchterm')
	print("You searched for: " + query)
	firstName = ['Ben','Sarah', 'Xandar', 'Ellewyn']
	lastName = ['McCamish', 'G', 'Quazar', 'Sabbeth']
	return render_template('results.html', query=query, results=zip(firstName, lastName))
'''
#Found at URL: http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
	app.run(debug=True)
