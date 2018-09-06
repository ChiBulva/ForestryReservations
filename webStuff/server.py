from flask import Flask, render_template, url_for, request
import os
import csv

app = Flask(__name__)

# CSV functions
################################################################################################################################################################
# -                                     1       2       3       4       5         6       7       8       9       10
# - Files:  HelpdeskItems           ( Number, Item,  ItemType,Status,Description )
# -         CheckedoutandReserved   ( Item,   User,    In,    Out,    Dest,     Desc,  Status )
# -         OnidUsernames           ( Onid )
# -
# - Needs:  Buttons: ReserveItem
# -
def checkoutitem(Item, User, In, Out, DateIn, DateOut, Destination, Description):
    DesiredStatus = "out"
    #Error checking done here
    #
    changeStatus(DesiredStatus, Item)
    delRowFromCheckedOutAndReserved(Item, User, "reserved")
    addRowToCheckedOutAndReserved(Item, User, In, Out, DateIn, DateOut, Destination, Description, DesiredStatus)
# -
# -
def checkinitem(Item, User):
    DesiredStatus = "in"
    print(User)
    print(Item)
    changeStatus(DesiredStatus, Item)
    delRowFromCheckedOutAndReserved(Item, User, DesiredStatus)
# -
# -
def reserveitem(Item, User, In, Out, DateIn, DateOut, Destination, Description):
    DesiredStatus = "reserved"
    changeStatus(DesiredStatus, Item)
    delRowFromCheckedOutAndReserved(Item, User, "out")
    addRowToCheckedOutAndReserved(Item, User, In, Out, DateIn, DateOut, Destination, Description, DesiredStatus)

def reservecheckout(Item, User):
    DesiredStatus = "out"
    changeStatus(DesiredStatus, Item)
# -
# -
################################################################################################################################################################
# +  Actual manipulation of CSV files
# +
def changeStatus(DesiredStatus, Item):
    inputfile = csv.reader(open('./static/storage/HelpdeskItems.csv','r'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        if(row[1]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(DesiredStatus)),(str(row[4]))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/HelpdeskItems.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)

def ResToOut(DesiredStatus, Item):
    print("INSIDE OMG")
    inputfile = csv.reader(open('./static/storage/HelpdeskItems.csv','r'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        if(row[1]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(DesiredStatus)),(str(row[4]))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/HelpdeskItems.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)

    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r'))
    #outfile =
    newFileArray = []
    for row in inputfile:
        print(row)
        if(row[0]==Item):
            newFileArray.append([(str(row[0])),(str(row[1])),(str(row[2])),(str(row[3])),(str(row[4])),(str(row[5])),(str(row[6])),(str(row[7])),(str(DesiredStatus))])
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)
# +
# +
def addRowToCheckedOutAndReserved(Item, User, TimeIn, TimeOut, DateIn, DateOut, Dest, Desc, DesiredStatus):
    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r'))
    newFileArray = []
    for row in inputfile:
        newFileArray.append(row)

    newFileArray.append([Item, User, TimeIn, TimeOut, DateIn, DateOut, Dest, Desc, DesiredStatus])

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)
# +
# +
def delRowFromCheckedOutAndReserved(Item, User,  DesiredStatus):
    inputfile = csv.reader(open('./static/storage/CheckedoutandReserved.csv','r'))
    newFileArray = []
    for row in inputfile:
        if(row[1]==User and row[0]==Item):
            print("Skipped: "+str(User))
        else:
            newFileArray.append(row)

    outfile = csv.writer(open('./static/storage/CheckedoutandReserved.csv','w'))
    for row in newFileArray:
        #print(row)
        outfile.writerow(row)
# +
# +
################################################################################################################################################################

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

# Turns a csv into a dictionary for easier display
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
@app.route('/', methods=['GET', 'POST', 'Item', 'User', 'lenInventoryList', 'TimeIn', 'TimeOut', 'DateIn', 'DateOut', 'Destination', 'Description', 'Rescheck', 'CheckoutTrigger', 'ReserveTrigger', 'CheckinTrigger', 'CheckOutRes'])
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
    TimeIn = data.get('TimeIn')
    TimeOut = data.get('TimeOut')
    Destination = data.get('Destination')
    Description = data.get('Description')
    CheckoutTrigger = data.get('CheckoutTrigger')
    ReserveTrigger = data.get('ReserveTrigger')
    CheckinTrigger = data.get('CheckinTrigger')
    CheckOutRes = data.get('CheckOutRes')
    DateIn = data.get('DateIn')
    DateOut = data.get('DateOut')
    Rescheck = 1

    print()
    print(CheckoutTrigger)
    print(ReserveTrigger)
    print()

    #will check out an item
    if(CheckoutTrigger=='Checkout Item'):
        checkoutitem(Item, User, TimeIn, TimeOut, DateIn, DateOut, Destination, Description)

    elif(CheckinTrigger=='Check-In'):
        checkinitem(Item, User)
        Item = 'None'
        User = 'None'

    elif(CheckOutRes=='Check Out'):
        ResToOut("out", Item)
        Item = 'None'
        User = 'None'

    elif(ReserveTrigger=='Reserve Item'):
        reserveitem(Item, User, TimeIn, TimeOut, DateIn, DateOut, Destination, Description)

    if(Item!=None and Item!='None') and (User!=None and User!='None'):
        Rescheck = 0;

    #fetches current cvs for Inventry
    filename="./static/storage/HelpdeskItems.csv"
    InventoryList = csvtodict(filename)

    #fetches current cvs for REserved Item and Checked out Item
    filename="./static/storage/CheckedoutandReserved.csv"
    ReservedList = csvtodict(filename)

    #fetches current cvs for Inventry
    filename="./static/storage/OnidUsernames.csv"
    OnidList = csvtodict(filename)
    #print(OnidList)

    #readCSV = csvRowsList(filename)
    #row_you_want = readCSV[1]
    #print(row_you_want)

    #readCSV = csvSpecificRows(filename, 1)
    #row_you_want = readCSV
    #print(row_you_want)

    return render_template('Homepage.html',
        x=x,
        InventoryList=InventoryList,
        OnidList=OnidList,
        ReservedList=ReservedList,
        Item=Item,
        User=User,
        TimeIn=TimeIn,
        TimeOut=TimeOut,
        Destination=Destination,
        Description=Description,
        CheckoutTrigger=CheckoutTrigger,
        ReserveTrigger=ReserveTrigger,
        CheckinTrigger=CheckinTrigger,
        CheckOutRes=CheckOutRes,
        DateIn=DateIn,
        DateOut=DateOut,
        Rescheck=Rescheck)

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
