from flask import Flask, render_template, url_for, request
import os
import csv

app = Flask(__name__)

#Returns list of csv rows
#
def csvRowsList(filename):
    with open("./static/storage/test.csv") as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
    return readCSV

#Returns specific row of csv
#
def csvSpecificRows(filename, x):
    with open("./static/storage/test.csv") as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
    return readCSV[x]

#Turns a csv into a dictionary for easier display
#
def csvtodict(filename):
    passreader = csv.DictReader(open(filename, 'rb'))
    dict_list = []
    for line in passreader:
        #print(line)
        dict_list.append(line)
    return dict_list

def Reserve():
    print("RESERVED")

#Main page
#
@app.route('/', methods=['GET', 'POST', 'Item', 'User', 'lenInventoryList', 'In', 'Out', 'Destination', 'Description', 'Rescheck', 'CheckoutTrigger'])
def Reservations():
    if request.method == 'POST':
    	data = request.form
    else:
    	data = request.args

    print("Future of Forestry Reservations")

    #TODO: Create CSV's for inventory.
    #TODO: Clean up CSS.
    #TODO: Add buttons for submitting.
    #TODO: .
    #TODO: a query needs to be made nfor this.
    #TODO: a query needs to be made nfor this.

    x = "Future of Forestry Reservations"

    Item = data.get('Item')
    User = data.get('User')

    #TODO assign these values
    In = data.get('In')
    Out = data.get('Out')
    Destination = data.get('Destination')
    Description = data.get('Description')
    CheckoutTrigger = data.get('CheckoutTrigger')
    Rescheck = 1

    if(CheckoutTrigger=='1'):
        print("Checkout: Item: "+str(Item)+" User: "+str(User))

    if(Item!=None and Item!='None') and (User!=None and User!='None'):
        Rescheck = 0;

    #fetches current cvs for Inventry
    filename="./static/storage/HelpdeskCheckoutItems.csv"
    InventoryList = csvtodict(filename)

    #fetches current cvs for REserved Item and Checked out Item
    filename="./static/storage/CheckedoutandReserved.csv"
    ReservedList = csvtodict(filename)

    #fetches current cvs for Inventry
    filename="./static/storage/OnidUsernames.csv"
    OnidList = csvtodict(filename)
    #print(OnidList)

    readCSV = csvRowsList(filename)
    row_you_want = readCSV[1]
    print(row_you_want)

    readCSV = csvSpecificRows(filename, 1)
    row_you_want = readCSV
    print(row_you_want)

    return render_template('Homepage.html',
        x=x,
        InventoryList=InventoryList,
        OnidList=OnidList,
        ReservedList=ReservedList,
        Item=Item,
        User=User,
        In=In,
        Out=Out,
        Destination=Destination,
        Description=Description,
        CheckoutTrigger=CheckoutTrigger,
        Rescheck=Rescheck)

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
