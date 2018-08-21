from flask import Flask, render_template, url_for, request
import os
import csv

app = Flask(__name__)

def csvtodict(filename):
    passreader = csv.DictReader(open(filename, 'rb'))
    dict_list = []
    for line in passreader:
        #print(line)
        dict_list.append(line)
    return dict_list

@app.route('/', methods=['GET', 'POST', 'TESTINPUT', 'ONIDUSERNAME'])
def Reservations():
    if request.method == 'POST':
    	data = request.form
    else:
    	data = request.args

    print("Future of Forestry Reservations")

    x = "Future of Forestry Reservations"

    TESTINPUT = data.get('TESTINPUT')
    ONIDUSERNAME = data.get('ONIDUSERNAME')

    #fetches current cvs for Inventry
    filename="./static/storage/test.csv"
    InventoryList = csvtodict(filename)

    #TODO: Create CSV's for inventory.
    #TODO: Clean up CSS.
    #TODO: Add buttons for submitting.
    #TODO: .
    #TODO: a query needs to be made nfor this.
    #TODO: a query needs to be made nfor this.

    #fetches current cvs for Inventry
    filename="./static/storage/OnidUsernames.csv"
    OnidList = csvtodict(filename)
    #print(OnidList)

    return render_template('Homepage.html',
        x=x,
        InventoryList=InventoryList,
        OnidList=OnidList,
        TESTINPUT=TESTINPUT,
        ONIDUSERNAME=ONIDUSERNAME)

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
